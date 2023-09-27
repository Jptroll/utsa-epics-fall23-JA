import os
import shutil

def split_images_into_folders(source_folder):
    num_folders = 5
    images_per_folder = 10
    
    # Create the destination folders JA
    for i in range(num_folders):
        folder_name = f"folder_{i+1}"
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path)
    
    # Get a list of image files in the source folder JA
    image_files = [file for file in os.listdir(source_folder) if file.startswith("juan_")]
    image_files.sort()  # Sort the image files
    
    # Move images into the destination folders
    folder_index = 0
    for index, image_file in enumerate(image_files, start=1):
        if index > images_per_folder:
            folder_index += 1
            images_per_folder += 10
        
        src_path = os.path.join(source_folder, image_file)
        dest_folder = f"folder_{folder_index+1}"
        dest_path = os.path.join(source_folder, dest_folder, image_file)
        
        shutil.move(src_path, dest_path)
        print(f"Moved: {image_file} -> {dest_folder}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\Jptroll\\Desktop\\python"  # Replace with your folder path
    split_images_into_folders(folder_path)
