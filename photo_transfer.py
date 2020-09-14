# Move select photos from external SD card onto main drive in the correct folder 
# Sort remaining photos into correct folder on an external drive for storage 

# Note 1: os.listdir(path) - returns directories in a path as a list  
# Note 2: Python scripts from terminal can be terminated using Ctl + C
# Note 3: string to integer is int('string'), integer to string is str(integer)

# Path to storage drive: /Volumes/"Personal Drive 1/Pictures/"
# Path to camera SD card: /Volumes/"Nikon D3300/DCIM/100D3300/" 
# Path to pictures folder: /Users/samdonnelly/Pictures/

# Photos on camera SD card are in the format: DSC_XXXX.JPG where XXXX is a four digit number starting at 0001

# Improvements:
# - Check if an external drive is connected and give option to insert or do without it
# - Make the save_image() function add zeros to file name if needed

import shutil as s 
import os


def file_location(text):
    # create path to storage folders
    while True:
        path = input(text)

        # Add a slash to the beginning of the path if needed to make the path valid
        if path[0] != '/':
            path = '/' + path

        # Check validity of path before continuing
        location_check = os.path.isdir(path)
        if location_check is True:
            # Append a slash to the paths if needed
            if path[-1] != '/':
                path = path + '/'
            break
        else:
            print("Invalid path")
    return path


def save_images():
    # Move desired photos to a local folder
    print("Enter the number of the photo to save it.")
    print("Input 'done' or 'end' to finish saving photos.")
    while True:
        file = input("Image to save: ")

        if file == 'done' or file == "end":
            break

        try:
            file_name_int = int(file)

            if file_name_int < lower_limit or file_name_int > upper_limit:
                print("Out of range")
                continue  # resets the while loop

            file = image_file + file + file_format

            if file in images_list:
                from_path = retrieval_path + file
                to_path = full_path + file
                s.move(from_path, to_path)

        except ValueError:
            print("invalid input")
            continue
    return file


def move_image():
    # Move remaining photos to storage
    # Ensures that only photos within specified range are moved to the folder
    for x in range(lower_limit, upper_limit + 1):
        if x < 10:
            file = image_file + '000' + str(x) + file_format
        elif 10 <= x < 100:
            file = image_file + '00' + str(x) + file_format
        elif 100 <= x < 1000:
            file = image_file + '0' + str(x) + file_format
        else:
            file = image_file + str(x) + file_format

        if file in new_image_list:
            from_path = retrieval_path + file
            to_path = full_storage_path + file
            s.move(from_path, to_path)


# Define repeated parts of image file names
image_file = "DSC_"
file_format = ".JPG"

while True:
    # Main loop

    # Where images are initially located (SD Card) 
    retrieval_path = "/Volumes/Nikon D3300/DCIM/100D3300/"

    # Choose folder name
    folder_name = input("Folder name: ")
    if folder_name[-1] != '/':
        folder_name = folder_name + '/'

    # Choose local and external paths for storing photos
    local_path = file_location('Location of local folder: ')
    storage_path = file_location('Location of external folder: ')

    # Append folder name onto the end of path 
    full_path = local_path + folder_name
    full_storage_path = storage_path + folder_name
    print("Path to saved photos: ", full_path)
    print("Path to storage: ", full_storage_path)

    # Create folders using chosen name
    try:
        os.mkdir(full_path)
        os.mkdir(full_storage_path)
    except FileNotFoundError:
        print("The path could not be created. Please check that the folder name is correctly formatted")
        continue

    # Input range of photo file names 
    limits = [None]*2
    limits[0] = input("Lower limit image number: ")
    lower_limit = int(limits[0])
    limits[1] = input("Upper limit image number: ") 
    upper_limit = int(limits[1])

    # Alternate code to the section above
    """
    limits = []
    lower_limit = input("lower limit image number: ")
    upper_limit = input("Upper limit image number: ")
    limits.append(lower_limit)
    limits.append(upper_limit)
    """

    # Return image file directory from SD card as a list
    images_list = os.listdir(retrieval_path)

    # Select photos to store in folder and move them
    # 'images_list' is used here
    file_name = save_images()

    # Return directory as a list with select photos removed 
    new_image_list = os.listdir(retrieval_path)

    # Move remaining photos to storage
    move_image()

    # Choose to sort more photos
    while True:
        ans = 0
        answer = input("Sort more photos? Y/N ")
        answer.lower()
        if answer == "y" or answer == 'yes':
            ans = 1
            break
        elif answer == 'n' or answer == 'no':
            break
        else:
            continue

    if ans == 1:
        continue
    else:
        break
