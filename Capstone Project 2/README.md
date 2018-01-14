
# Classification of Cuisines using Recipe Ingredients - Milestone Report

### Table of Contents:
1. [Introduction](#Introduction)
2. [Data Acquisition/Cleaning](#Data)
3. [Data Exploration](#EDA)
4. [Initial Findings](#Findings)
5. [Next Steps](#Next_steps)
6. [Resources](#Resources)

## 1. Introduction <a class="anchor" id="Introduction"></a>

Problem: Food is a massive and complex arena in which culture, geography, climate, and social factors combine to create unique cuisines around the world. With the age of the internet, millions of recipes are now shared instantly and easily accessible. Many ingredients previously specific to certain regions of the world are now also widely available due to online commerce. 

**Objectives**

With this dataset, provided by Yummly, I aim to answer the following questions:

1. **What are the ingredients uniquely used or combined that make up the “signatures” of particular cuisines?**
2. **Can we learn more about the origins of cuisine by analyzing their ingredients to provide insights into the cultures and regions from which they originate?**

**Client**

The client for this project would be a recipe-hosting website, such as Yummly. Being able to intelligently group recipes into cuisine categories could improve new recipe discovery and engagement for their users. Some applications of a model that can group cuisines include recommendation of a cuisine based on available ingredients, or suggested pairings of spices and or other ingredients based on ingredients that are frequently used together.

**Broader Impact**

Beyond directly providing the capability to categorize cuisines based on their ingredients, analysis of this data can provide valuable insight into the evolution of cuisines. If it can be coupled with feedback from a community, such as from users that use and rate the recipe quality on Yummly, it has the potential to be used to create new recipes that intelligently combine ingredients to produce suggestions for promising yet unexplored recipes.

## 2. Data Acquisition/Cleaning <a class="anchor" id="Data"></a>

#### Objectives

1. Load the data and extract general info and structure
2. Deal with outlier values in recipe ingredients
3. Export cleaned version of dataset for further exploration and analysis

### 2.1 Load Original Dataset

The dataset that I am working with can be found in the "data" folder of this repository (filename is train.json), or from its origin at the site for [Kaggle's "What's Cooking?" Competition](https://www.kaggle.com/c/whats-cooking).

To start, the dataset was loaded from a json file into a dataframe so that it could be viewed and modified as needed. Below is the information on the original dataset.


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 39774 entries, 0 to 39773
    Data columns (total 3 columns):
    cuisine        39774 non-null object
    id             39774 non-null int64
    ingredients    39774 non-null object
    dtypes: int64(1), object(2)
    memory usage: 932.3+ KB
    


```python
# Count how many duplicate rows appear in the dataset
data.duplicated(subset='id').sum()
```




    0



We can see that the data is relatively clean with no apparent null entries, and apparently free of duplicate entries. We can now check what each entry of the data looks like.


```python
# Preview first few rows of data
data.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cuisine</th>
      <th>id</th>
      <th>ingredients</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>greek</td>
      <td>10259</td>
      <td>[romaine lettuce, black olives, grape tomatoes...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>southern_us</td>
      <td>25693</td>
      <td>[plain flour, ground pepper, salt, tomatoes, g...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>filipino</td>
      <td>20130</td>
      <td>[eggs, pepper, salt, mayonaise, cooking oil, g...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>indian</td>
      <td>22213</td>
      <td>[water, vegetable oil, wheat, salt]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>indian</td>
      <td>13162</td>
      <td>[black pepper, shallots, cornflour, cayenne pe...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>jamaican</td>
      <td>6602</td>
      <td>[plain flour, sugar, butter, eggs, fresh ginge...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>spanish</td>
      <td>42779</td>
      <td>[olive oil, salt, medium shrimp, pepper, garli...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>italian</td>
      <td>3735</td>
      <td>[sugar, pistachio nuts, white almond bark, flo...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>mexican</td>
      <td>16903</td>
      <td>[olive oil, purple onion, fresh pineapple, por...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>italian</td>
      <td>12734</td>
      <td>[chopped tomatoes, fresh basil, garlic, extra-...</td>
    </tr>
  </tbody>
</table>
</div>



There are three columns presented above:

**cuisine** - indicates the category of cuisine for a particular recipe  
**id** - unique recipe ID number  
**ingredients** - contains a list of ingredients for the respective entry  

The main columns of interest here are the cuisine and ingredients categories. To begin, we should inspect the contents of each. Below is a list of all cuisine categories that appear in the dataset.


```python
# 
```

    Cuisine Categories in the dataset (by occurence):
    italian         7838
    mexican         6438
    southern_us     4320
    indian          3003
    chinese         2673
    french          2646
    cajun_creole    1546
    thai            1539
    japanese        1423
    greek           1175
    spanish          989
    korean           830
    vietnamese       825
    moroccan         821
    british          804
    filipino         755
    irish            667
    jamaican         526
    russian          489
    brazilian        467
    Name: cuisine, dtype: int64
    
    There are 20 cuisine categories represented in this dataset.
    


![png](output_8_1.png)


We can see that some categories, such as Italian and Mexican Cuisines occupy much larger fractions of the data, but overall there aren't any cuisines with overly small amounts of recipes represented here.

Next we will take a look at the ingredient details. First, we will look at the statistics of overall length of the ingredients list for each entry.


```python
# 
```

    count    39774.000000
    mean        10.767713
    std          4.428978
    min          1.000000
    25%          8.000000
    50%         10.000000
    75%         13.000000
    max         65.000000
    dtype: float64
    
     Median Value: 10.0
    


![png](output_10_1.png)


There is quite a large variation in the number of ingredients per recipe, with a maximum of 65 in this dataset. The average tends to be about 10 ingredients per recipe. Surprisingly, there are recipes with only 1 ingredient! We can see the ingredients for these below.


```python
# 
```

    japanese ['sushi rice']
    vietnamese ['dried rice noodles']
    indian ['plain low-fat yogurt']
    indian ['unsalted butter']
    japanese ['udon']
    thai ['sticky rice']
    indian ['butter']
    mexican ['corn tortillas']
    thai ['grained']
    southern_us ['lemonade concentrate']
    thai ['jasmine rice']
    indian ['unsalted butter']
    italian ['cherry tomatoes']
    french ['butter']
    indian ['cumin seed']
    french ['haricots verts']
    mexican ['vegetable oil']
    spanish ['spanish chorizo']
    spanish ['sweetened condensed milk']
    japanese ['water']
    greek ['phyllo']
    indian ['unsalted butter']
    

Now we can look at some more details of the ingredients we are working with. We will look at the total list of all ingredients in the data.


```python
# 
```

    Number of unique ingredients in the dataset: 6714
    Number of total ingredients in the dataset: 428275
    
    Ingredients ranked by occurence in the data:
    salt                                          18049
    onions                                         7972
    olive oil                                      7972
    water                                          7457
    garlic                                         7380
    sugar                                          6434
    garlic cloves                                  6237
    butter                                         4848
    ground black pepper                            4785
    all-purpose flour                              4632
    pepper                                         4438
    vegetable oil                                  4385
    eggs                                           3388
    soy sauce                                      3296
    kosher salt                                    3113
    green onions                                   3078
    tomatoes                                       3058
    large eggs                                     2948
    carrots                                        2814
    unsalted butter                                2782
    ground cumin                                   2747
    extra-virgin olive oil                         2747
    black pepper                                   2627
    milk                                           2263
    chili powder                                   2036
    oil                                            1970
    red bell pepper                                1939
    purple onion                                   1896
    scallions                                      1891
    grated parmesan cheese                         1886
                                                  ...  
    lamb rib roast                                    1
    bird pepper                                       1
    tuna, drain and flake                             1
    JonshonvilleÂ® Cajun Style Chicken Sausage        1
    frozen sweetened raspberries                      1
    BACARDIÂ® Superior                                1
    angled loofah                                     1
    dried pineapple                                   1
    semisweet vegan chocolate chips                   1
    peppermint schnapps                               1
    rock cornish game hens                            1
    boneless skinless chicken thigh fillets           1
    sliced mango                                      1
    garlic olive oil                                  1
    cubed mango                                       1
    San Marzano Diced Tomatoes                        1
    japanese style bread crumbs                       1
    fat-trimmed beef flank steak                      1
    puff pastry cups                                  1
    arepa flour                                       1
    fresno pepper                                     1
    shredded low-fat cheddar                          1
    jumbo shell pasta , cook and drain                1
    bean curd stick                                   1
    wasabe                                            1
    sweet chorizo                                     1
    A Taste of Thai Rice Noodles                      1
    butter flavor shortening                          1
    diced mushrooms                                   1
    italian style rolls                               1
    Length: 6714, dtype: int64
    


```python
# 
```


![png](output_15_0.png)


We can see that while salt is almost ubiquitous, less than half of our ingredients show up more than a few times each. This will need to be addressed, since it may make building a predictive model very difficult. One reason for this is that many similar ingredients have many variants, as is shown below for ingredients containing "Turkey".


```python
#
```

    turkey breast steaks: 1
    turkey salami: 1
    turkey ham: 1
    sliced turkey: 6
    lean ground turkey: 26
    rich turkey stock: 1
    hot italian turkey sausage: 2
    boneless turkey breast: 3
    ground turkey sausage: 1
    turkey tenderloins: 11
    smoked turkey breast: 5
    turkey carcass: 2
    turkey burger: 1
    low fat mild Italian turkey sausage: 1
    Italian turkey sausage: 54
    turkey sausage links: 3
    turkey meatballs: 1
    turkey kielbasa: 18
    turkey gravy: 1
    sweet turkey sausage: 1
    whole turkey: 1
    turkey giblet stock: 1
    turkey thigh: 2
    ground turkey breast: 39
    smoked turkey: 16
    ground turkey: 168
    cooked turkey: 48
    Italian turkey sausage links: 2
    turkey breast deli meat: 2
    roast turkey: 10
    turkey: 62
    dark turkey meat: 1
    turkey sausage: 15
    turkey hot dogs: 1
    smoked turkey drumstick: 1
    turkey breast tenderloins: 2
    fat free ground turkey breast: 1
    turkey mince: 1
    turkey legs: 9
    seasoned ground turkey: 1
    low-fat turkey kielbasa: 1
    turkey stock: 9
    turkey bacon: 12
    boneless skinless turkey breasts: 1
    turkey breast cutlets: 10
    hot italian turkey sausage links: 4
    turkey broth: 6
    smoked turkey sausage: 13
    turkey breast: 25
    turkey breakfast sausage: 4
    turkey meat: 15
    andouille turkey sausages: 2
    skinless boneless turkey breast halves: 1
    Number of Turkey variations: 53
    Total times ingredients with Turkey were used: 626
    

We can see that although turkey appears more than 600 times in the dataset, there are over 50 variants of turkey in the ingredient set, and most are only present a few times. In addition, we cannot simply set all variants to be labeled as "Turkey" since some, such as turkey stock are only flavorings and do not include any of the original turkey meat.

In order to deal with these variants, several (or many) steps will need to be taken.

### 2.2. Dealing with outliers (the messy part)

The next section will be a bit messy with many iterations in place to converge on a final set of ingredients. Hopefully my explanations will make a clear throughline to follow.

* First, I will take each ingredient from our ingredient_rankings (which is an ordered form of our unique ingredients set) and extract only the nouns. This means that 'chopped ingredient', 'fresh ingredient', 'baked ingredient' etc. will be converted to 'ingredient'.

* Next, I take only the singular form of each ingredient, so that there aren't unnecessary duplicates (e.g. 'onions' and 'onion')

Note: some words don't play nicely with NLTK's database of vocabulary (such as 'garlic', which tends to be classified as an adjective. e.g. 'garlic cloves' is simplified as 'clove') so I will include two lists of words for this process that will be updated throughout this section. They are **'words_to_exclude'** for words I do not want in my final list, and **'words_to_include'** for words that I do not want filtered out.

* Next, there are some ingredients in our dataset are either misspelled or incomplete in some way (e.g. 'any', 'extra', 'asian') we can deal with misspellings later, but first, we should make sure that some of the words that are falling through the cracks do not, such as 'flour', 'couscous', 'pudding', etc.

After these processing steps, the data has been transformed to what is shown below:


```python
# 
```

          original ingredients     simplified
    0                     salt           salt
    1                   onions          onion
    2                olive oil      olive oil
    3                    water          water
    4                   garlic         garlic
    5                    sugar          sugar
    6            garlic cloves   garlic clove
    7                   butter         butter
    8      ground black pepper         pepper
    9        all-purpose flour          flour
    10                  pepper         pepper
    11           vegetable oil  vegetable oil
    12                    eggs            egg
    13               soy sauce      soy sauce
    14             kosher salt           salt
    15            green onions          onion
    16                tomatoes         tomato
    17              large eggs            egg
    18                 carrots         carrot
    19         unsalted butter         butter
    20            ground cumin          cumin
    21  extra-virgin olive oil      olive oil
    22            black pepper         pepper
    23                    milk           milk
    24            chili powder   chili powder
    25                     oil            oil
    26         red bell pepper    bell pepper
    27            purple onion          onion
    28               scallions       scallion
    29  grated parmesan cheese         cheese
    
    After 1st Step: Unique ingredients reduced from 6714 to 4446
    

Ok! So after these processing steps we've dropped about 2,200 ingredients (1/3 of our original set!), but there is still a long way to go. 

* Next, we check to see if there are any spelling errors causing variations in our ingredient set.

For this step, we have several sources of misspelled words. There are words originating from other languages such as *'edamame'* and *'arborio'*.

We also have some words that are brand-related, such as *'lipton'*, *'smithfield'* and *'knorr'*.

Finally, in addition to the normal misspellings (e.g. *cheesi* instead of cheese or cheesy) there are many misspelling entries that have special characters, such as *'johnsonvilleâ®'* and *'crã¨me fraã®che'*. These are the easiest to deal with since we can simply remove all words that are not strictly composed of alphabetic characters.

The following steps were taken to deal with misspelled words: 

1. the words with non-alphabetic characters have been removed
2. remove the brand-related words by adding them into the 'words_to_exclude' list
3. check the misspelled words left, along with their frequency in the list of ingredients

The number of misspelled ingredients remaining are shown below:


```python
# 
```

    Number of total misspellings occuring in simple_ingredients4: 701
    misspell_errors list exported to .txt file!
    

There are a lot of entries in the misspelled ingredients. This presents a dilemma, since it's too long to go through by hand, and the strange nature of of many of the words not being strictly English makes them difficult to be interpreted correctly by a local spell-checker. No worries, Google's spell checker to the rescue! The workflow for this step is going to require some manual labor (until I find a way to do this within the script). The steps are as follows:

1. Export the list of misspellings to a txt file (completed above)
2. Import the list into a google doc manually
3. Use google doc spell checker to quickly run through and make corrections where possible
4. Export google doc as .txt file in the data folder ('data/misspells_corrected.txt')
5. Import .txt file into list and create a dictionary of misspelled words to corrected versions for quick replacement

Using Google's spell check, I was able to complete these steps in less than 5 minutes total, which is in my opinion an superb return on time efficiency for around 700 entries in multiple languages. Now we can replace the misspelled entries with the corrected versions using the dictionary that has been built.

Now that we have run through quite a few of our options in removing errors and combining ingredients via several methods, we see that we still have about 4,000 ingredients in our list (60% of our original ingredients!). But which of these are useful to our analysis? Next I remove outliers in the dataset for ingredients that only appear a few times within the ~40k recipes.


```python
print('Number of unique ingredients in simplified dataset: {0}'.format(len(set(total_ingredients))))
print('Number of unique ingredient words: {0}'.format(len(set(total_words))))
```

    Number of unique ingredients in simplified dataset: 4068
    Number of unique ingredient words: 2081
    

Although we still have about 4,000 ingredients in our dataset, we can see that only 2,000 ingredient words appear in the data. Additionally, we can compare the distribution of ingredients before and after our processing of the data.


```python
# 
```


![png](output_26_0.png)



```python
#
```

    Top 10 most common original ingredients:
    salt                   18049
    onions                  7972
    olive oil               7972
    water                   7457
    garlic                  7380
    sugar                   6434
    garlic cloves           6237
    butter                  4848
    ground black pepper     4785
    all-purpose flour       4632
    pepper                  4438
    vegetable oil           4385
    eggs                    3388
    soy sauce               3296
    kosher salt             3113
    green onions            3078
    tomatoes                3058
    large eggs              2948
    carrots                 2814
    unsalted butter         2782
    dtype: int64
    
    Top 20 most common ingredients (simplified):
    salt             21122
    pepper           17106
    onion            16700
    olive oil        10625
    garlic            9451
    water             8716
    sugar             8629
    butter            7927
    egg               7186
    garlic clove      7076
    flour             6902
    tomato            6477
    ginger            4680
    soy sauce         4470
    vegetable oil     4385
    milk              4029
    cheese            3939
    cumin             3678
    bell pepper       3505
    carrot            3126
    dtype: int64
    


```python
print('Number of ingredients that appear more than 40 times (0.1% of entries in data): {0}'.format(simple_ingredient_rankings[simple_ingredient_rankings > 40].shape[0]))
print('Number of words that appear more than 40 times (0.1% of entries in data): {0}'.format(word_rankings[word_rankings > 40].shape[0]))
```

    Number of ingredients that appear more than 40 times (0.1% of entries in data): 733
    Number of words that appear more than 40 times (0.1% of entries in data): 610
    

Now that the ingredients have been simplified and consolidated, we can see that the number of ingredients that appear in more than 0.1% of data entries (40 times) is about 700, while the number of words that appear above the same threshold is about 600. We can now move to creating a dataset that holds only these ingredients for export.

This dataset will be what is used for exploration and analysis, and has the following 4 columns:

**id** - the unique identification number for each recipe  
**cuisine** - the category label of the recipe cuisine  
**ingredients** - a simplified list of ingredients, processed by the steps above (with outliers removed)  
**words** - a list of unique words that appear in the ingredients list (with outliers removed)  

Additionally, since come of the ingredients lists may have been emptied if they only contained non-noun words or symbols, we must removed these rows before exporting our dataset.


```python
# 
```

    Number of rows dropped from dataset: 17
    

Only 17 rows needed to be removed from the dataset, and now it is ready for export. The new dataset will be exported as **data_clean.pkl** to the data folder.


```python
# Set the index of the dataset to be the 'id' column of the dataframe
data_clean = data_clean.set_index('id')
data_clean.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 39757 entries, 10259 to 2362
    Data columns (total 3 columns):
    cuisine        39757 non-null object
    ingredients    39757 non-null object
    words          39757 non-null object
    dtypes: object(3)
    memory usage: 1.2+ MB
    

## 3. Data Exploration <a class="anchor" id="EDA"></a>


```python
# Load the cleaned dataset from the data folder
data = pd.read_pickle('data/data_clean.pkl')

# Preview the first few rows
data.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cuisine</th>
      <th>ingredients</th>
      <th>words</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10259</th>
      <td>greek</td>
      <td>[feta cheese crumbles, olive, grape tomato, on...</td>
      <td>[pepper, crumbles, olive, lettuce, tomato, rom...</td>
    </tr>
    <tr>
      <th>25693</th>
      <td>southern_us</td>
      <td>[corn meal, milk, thyme, flour, salt, tomato, ...</td>
      <td>[meal, milk, thyme, vegetable, flour, salt, to...</td>
    </tr>
    <tr>
      <th>20130</th>
      <td>filipino</td>
      <td>[garlic powder, salt, cooking oil, onion, chic...</td>
      <td>[mayonnaise, powder, soy, salt, onion, chicken...</td>
    </tr>
    <tr>
      <th>22213</th>
      <td>indian</td>
      <td>[water, salt, vegetable oil]</td>
      <td>[wheat, vegetable, salt, water, oil]</td>
    </tr>
    <tr>
      <th>13162</th>
      <td>indian</td>
      <td>[milk, bay leaf, shallot, chili powder, garlic...</td>
      <td>[leaf, masala, onion, garam, cayenne, yogurt, ...</td>
    </tr>
  </tbody>
</table>
</div>



The **ingredients** column provides a list of ingredients, while the **words** column provides us with a unique set of words found in each respective ingredients list. We will use both columns for analysis.

### 1. What are the most frequently used ingredients in each cuisine?

We can get an idea of the ingredients used in each cuisine by splitting ingredients and words by categories.


```python
cuisines[1].head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cuisine</th>
      <th>ingredients</th>
      <th>words</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16903</th>
      <td>mexican</td>
      <td>[pepper, jalapeno pepper, corn tortilla, salt,...</td>
      <td>[cilantro, tortilla, fresh, poblano, olive, ch...</td>
    </tr>
    <tr>
      <th>41995</th>
      <td>mexican</td>
      <td>[cilantro, coriander, chili powder, cinnamon, ...</td>
      <td>[cilantro, powder, coriander, flank, olive, ch...</td>
    </tr>
    <tr>
      <th>40523</th>
      <td>mexican</td>
      <td>[cilantro, salt, rom tomato, lime, onion, jala...</td>
      <td>[cilantro, pepper, salt, tomato, lime, onion, ...</td>
    </tr>
    <tr>
      <th>1299</th>
      <td>mexican</td>
      <td>[cheese, flour tortilla, egg]</td>
      <td>[tortilla, flour, sausage, cheese, egg]</td>
    </tr>
    <tr>
      <th>10276</th>
      <td>mexican</td>
      <td>[garlic powder, chili powder, sea salt, cumin,...</td>
      <td>[powder, sea, chili, salt, cumin, onion, papri...</td>
    </tr>
  </tbody>
</table>
</div>



We will use a collection of wordclouds since: 1) They are a pretty good way to visualize the most common ingredients found in any subset of our data, and 2) They are really fun.

Below is a preview of the collection of wordclouds generated from their respective ingredients lists.


```python
# 
```


![png](output_40_0.png)



```python
#
```


![png](output_41_0.png)



![png](output_41_1.png)



![png](output_41_2.png)



![png](output_41_3.png)



![png](output_41_4.png)



![png](output_41_5.png)



![png](output_41_6.png)



![png](output_41_7.png)



![png](output_41_8.png)



![png](output_41_9.png)



![png](output_41_10.png)



![png](output_41_11.png)



![png](output_41_12.png)



![png](output_41_13.png)



![png](output_41_14.png)



![png](output_41_15.png)



![png](output_41_16.png)



![png](output_41_17.png)



![png](output_41_18.png)



![png](output_41_19.png)


There are a few things we can see by looking briefly through the wordclouds above. Firstly, ingredients like salt and onions seem to be ubiquitous, represented in every cuisine of our dataset. Alternatively, there are some clearly unique ingredients widely used in some cuisines, such as cumin in Mexican recipes. These standouts may definitely help us to build a model of cuisine prediction later on, if they can be weighted more importantly than those which appear in all cuisines.

We can also see rankings of the average lengths of ingredients lists for each cuisine to get an idea of which cuisines enjoy more complex dishes than others.


```python
#
```


![png](output_43_0.png)


It looks like cuisines like Moroccan, Indian and Thai use the most ingredients per recipe, while British, Irish and Brazilian cuisines have slightly simpler recipe lists.

It may also be useful to see which cuisines use the widest variety of ingredients to get an idea of the breadth of ingredients or flavors that make up each cuisine.


```python
#
```


![png](output_45_0.png)


We can see that although Moroccan, Indian and Thai lead with the most ingredients per recipe, the kitchens of Mexican, Italian and Southern U.S. cuisines are stocked with a larger variety of ingredients in our dataset. In all cases, Brazilian cuisine tends to be a simpler affair.


### Preparing data for Vectorization (TF-IDF weighted Processing)

While the visualizations above are nice, ubiquitous ingredients such as onion, salt, and garlic tend to obscure the ingredients unique to each cuisine. In order to account for this distribution and extract the ingredients that form a "signature" of each cuisine, we will use TF-IDF weighting which will give higher importanct to words which mainly appear in their respective category, and not across many cuisines.

Before we can proceed to apply this weighting to our cuisine ingredient lists, the ingredient lists for recipes of each cuisine will be normalized to be approximately the same length to adjust for cuisines that have a wide difference in the number of recipes represented. We will choose a random sample set of 20,000 ingredients for each cuisine for our analysis (the mean ingredients for all recipes is ~10, so this approximates about 2,000 recipes each).


```python
#
```


![png](output_47_0.png)


The plots above show us a much better representation of which ingredients form the unique signature of each cuisine. We can also use this grouping to see how similar cuisines are, as shown below.


```python
# 
```


![png](output_49_0.png)


Great! Although we've input nothing beyond labels and recipe ingredients, we can see that the visualization has naturally grouped together cuisines that are similar! Geography seems to play a role, since many Eastern and Western countries are grouped closely, and we can see the cuisines that best bridge the gap between these two, such as Filipino and Indian cuisines!

Now that we seem to have isolated the valuable data, we can return to our wordclouds and generate wordclouds that accurately depict the signature ingredients of each cuisine.


```python
#
```


![png](output_51_0.png)



![png](output_51_1.png)



![png](output_51_2.png)



![png](output_51_3.png)



![png](output_51_4.png)



![png](output_51_5.png)



![png](output_51_6.png)



![png](output_51_7.png)



![png](output_51_8.png)



![png](output_51_9.png)



![png](output_51_10.png)



![png](output_51_11.png)



![png](output_51_12.png)



![png](output_51_13.png)



![png](output_51_14.png)



![png](output_51_15.png)



![png](output_51_16.png)



![png](output_51_17.png)



![png](output_51_18.png)



![png](output_51_19.png)


### TF-IDF for each recipe

Now that we have looked at ingredients grouped together by their cuisine, we can perform a similar representation and visualization by processing each recipe individually into a TF-IDF weighted format.


```python
# 
```




    <39757x720 sparse matrix of type '<class 'numpy.float64'>'
    	with 267634 stored elements in Compressed Sparse Row format>



This time, instead of just projecting the data onto 2 dimensions, we will compress the data onto about 100 dimensions and then feed that into a t-SNE algorithm. This algorithm will plot the data onto a 2-dimensional space that we can try to use to visualize if cuisine recipes can be grouped together without explicit labelling.


```python
# 
```


![png](output_55_0.png)


We can see above that there are some nice groupings for most of the data above! The algorithm has done a good job representing each individual recipe with its associated cuisine. There is still room for improvement here though, since several of the cuisines with less entries such as British, Irish, Russian, etc. Are still quite spread out.

There are two corrections we can make to attempt to fix this. First, the distribution of recipes should be equalized, so that each cuisine is represented an approximately equal amount. Second, This model still includes ubiquitous ingredients such as Salt, Onion, Garlic, etc.! These entries should be excluded, similar to the previous work that was done during building of the tf-idf model. Making these corrections are likely to improve the groupings of recipes performed by t-SNE.

## 4. Initial Findings <a class="anchor" id="Findings"></a>

In this project the Yummly recipe dataset was investigated with a wide range of metrics to explore and analyze the attributes of various cuisines. The ingredients that make up a cuisines "signature" were identified for each cuisine, exposing what makes the flavors of each cuisine unique.

Overall, the analysis showed that the make up of cuisines is also related, in part, to geography. Cuisines from Eastern countries such as China, Korea, and Japan were shown to share a relatively common makeup of ingredients, while Western-based cuisines such as French, Irish and British were also similar. This analysis was also able to extract some information for cuisines that are mixed, which could be an indicator of their origins, such as is seen in Filipino cuisines, which were shown to fall somewhere in between Eastern and Western cuisines. This is not without base, since the Phillipines, while geographically located near the Eastern countries, was long colonized and controlled by the Spanish ([see this link for further information](https://en.wikipedia.org/wiki/History_of_the_Philippines_(1521%E2%80%931898)). Viewed from this perspective, deeper results from this dataset have the potential to yield "genomic" data of cuisines, tracing their origins and history.

## 5. Classification Models <a class="anchor" id="Models"></a>

Now that the data has been explored visually from several different angles, the next step will be to build a model in attempts to predict the cuisine of a recipe given its ingredients. The TF-IDF feature representation of ingredients will be used as the base input for predictive models. The problem is a multinomial classification problem, with 20 cuisine classes being considered.

Several models will be implemented and compared, with current candidates including K-nearest neighbors, multinomial Naive Bayes, Random Forests and Logistic Regression. The models will be compared primarily by classification accuracy, but precision and recall metrics will also be taken into account.

## 6. Resources <a class="anchor" id="Resources"></a>

* Dataset - [Kaggle's "What's Cooking?" Competition Site](https://www.kaggle.com/c/whats-cooking/data)
* Project Proposal - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%202/Project%20Proposal%20-%20Cuisines.md)
* Code (IPython Notebooks):
    * Data Cleaning - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%202/Data%20Wrangling%20-%20Cuisines.ipynb)
    * Data Exploration - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%202/EDA%20-%20Cuisines.ipynb)
