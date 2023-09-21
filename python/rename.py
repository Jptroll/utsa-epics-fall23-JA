import os

def rename_images(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only image files
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'))]
    
    # Sort the image files
    image_files.sort()
    
    # Rename images sequentially
    for index, image_file in enumerate(image_files, start=1):
        _, ext = os.path.splitext(image_file)
        new_name = f"juan_{index}{ext}"
        old_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {image_file} -> {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\Jptroll\\Desktop\\python"  # Replace with your folder path
    rename_images(folder_path)


