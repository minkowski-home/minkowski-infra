import os

# Path to the folder where this script is running
base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "product_images")

# Ensure base images directory exists
os.makedirs(images_dir, exist_ok=True)

# Create folders product_1 to product_50
for i in range(1, 51):
    folder_name = f"product_{i}"
    folder_path = os.path.join(images_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
