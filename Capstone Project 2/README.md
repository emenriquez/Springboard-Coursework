# Classification of Food Categories using Ingredients
Erik Enriquez

**Problem**: Food is a massive and complex arena in which culture, geography, climate, and social factors combine to create unique cuisines around the world. With the age of the internet, millions of recipes are now shared instantly and easily accessible. Many ingredients previously specific to certain regions of the world are now also widely available due to online commerce. With this dataset, provided by Yummly, I aim to answer the following questions:

1. What are the ingredients uniquely used or combined that make up the “signatures” of particular cuisines?  
2. Can we learn more about the origins of cuisine by analyzing their ingredients to provide insights into the cultures and regions from which they originate?  

**Client**: The client for this project would be a recipe-hosting website, such as Yummly. Being able to intelligently group recipes into cuisine categories could improve new recipe discovery and engagement for their users. Some applications of a model that can group cuisines include recommendation of a cuisine based on available ingredients, or suggested pairings of spices and or other ingredients based on ingredients that are frequently used together.

**Data**: Yummly has provided a dataset containing entries of recipe IDs linked to ingredients lists and pre-labeled categories of cuisines. This dataset is available here. The data includes approximately 40,000 entries of recipes for the following categories of cuisine:

Italian  
French  
Spanish  
Filipino  
Mexican  
Cajun/Creole  
Korean  
Irish  
Southern U.S.  
Thai  
Vietnamese  
Jamaican  
Indian  
Japanese  
Moroccan  
Russian  
Chinese  
Greek  
British  
Brazilian  

**Approach**: The proposed project is a supervised learning problem, which will require multinomial classification techniques due to the multiple outcome classes of the variable we are interested in. The dependent variable of interest for this project will be the “cuisine” category of the ingredients list, which includes 20 classes, listed above.

The created features from the dataset will be used for prediction, with feature selection/engineering techniques employed to maximize the predictive accuracy of the model. Several models will be employed and compared, including: Logistic Regression, Naive Bayes, Random Forests, and Gradient Boosting techniques.

**Deliverables**: Deliverables for this project will include code and report submissions posted in a github repository (here) for the following:
1. Code for dataset cleaning, exploration/visualization, and model development  
2. Report on analysis and findings for the proposed problems  
3. Slide deck presentation of this project  
