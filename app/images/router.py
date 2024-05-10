import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_image


router = APIRouter(
    prefix='/images',
    tags=['Upload images']
)

@router.post('/upload')
async def create_upload_file(name: str, file: UploadFile):
    im_path = f'app/static/images/{name}.webp'
    with open(im_path, 'wb') as file_object:
        shutil.copyfileobj(file.file, file_object)

        process_image.delay(path=im_path)

    return 'Success'
