from pathlib import Path
import smtplib
import ssl

from PIL import Image
from pydantic import EmailStr

from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_template
from app.config import settings


@celery.task
def process_image(path: str,
                  target_width: int = 1000,
                  target_height: int = 600,
                  shrink_factor: int = 3,
                  ) -> None:
    '''
    Proportionally resize the image by the selected width.
    '''

    im_path = Path(path)
    im = Image.open(im_path)

    # Calculate the aspect ratio of the image.
    aspect_ratio = im.size[0] / im.size[1]

    # Calculate the new dimensions
    # based on the aspect ratio and target dimensions.
    # If the original image is wider than it is tall:
    if aspect_ratio > 1:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    # If the original image is taller than it is wide:
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    # Resize the image while maintaining aspect ratio.
    im_resized_big = im.resize(
        (new_width, new_height))
    im_resized_small = im.resize(
        (int(new_width / shrink_factor),
         int(new_height / shrink_factor)))

    im_resized_big.save(str(
        f'app/static/images/resized_big{im_path.name}'))
    im_resized_small.save(str(
        f'app/static/images/resized_small{im_path.name}'))


email_to_mock = settings.SMTP_USER


@celery.task
def send_booking_confirmation(
    email_info_dict: dict,
    email_to: EmailStr = email_to_mock,
) -> None:
    msg = create_booking_confirmation_template(email_info_dict, email_to)

    with smtplib.SMTP(host=settings.SMTP_HOST,
                      port=settings.SMTP_PORT,
                      timeout=10) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.sendmail(msg['From'], msg['To'], msg.as_string())

    print(f'Successfully sent confirmation email to {msg['To']}')
