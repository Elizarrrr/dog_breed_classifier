#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 

    # Initialize the results statistics dictionary
    results_stats_dic = {}
    
    # Initialize all counters to zero
    n_images = 0        # Total number of images
    n_dogs_img = 0      # Number of dog images
    n_notdogs_img = 0   # Number of non-dog images
    n_match = 0         # Labels that match exactly
    n_correct_dogs = 0  # Dogs correctly identified as dogs
    n_correct_notdogs = 0 # Non-dogs correctly identified as not dogs
    n_correct_breed = 0 # Dog breed correctly identified
    
    # Loop through each image in the results dictionary and count each category
    for filename in results_dic:
        # Get the values from the results dictionary
        # Format: [pet_label, classifier_label, label_match, is_dog_pet, is_dog_classifier]
        label_match = results_dic[filename][2]  # 1=match, 0=no match
        is_dog_pet = results_dic[filename][3]   # 1=pet is dog, 0=not dog
        is_dog_classifier = results_dic[filename][4] # 1=classifier says dog, 0=not dog
        
        # Increment total number of images
        n_images += 1
        
        # Check if the pet label is a dog
        if is_dog_pet == 1:
            n_dogs_img += 1
        else:
            n_notdogs_img += 1
        
        # Check if the classifier label matches the pet label
        if label_match == 1:
            n_match += 1
        
        # Check if the classifier correctly classified a dog image as a dog
        if is_dog_pet == 1 and is_dog_classifier == 1:
            n_correct_dogs += 1
        
        # Check if the classifier correctly classified a non-dog image as not a dog
        if is_dog_pet == 0 and is_dog_classifier == 0:
            n_correct_notdogs += 1
        
        # Check if the classifier correctly identified the breed of a dog
        if is_dog_pet == 1 and label_match == 1:
            n_correct_breed += 1
    
    # Store the counts in the results statistics dictionary
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    
    # Calculate percentages (avoid division by zero)
    
    # Percentage of images with matching labels
    if n_images > 0:
        results_stats_dic['pct_match'] = (n_match / n_images) * 100
    else:
        results_stats_dic['pct_match'] = 0
    
    # Percentage of dog images correctly classified as dogs
    # Percentage of dog breeds correctly identified
    if n_dogs_img > 0:
        results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100
        results_stats_dic['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100
    else:
        results_stats_dic['pct_correct_dogs'] = 0
        results_stats_dic['pct_correct_breed'] = 0
    
    # Percentage of non-dog images correctly classified as not dogs
    if n_notdogs_img > 0:
        results_stats_dic['pct_correct_notdogs'] = (n_correct_notdogs / n_notdogs_img) * 100
    else:
        results_stats_dic['pct_correct_notdogs'] = 0

    return results_stats_dic