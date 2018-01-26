from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import engines1
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class SimpleForm(Form):
    recipe = TextField('Recipe:', validators=[validators.required()]) 
    
"""
This section of the script will add some descriptive text to each of the engines
"""

simple_text = 'This engine will take recipe IDs from the Yummly recipe dataset and output recipes of the most similar recipes that occur in that dataset. The IDs are randomly ordered, so a real application of this engine would be on the backend, when users try a recipe and perhaps rate it highly, the recommendations can be given for additional recipes to try. For demo purposes, here are a few of the recipe IDs you can try to start with: 4758, 10259, 25693, 20130, 22213, 13162, 6602, 42779, 3735, 16903, 12734'

discovery_text = 'In contrast to the "Recipe ID Recommendations" engine, this engine will take in the recipe ID of a recipe that a user tries out or rates highly on the Yummly service, and will output recipes which are the most similar in the Yummly dataset, while being of cuisines that are different from the original recipe cuisine that the user has tried. This can be used as a recipe discovery engine that can encourage users to try recipes that they are likely to enjoy by remaining as similar as possible to the recipes they rate highly while introducing them to new cuisine variants. As before, the IDs are randomly ordered, so a real application of this engine would be on the backend. For demo purposes, here are a few of the recipe IDs you can try to start with: 4758, 10259, 25693, 20130, 22213, 13162, 6602, 42779, 3735, 16903, 12734'

ingredients_list_text = 'This engine will take a list of ingredients from the user and can produce recipes from the yummly dataset that best approximate the ingredients they have (perhaps already in their kitchen, or in their cooking interests). * A Quick note: user text processing has not been implemented in this demo version of the engine yet, so for best results try using a list of ingredients all in lower case, without any plurals, verbs or adjectives. Example ingredients that will be recognized in this version: single items such as "beef" or "strawberry", and list entries such as "chicken, milk, sausage, butter"'

complimentary_text = 'This engine will take a list of ingredients from the user and can produce suggestions for ingredients that are likely to compliment the ingredients well based on how often they occur together in recipes in the Yummly dataset. * A Quick note: user text processing has not been implemented in this demo version of the engine yet, so for best results try using a list of ingredients all in lower case, without any plurals, verbs or adjectives. Example ingredients that will be recognized in this version: single items such as "beef" or "strawberry", and list entries such as "chicken, milk, sausage, butter"'
 
@app.route("/")
def Home(): 
    return render_template('homepage.html')
    
@app.route("/simple/", methods=['GET', 'POST'])
def SimpleRecommendation():
    form1 = SimpleForm(request.form)
    
    flash(simple_text)
 
    if request.method == 'POST':
        recommendation1=request.form['recipe']
 
        if form1.validate():
            # Save the comment here
            result = engines1.similar_cuisine_recommendations(recommendation1)
            for entry in result:
                flash(entry)
        else:
            flash('All the form fields are required. ')
 
    return render_template('engines.html', form=form1)

@app.route("/discovery/", methods=['GET', 'POST'])
def DiscoveryRecommendation():
    form1 = SimpleForm(request.form)
    
    flash(discovery_text)
 
    if request.method == 'POST':
        recommendation1=request.form['recipe']
 
        if form1.validate():
            # Save the comment here
            result = engines1.unique_cuisine_recommendations(recommendation1)
            for entry in result:
                flash(entry)
        else:
            flash('All the form fields are required. ')
 
    return render_template('engines.html', form=form1)

@app.route("/ingredient_list/", methods=['GET', 'POST'])
def IngredientListRecommendation():
    form1 = SimpleForm(request.form)
    
    flash(ingredients_list_text)
 
    if request.method == 'POST':
        recommendation1=request.form['recipe']
 
        if form1.validate():
            # Save the comment here
            result = engines1.ingredient_list_recommendations(recommendation1)
            for entry in result:
                flash(entry)
        else:
            flash('All the form fields are required. ')
 
    return render_template('engines.html', form=form1)
 
@app.route("/complimentary/", methods=['GET', 'POST'])
def ComplimentaryRecommendation():
    form1 = SimpleForm(request.form)
    
    flash(complimentary_text)
 
    if request.method == 'POST':
        recommendation1=request.form['recipe']
 
        if form1.validate():
            # Save the comment here
            message, result = engines1.complimentary_ingredients(recommendation1)
            for entry in message:
                flash(entry)
            for entry in result:
                flash('* {0}'.format(entry))
        else:
            flash('All the form fields are required. ')
 
    return render_template('engines.html', form=form1)    

if __name__ == "__main__":
    app.run()