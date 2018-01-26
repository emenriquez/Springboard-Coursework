#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:37:55 2018

@author: Erik
"""

# import packages to read and work with data
import pandas as pd
import numpy as np
from collections import defaultdict

# Packages for working with text data
from nltk import tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Tools for Recommendations
from sklearn.neighbors import NearestNeighbors

# Load the cleaned dataset from the data folder
data = pd.read_pickle('data_clean.pkl')

# drop the words column of data
data.drop('words', axis=1, inplace=True)

# Convert the recipe ingredient lists into strings
ingredient_strings = [', '.join(recipe) for recipe in data.ingredients]
data.ingredients = ingredient_strings

# Custom tokenizer to separate list into tokens by commas
tokenized = tokenize.regexp.RegexpTokenizer(pattern=", ", gaps=True)

# Create TF-IDF weighting dictionary for each cuisine, exclude terms that appear in every cuisine
tfidf = TfidfVectorizer(tokenizer=tokenized.tokenize, max_df=0.12, binary=True, use_idf=False, norm=None)

# Fit and transform cuisine ingredient lists to generate sparse matrix
ingredients_weighted = tfidf.fit_transform(data.ingredients)

def preprocess_user_input(user_input):
    return None

def similar_cuisine_recommendations(user_recipe_id, n_recommendations=3):
    """
    This function takes in the id of a recipe for a user, and generates similar recipe recommendations.
    """
    output_string = []
    try:
        user_recipe_id = int(user_recipe_id)
    except:
        output_string.append('Oh no! This recipe is not in our database!')
        output_string.append('Here are a few recipe IDs you can try:')
        output_string.append('4758, 23260, 37648, 11935, 4407')
        return output_string
    # Define a map between ingredients_weighted and data ID's
    assert ingredients_weighted.shape[0] == data.shape[0]
    
    ingredients_weighted_indices_dict = defaultdict(int)
    for i in range(data.shape[0]):
        ingredients_weighted_indices_dict[data.index[i]] = i

    if user_recipe_id not in data.index:
        output_string.append('Oh no! This recipe is not in our database!')
        output_string.append('Here are a few recipe IDs you can try:')
        output_string.append('4758, 23260, 37648, 11935, 4407')
    else:        
        # Find nearest neigbors among all recipes
        nbrs = NearestNeighbors(n_recommendations+1).fit(ingredients_weighted)
        indices = nbrs.kneighbors(ingredients_weighted[ingredients_weighted_indices_dict[user_recipe_id]], return_distance=False)
        output_string.append('Your recipe:')
        output_string.append('RECIPE ID: {0}'.format(user_recipe_id))
        output_string.append('CUISINE: {0}'.format(data.loc[user_recipe_id].cuisine))
        output_string.append('INGREDIENTS: {0}'.format(data.loc[user_recipe_id].ingredients))
        output_string.append('********************')
    
        output_string.append('\n\nSimilar recipes you might be interested in:')
        for recipe in indices[0][1:]:
            output_string.append('RECIPE ID: {0}'.format(list(data.index)[recipe]))
            output_string.append('CUISINE: {0}'.format(data.iloc[recipe].cuisine))
            output_string.append('INGREDIENTS: {0}'.format(data.iloc[recipe].ingredients))
            output_string.append('========================')
    
    return output_string

# Find nearest neighbors from cuisines distinct from input
def unique_cuisine_recommendations(user_recipe_id, n_recommendations=3):
    """
    This function takes in the id of a recipe for a user, and generates similar recipe recommendations from other cuisines.
    """
    output_string = []
    try:
        user_recipe_id = int(user_recipe_id)
    except:
        output_string.append('Oh no! This recipe is not in our database!')
        output_string.append('Here are a few recipe IDs you can try:')
        output_string.append('4758, 23260, 37648, 11935, 4407')
        return output_string
        
    # Define a map between ingredients_weighted and data ID's
    assert ingredients_weighted.shape[0] == data.shape[0]
    
    ingredients_weighted_indices_dict = defaultdict(int)
    for i in range(data.shape[0]):
        ingredients_weighted_indices_dict[data.index[i]] = i

    
    if user_recipe_id not in data.index:
        output_string.append('Oh no! This recipe is not in our database!')
        output_string.append('Here are a few recipe IDs you can try:')
        output_string.append('4758, 23260, 37648, 11935, 4407')
    else:        
        # Display the record for the user's recipe
        output_string.append('Your recipe:')
        output_string.append('RECIPE ID: {0}'.format(user_recipe_id))
        output_string.append('CUISINE: {0}'.format(data.loc[user_recipe_id].cuisine))
        output_string.append('INGREDIENTS: {0}'.format(data.loc[user_recipe_id].ingredients))
        output_string.append('*********************')
        
        # Create a list of all cuisines
        cuisines_observed = [data.cuisine[user_recipe_id]]
        recommendations = []
            
        for recommendation in range(n_recommendations):
            data_subset = [data.index[i] for i in range(data.shape[0]) if data.loc[data.index[i]].cuisine not in cuisines_observed]
            ingredients_indices = [ingredients_weighted_indices_dict[value] for value in data_subset]
            ingredients_subset = ingredients_weighted[ingredients_indices]
            
            # Find nearest neigbors among cuisine subsets
            nbrs = NearestNeighbors(n_neighbors=2).fit(ingredients_subset)
            index = nbrs.kneighbors(ingredients_weighted[ingredients_weighted_indices_dict[user_recipe_id]],
                                      return_distance=False)
            
            # Append the result to the list for output and add the cuisine to cuisines_observed
            recommendations.append(index[0][0])
            cuisines_observed.append(data.iloc[index[0][0]].cuisine)
    
        # Display the results!
        output_string.append('\n\nTry some of these new recipes you might enjoy!')
        for recommendation in recommendations:
            output_string.append('RECIPE ID: {0}'.format(list(data.index)[recommendation]))
            output_string.append('CUISINE: {0}'.format(data.iloc[recommendation].cuisine))
            output_string.append('INGREDIENTS: {0}'.format(data.iloc[recommendation].ingredients))
            output_string.append('========================')
    
    return output_string

def ingredient_list_recommendations(user_ingredients_string, n_recommendations=3):
    """
    This function takes in the list of ingredients from a user, and generates similar recipe recommendations.
    """
    
    output_string = []
    # Transform the recipe ingredients vector to TF-IDF format
    user_tfidf = tfidf.transform([user_ingredients_string])
    user_ingredient_list = user_ingredients_string.split(', ')
    
    # Find nearest neigbors among all recipes
    nbrs = NearestNeighbors(n_recommendations).fit(ingredients_weighted)
    indices = nbrs.kneighbors(user_tfidf, return_distance=False)

    output_string.append('\n\nYou can try these recipes!')
    
    # loop through nearest neighbors = n_recommendations
    for neighbor in range(n_recommendations):
        
        # List ingredients (if needed) to make neighbor recipe
        neighbor_ingredients = (data.iloc[indices[0][neighbor]].ingredients).split(', ')
        missing_ingredients = [ingredient for ingredient in neighbor_ingredients if ingredient not in user_ingredient_list]
        
        # Print a border between recipes
        output_string.append('\n------------------------------\n')
        
        # Display recipes that user can make
        if len(missing_ingredients) == 0:
            output_string.append('\nYou have all of the ingredients needed to make this recipe!')
            output_string.append('RECIPE ID: {0}'.format(list(data.index)[indices[0][neighbor]]))
            output_string.append('CUISINE: {0}'.format(data.iloc[indices[0][neighbor]].cuisine))
            output_string.append('INGREDIENTS: {0}'.format(data.iloc[indices[0][neighbor]].ingredients))
            
        else:
            # Display recipes that can be made
            output_string.append('\nIf you buy: {0}'.format(missing_ingredients))
            output_string.append('\nYou can make:')
            output_string.append('RECIPE ID: {0}'.format(list(data.index)[indices[0][neighbor]]))
            output_string.append('CUISINE: {0}'.format(data.iloc[indices[0][neighbor]].cuisine))
            output_string.append('INGREDIENTS: {0}'.format(data.iloc[indices[0][neighbor]].ingredients))
    
    output_string.append('\n------------------------------\n')
    
    return(output_string)

# Convert to dense format for simpler handling
ingredients_dense = ingredients_weighted.todense()

# create a matrix of zeros to fill co-occurence values into
ingredient_pairs = np.zeros((ingredients_dense.shape[1], ingredients_dense.shape[1]))

# loop through ingredients and calculate fraction of recipes in which they occur together
for i in range(ingredients_dense.shape[1]):
    ingredient_indices = np.where(ingredients_dense[:,i] == 1)[0]
    ingredient_pairs[i,:] = ingredients_dense[ingredient_indices, :].sum(axis=0)/len(ingredient_indices)
    ingredient_pairs[i,i] = 0

def complimentary_ingredients(user_ingredient_list_string, n_recommendations=3):
    """
    This function takes in a list of ingredients from a user and suggests ingredients that are 
    most likely to compliment the set.
    """
    output_string = []
    # Convert string input to list
    user_ingredient_list = user_ingredient_list_string.split(', ')
    
    # Create a sublists of users ingredients that are in the ingredient pairings matrix
    ingredient_sublist = [ingredient for ingredient in user_ingredient_list if ingredient in tfidf.vocabulary_.keys()]
    output_string.append('Searching for compliments to the following recognized ingredients:')
    if len(ingredient_sublist) == 0:
        output_string.append('Nothing!')
    else:
        output_string.append(ingredient_sublist)
    output_string.append('**************************')
    
    if len(ingredient_sublist) == 0:
        recommended_ingredients = ['No ingredients recognized for matching! Please try again!',
                                   'You may want to try some of the following: cumin, strawberry, beef, sake, celery']
    else:
        # Extract indices of the rows in the matrix for the given ingredients
        ingredient_indices = [sorted(tfidf.vocabulary_).index(ingredient) for ingredient in ingredient_sublist]
            
        # Sum up the co-occurences of all ingredients and return the ingredients with the highest combined co-occurence scores
        top_pairings = np.argsort(ingredient_pairs[ingredient_indices,:].sum(axis=0))[::-1]
        top_complimentary_ingredients = [ingredient for ingredient in top_pairings if ingredient not in ingredient_sublist]
        
        # Convert the indices back into ingredient names for display
        recommended_ingredients = [sorted(tfidf.vocabulary_)[i] for i in top_complimentary_ingredients[:n_recommendations]]
        output_string.append('These might pair well with your ingredients!')
        
    # Display the recommendations to the user
    return(output_string, recommended_ingredients)