from PIL import Image
import os

def preprocess_frame_images(input_dir: str):
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            path = os.path.join(input_dir, filename)
            with Image.open(path) as img:
                # Example: resize and convert to RGB
                img = img.resize((224, 224)).convert("RGB")
                img.save(path)  # Overwrite or save to a new directory

