import os
from PIL import Image

# Set the path to your image folder
folder_path = "images"
new_size = (800, 600)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        full_path = os.path.join(folder_path, filename)
        image = Image.open(full_path)
        resized_image = image.resize(new_size)
        save_path = os.path.join(folder_path, "resized_" + filename)
        resized_image.save(save_path)
        print(f"{filename} resized and saved as {save_path}")
