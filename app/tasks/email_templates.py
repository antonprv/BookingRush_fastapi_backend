from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pydantic import EmailStr

from app.config import settings


def create_booking_confirmation_template(
    email_info_dict: dict,
    email_to: EmailStr,
):
    message = MIMEMultipart("alternative")

    message['Subject'] = 'Booking confirmation'
    message['From'] = settings.SMTP_USER
    message['To'] = email_to

    html_text = f'''
        <h1>Booking Confirmation</h1>
        <h2>Booking details:</h2>
        <p>You've booked a hotel for this period of time:<br>
        from {email_info_dict['date_from']} to {email_info_dict['date_to']}<br>
        Total amount of days: {email_info_dict['total_days']}<br>
        Total cost: {email_info_dict['total_cost']}<br>
        Hotel name: {email_info_dict['hotel_name']}<br>
        Room name: {email_info_dict['hotel_room_name']}<br>
        Room description: {email_info_dict['hotel_room_description']}<br>
        Room services: {', '.join(
            service for service in email_info_dict['hotel_room_services'])}<br>
        Hotel location: {email_info_dict['hotel_location']}<br>
        Hotel services: {', '.join(service for service in email_info_dict['hotel_services'])}<br>
        User email: {email_info_dict['user_email']}</p>
        '''
    html_content = MIMEText(html_text, 'html')
    message.attach(html_content)

    return message
