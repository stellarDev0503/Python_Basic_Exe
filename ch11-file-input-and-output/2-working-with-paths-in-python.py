# 11.2 - Working With Paths in Python
# Solutions to review exercises


# Initial setup
import os
import glob
# This path may need to be changed depending on your setup
path = "C:/Real Python/refactor/chp10/practice_files/images"


# Exercise 1
# Display the full paths of all files and folders in the main "images" folder
print('Full contents of "images" folder:')
for file_name in os.listdir(path):
    print(os.path.join(path, file_name))


# Exercise 2
# Display the full paths of any PNG files in the "images" folder
file_matches = os.path.join(path, "*.png")
print('All PNG files in "images" folder:')
for file_name in glob.glob(file_matches):
    print(file_name)


# Exercise 3
# Change all PNGs to JPGs in the "images" folder and its subfolders
# Could use indexing to get the file extension, but try using os.path.splitext()
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        file_path = os.path.join(current_folder, file_name)
        file_tuple = os.path.splitext(file_path)  # split into (path, extension)
        if file_tuple[1].lower() == ".png":  # check if extension is PNG
            pass  # os.rename(file_path, file_tuple[0] + ".jpg")


# Exercsie 4
# Check that the two files have been converted to JPGs successfully
print(os.path.exists(os.path.join(path, "png file - not a gif.jpg")))
print(os.path.exists(os.path.join(path, "additional files/one last image.jpg")))


# Exercise 5
os.mkdir("Output")
with open("Output/python.txt", "w") as out_file:
    out_file.write("I was put here by Python!")
