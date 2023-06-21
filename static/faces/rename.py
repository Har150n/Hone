# import os
# from PIL import Image
#
# folder_path = "."  # Update with the folder path where your images are located
# prefix = "disgust"
# extension = ".jpg"
#
# # Get all the JPEG files in the folder
# jpg_files = [file for file in os.listdir(folder_path) if file.endswith(".jpg")]
#
# # Sort the files to ensure consistent renaming
# jpg_files.sort()
#
# # Rename the files
# for i, file in enumerate(jpg_files, start=1):
#     old_path = os.path.join(folder_path, file)
#     new_name = f"{prefix}{i}{extension}"
#     new_path = os.path.join(folder_path, new_name)
#
#     # Rename the file
#     os.rename(old_path, new_path)
#
#     # Update the image metadata if needed (optional)
#     image = Image.open(new_path)
#     image.save(new_path)  # Save the image with updated metadata
#
#     print(f"Renamed {file} to {new_name}")
#
# print("All files renamed successfully.")

for emotion in ['happy', 'sad', 'angry', 'disgust', 'neutral', 'fear']:
    for i in range(1,   13):
        print(emotion + str(i) + '.jpg')
