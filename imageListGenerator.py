import os
import re

# Path to the folder containing images
folder_path = "assets"

# Initialize the dictionary
images = {}

# Loop through the folder and enumerate image files
for index, filename in enumerate(os.listdir(folder_path), start=1):
    # Filter for image files (optional: based on extensions)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Create a key-value pair

        value = os.path.join(folder_path, filename)  # Full path to the image file
        year = re.findall(r'\d+', filename)  # Fetches the year in the image name

        if year:  # Ensure that the year was found
            key = f"Mapas del {year[0]}"

            # If the key already exists, append the new image to the list, otherwise create a new list
            if key in images:
                images[key].append(value)
            else:
                images[key] = [value]
    
    # Uncomment to check if the file exists
        # if os.path.exists(value):
        #     print(f"File {value} exists.")
        # else:
        #     print(f"File {value} does not exist!")

def getImages():
    return images

# Uncomment this to see the resulting dictionary (Testing purposes)
# print(images)

# TESTING --------------------------------------------------------------------------------------------------

# Check File Accessibility
# for key, value in images.items():
#     try:
#         with open(value, "rb") as file:
#             print(f"Successfully opened {value}")
#     except IOError:
#         print(f"Failed to open {value}")

# Print the File Paths
# for key, value in images.items():
#     print(f"{key}: {value}")