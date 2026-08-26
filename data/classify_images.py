#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROGRAMMER: Your Name
# DATE CREATED: 2024-01-15
# REVISED DATE: 2024-01-15

from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Uses the classifier function to classify each image and compares the
    classifier's label with the pet label.
    
    Args:
       images_dir - The path to the directory containing the pet images
       results_dic - The dictionary containing the pet labels
       model - The CNN model architecture to use (vgg, alexnet, resnet)
    
    Returns:
       None - The results_dic is updated in place with the classifier labels
              and a comparison flag (1 if match, 0 if not)
    """
    # Loop through each image filename in the results dictionary
    for filename in results_dic:
        # Build the full path to the image file
        image_path = images_dir + '/' + filename
        
        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)
        
        # Clean the classifier label
        # Convert to lowercase and remove leading/trailing spaces
        classifier_label = classifier_label.lower().strip()
        
        # Get the pet label from the results dictionary
        pet_label = results_dic[filename][0]
        
        # Check if the pet label matches the classifier label
        # Use 'in' operator because classifier label may contain multiple terms
        # Example: pet_label = "beagle", classifier_label = "beagle, english foxhound"
        # e.g. pet_label='dalmatian', classifier_label='dalmatian, coach dog, carriage dog' → match
        if pet_label in classifier_label:
            match = 1 # Labels match
        else:
            match = 0 # Labels don't match
        
        # Add the classifier label and match flag/result to the dictionary
        # Since results_dic is a mutable data type, changes persist outside the function
        # results_dic[filename].extend([classifier_label, match]) # method 2
        results_dic[filename].append(classifier_label)
        results_dic[filename].append(match)
    
    # For Testing
    # print("\nDictionary structure check (first 3 entries):")
    # count = 0
    # for filename in results_dic:
    #     if count < 3:
    #         print(f"Key: {filename}")
    #         print(f"  Index 0 (pet label): {results_dic[filename][0]}")
    #         print(f"  Index 1 (classifier label): {results_dic[filename][1]}")
    #         print(f"  Index 2 (match): {results_dic[filename][2]}")
    #         count += 1
    #     else:
    #         break