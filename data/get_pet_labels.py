#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROGRAMMER: Your Name
# DATE CREATED: 2024-01-15
# REVISED DATE: 2024-01-15

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image files.
    
    Parameters:
     image_dir - The (full) path to the folder of images (string)
    
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a List.
                     index 0 = pet image label (string)
    """
    # Create an empty dictionary
    results_dic = {}
    
    # Get list of all files in the directory
    filenames = listdir(image_dir)
    
    # Loop through each filename
    for filename in filenames:
        # Skip any files that are not .jpg images
        if not filename.endswith('.jpg'):
            continue
        
        # Convert filename to lowercase
        low_filename = filename.lower()
        
        # Split by underscores
        word_list = low_filename.split('_')
        
        # Build the label: join all parts except the last one (which is the number+extension)
        # e.g. 'Boston_terrier_02259.jpg' → ['boston', 'terrier', '02259.jpg'] → 'boston terrier'
        
        # Only keep alphabetic words
        pet_label = "" # Start with empty string
        for word in word_list:
            # Only add words that are purely alphabetic (no numbers)
            if word.isalpha():
                pet_label += word + " " # Add word followed by a space
        
        # Strip off starting/trailing whitespace characters
        pet_label = pet_label.strip()
        
        # Skip if empty
        # If pet_label is empty (shouldn't happen for valid images), skip
        if pet_label == "":
            continue
        
        # Add filename and pet label to dictionary only if filename not already there
        # The value is a list containing the pet label
        if filename not in results_dic:
          results_dic[filename] = [pet_label]

    # return the dictionary(results_dic)
    return results_dic