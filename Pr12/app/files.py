import os
import shutil
import re
from PIL import Image, ImageOps  
from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse

from app.users import current_active_user
from app.user_models import User
from app.schemas import ImageProcessingOptions 

file_router = APIRouter()

UPLOAD_DIR = "uploads"

def process_image(file_location: str, options: ImageProcessingOptions):
    with Image.open(file_location) as img:
        if options.resize:
            match = re.match(r'(\d+)x(\d+)', options.resize)
            if match:
                width, height = map(int, match.groups())
                img = img.resize((width, height))
        
        if options.grayscale:
            img = ImageOps.grayscale(img)
        
        if options.flip:
            if options.flip == 'horizontal':
                img = ImageOps.mirror(img)
            elif options.flip == 'vertical':
                img = ImageOps.flip(img)
        
        if options.convert_to:
            base = os.path.splitext(file_location)[0]
            new_location = f"{base}.{options.convert_to}"
            img.save(new_location, options.convert_to.upper())
            return new_location
        else:
            img.save(file_location)
            return file_location

@file_router.post("/upload/")
def upload_file(
    file: UploadFile = File(...),
    resize: str = Form(None),
    convert_to: str = Form(None),
    grayscale: bool = Form(None),
    flip: str = Form(None),
    user: User = Depends(current_active_user)
):
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    os.makedirs(user_folder, exist_ok=True)

    file_location = os.path.join(user_folder, file.filename)

    with open(file_location, "wb") as buffers:
        shutil.copyfileobj(file.file, buffers)
    
    options = ImageProcessingOptions(
        resize=resize,
        convert_to=convert_to,
        grayscale=grayscale,
        flip=flip
    )

    processed_file_location = process_image(file_location, options)
    
    return {"filename": os.path.basename(processed_file_location)}

@file_router.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str, user: User = Depends(current_active_user)):
    user_folder = f"{UPLOAD_DIR}/{user.id}"
    file_location = os.path.join(user_folder, filename)
    
    if not os.path.exists(file_location):
        raise HTTPException(status_code=404, detail="File not found")
        
    return FileResponse(file_location)