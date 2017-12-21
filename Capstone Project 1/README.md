
# Understanding Factors in Animal Shelter Adoption

### Table of Contents:
1. [Introduction](#Introduction)
2. [Data Acquisition/Cleaning](#Data)
3. [Data Exploration](#EDA)
4. [Data Exploration Findings](#Findings)
5. [Binomial Classification Models](#Binomial_Models)
    1. [Logistic Regression](#Log_Regression)
    2. [Random Forest](#RF)
6. [Multinomial Classification Models](#Multinomial_Models)
    1. [Logistic Regression](#Log_Regression2)
    2. [Random Forest](#RF2)
7. [Conclusions and Next Steps](#Conclusions)
8. [Additional Resources](#Resources)

## 1. Introduction <a class="anchor" id="Introduction"></a>

In efforts to understand trends in pet adoption outcomes, the Austin Animal Center has provided data relating to the pets in their adoption center. Austin, Texas is [America's largest "No Kill" city](https://www.huffingtonpost.com/kristen-auerbach/how-austin-became-americas-largest-no-kill-city_b_8482294.html), which means that animal shelters have devoted a large volume of time, resources and care to saving the lives of more homeless animals. This makes understanding trends of outcomes at Austin shelters a unique case study that can provide valuable insights into the underlying trends in animal adoptions.

#### Objectives

In this project, I will explore data from the Austin Animal Center in efforts to address two main questions:

1. **What are the most important factors that influence whether or not a pet finds a home in this area?** 
2. **How accurately can a predictive model identify pets that are likely to have difficulties being placed in a permanent home?**

I will explore factors related to 5 major outcome types reported by the Austin Animal Center, which include:

* Adoption  
* Returned to Owner
* Euthanasia
* Death
* Transfer

In addition, I will also consider factors for two groupings of these categories that more generally indicate whether or not animals were placed in a permanent home at the time that they left the shelter by grouping those that were either adopted or returned to their owners.

#### Client

The client for this project would be the Austin Animal Center in Austin, TX.  Efforts to increase the efficiency of the center and a better understanding of the factors that contribute to successfully finding homes for pets could allow them to more effectively allocate resources and serve more pets. If a model can be built from pet adoption data that outlines the most important factors relating to successful adoption, the insights we gain can be used to generate suggestions for actions that could potentially improve the chances of adoption for some pets. Some of these actions might include:  

1. Early transfer for pets that typically don’t typically get exposure at the center we are investigating  
2. Better selection of pets to prioritize for fostering  

#### Broader Impact

Beyond the direct potential to create valuable insights and actionable recommendations to improve the performance of the Austin Animal Center, the results of this project can serve a wider community of animal shelters in a number of ways. First, it can serve as a general baseline for other shelters to see which factors influence animal adoptions as well as the steps that this shelter has taken in order to successfully implement and maintain its No Kill status. Secondarily, if similar data can be acquired and provided, the framework of this project can be applied to other shelters to quickly assess and compare performance. This can significantly reduce the initial barrier to entry for shelters looking to gain insights and visualizations from their own data.

## 2. Data Acquisition/Cleaning  <a class="anchor" id="Data"></a>

In this section I will be exploring the dataset and using various data wrangling techniques to prepare the data via basic data wrangling techniques in order to prepare the data for analysis. This will include the following steps:

   1. Loading the data and extracting general info and structure
   2. Verifying that data is tidy
   3. Identifying & dealing with missing values
   4. Identifying & dealinig with outliers

#### 2.1. Data Information and Structure

The dataset I am working with can be found on the City of Austin Open Data Portal **[here](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)**

**Note:** This dataset is updated hourly, and was accessed on Sunday, December 12th 2017 at 19:00 UTC for this project.


    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 76133 entries, 0 to 76132
    Data columns (total 12 columns):
    Animal ID           76133 non-null object
    Name                52741 non-null object
    DateTime            76133 non-null object
    MonthYear           76133 non-null object
    Date of Birth       76133 non-null object
    Outcome Type        76123 non-null object
    Outcome Subtype     35280 non-null object
    Animal Type         76133 non-null object
    Sex upon Outcome    76131 non-null object
    Age upon Outcome    76123 non-null object
    Breed               76133 non-null object
    Color               76133 non-null object
    dtypes: object(12)
    memory usage: 7.0+ MB
    

There are a few details to mention here. Firstly we can see that within our 12 columns, there seem to be some missing entries in several of the columns, which may need to be addressed later on. In addition, all of the row types are classified as 'object', which can most likely be handled more efficiently if we are able to parse out specific types such as the 'DateTime' column. This column can be handled with much more functionality if we are able to convert it to a Datetime object in our dataframe.

In order to get more information, we will preview the first few rows of the data.





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Animal ID</th>
      <th>Name</th>
      <th>DateTime</th>
      <th>MonthYear</th>
      <th>Date of Birth</th>
      <th>Outcome Type</th>
      <th>Outcome Subtype</th>
      <th>Animal Type</th>
      <th>Sex upon Outcome</th>
      <th>Age upon Outcome</th>
      <th>Breed</th>
      <th>Color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A741715</td>
      <td>*Pebbles</td>
      <td>01/11/2017 06:17:00 PM</td>
      <td>01/11/2017 06:17:00 PM</td>
      <td>03/07/2016</td>
      <td>Adoption</td>
      <td>NaN</td>
      <td>Cat</td>
      <td>Spayed Female</td>
      <td>10 months</td>
      <td>Domestic Shorthair Mix</td>
      <td>Calico</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A658751</td>
      <td>Benji</td>
      <td>11/13/2016 01:38:00 PM</td>
      <td>11/13/2016 01:38:00 PM</td>
      <td>07/14/2011</td>
      <td>Return to Owner</td>
      <td>NaN</td>
      <td>Dog</td>
      <td>Neutered Male</td>
      <td>5 years</td>
      <td>Border Terrier Mix</td>
      <td>Tan</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A721285</td>
      <td>NaN</td>
      <td>02/24/2016 02:42:00 PM</td>
      <td>02/24/2016 02:42:00 PM</td>
      <td>02/24/2014</td>
      <td>Euthanasia</td>
      <td>Suffering</td>
      <td>Other</td>
      <td>Unknown</td>
      <td>2 years</td>
      <td>Raccoon Mix</td>
      <td>Black/Gray</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A746650</td>
      <td>Rose</td>
      <td>04/07/2017 11:58:00 AM</td>
      <td>04/07/2017 11:58:00 AM</td>
      <td>04/06/2016</td>
      <td>Return to Owner</td>
      <td>NaN</td>
      <td>Dog</td>
      <td>Intact Female</td>
      <td>1 year</td>
      <td>Labrador Retriever/Jack Russell Terrier</td>
      <td>Yellow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A750122</td>
      <td>Happy Camper</td>
      <td>05/24/2017 06:36:00 PM</td>
      <td>05/24/2017 06:36:00 PM</td>
      <td>04/08/2017</td>
      <td>Transfer</td>
      <td>Partner</td>
      <td>Dog</td>
      <td>Intact Male</td>
      <td>1 month</td>
      <td>Labrador Retriever Mix</td>
      <td>Black</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A756696</td>
      <td>Shakti</td>
      <td>09/01/2017 11:23:00 AM</td>
      <td>09/01/2017 11:23:00 AM</td>
      <td>08/24/2014</td>
      <td>Return to Owner</td>
      <td>NaN</td>
      <td>Cat</td>
      <td>Spayed Female</td>
      <td>3 years</td>
      <td>Domestic Shorthair Mix</td>
      <td>Blue/White</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A684346</td>
      <td>NaN</td>
      <td>07/22/2014 04:04:00 PM</td>
      <td>07/22/2014 04:04:00 PM</td>
      <td>07/07/2014</td>
      <td>Transfer</td>
      <td>Partner</td>
      <td>Cat</td>
      <td>Intact Male</td>
      <td>2 weeks</td>
      <td>Domestic Shorthair Mix</td>
      <td>Orange Tabby</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A666430</td>
      <td>Lucy</td>
      <td>11/07/2013 11:47:00 AM</td>
      <td>11/07/2013 11:47:00 AM</td>
      <td>11/06/2012</td>
      <td>Transfer</td>
      <td>Partner</td>
      <td>Dog</td>
      <td>Spayed Female</td>
      <td>1 year</td>
      <td>Beagle Mix</td>
      <td>White/Brown</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A675708</td>
      <td>*Johnny</td>
      <td>06/03/2014 02:20:00 PM</td>
      <td>06/03/2014 02:20:00 PM</td>
      <td>03/31/2013</td>
      <td>Adoption</td>
      <td>NaN</td>
      <td>Dog</td>
      <td>Neutered Male</td>
      <td>1 year</td>
      <td>Pit Bull</td>
      <td>Blue/White</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A680386</td>
      <td>Monday</td>
      <td>06/15/2014 03:50:00 PM</td>
      <td>06/15/2014 03:50:00 PM</td>
      <td>06/02/2005</td>
      <td>Transfer</td>
      <td>Partner</td>
      <td>Dog</td>
      <td>Neutered Male</td>
      <td>9 years</td>
      <td>Miniature Schnauzer Mix</td>
      <td>White</td>
    </tr>
  </tbody>
</table>
</div>



This table gives a much better look at what is going on in the data. Starting from the leftmost column are the following observations:

   1. **Animal ID** - This is a unique identifier for each entry that is a letter combined with a number. This seems well-formatted.
     
   2. **Name** - Some entries are missing here, and there are also some entries with asterisks before the names (e.g. \*Pebbles, \*Johnny). It will be useful if we can find out the meaning of the asterisk in this field.  
     
   3. **DateTime** and **MonthYear** - These columns look like datetime objects, but they look identical for the entries we see. If we verify that the columns are identical, we may be better served removing one.
     
   4. **Date of Birth** - This year may also be converted into a datetime object, so that we can perform time-series analysis with this information.
     
   5. **Outcome Type** - There are several categories in this column, and we may be able to convert the entries into categories for easier handling.
     
   6. **Outcome Subtype** - This has many missing entries, and we only see categories for Euthanasia and Transfer corresponding outcome types. Depending on the number of subtypes for these types, it may be more efficient to integrate them into the outcome type category.
     
   7. **Animal Type** - In addition to cats and dogs, there is an 'Other' category here in the third entry, corresponding to a 'Raccoon Mix' breed of animal. With the small amount of types of animals, this column is likely to perform better as categorical values.
     
   8. **Age upon Outcome** - If we are able to convert this into a uniform value (e.g. age in months) we can work with these values as numbers which will make analyzing this data easier. It should also be noted that if we work with the Outcome DateTime and Date of Birth columns as datetime objects, columns like this can be generated by arithmetic operations.
     
   9. **Breed** and **Color** - These columns look well-formatted, but more investigation is needed in order to determine whether they will perform better as categorical values, or what additional ways they can be transformed in order to yield more information.
   
#### 2.2. Data Cleaning

**i.** First the animal types were reduced to entries only containing cats and dogs, since they accounted for over 80% of the distribution of animals at the center and thus require the most resources to shelter and find homes.

**ii.** Next, for the 'Name' entries, I investigated those entries with and without asterisks. After contacting the custodians of this dataset, I recieved the following reply:

    "...ASO Staff are supposed to be using the asterisk when they name a pet at their review – after they come in.  
    If they came in with a name, then no asterisk."
    
Since the asterisks only denotes whether or not the name of the animal was given before they arrived at the shelter it is not a factor of interest for this analysis so were simply removed. The formatted names now appear without asterisks.

**iii.** Next up were the DateTime and MonthYear columns. Since these columns were proven to be identical, the MonthYear column was removed. The DateTime and Date of Birth columns were also converted to datetime objects.

**iv.** For the outcome types and subtypes columns, several steps were taken. Since the main investigation was into placement in permanent homes for animals, such as in adoption and transfers, other outcomes were considered undesirable. Euthanasia and Death entries were maintained as-is, but entries labeled as 'Missing' and the small number of entries for animals that were brought to the center for 'Disposal' were removed. Additionally, the 'Rto-Adopt' entries were combined with the Adoption class. This helps to significantly reduce the number of classes we are working with and thus improve the simplicity of the model. After refinement, the 'Outcome Type' column was converted into categorical value format.

**v.** Similarly, the 'Animal Type' and 'Sex upon Outcome' columns were converted into categorical features

**vi.** The Age upon Outcome column was converted into a timedelta object, since this format will allow for mathematical operations to be performed on it if needed.

**vii.** Next, the breed and color column categories were reduced significantly by selecting mixed breed entries of the format 'breed/breed' and replacing these entries with the first breed + 'Mix' (e.g. Chihuahua/Terrier => Chihuahua Mix). Similarly, colors of format 'color/color' were separated into 'Primary Color' and 'Secondary Color' entries. This process reduced the number of categories for breeds and colors to a manageable number for each.

    \# of unique breeds in the original dataset: 1948
    \# of mixed breeds classified by "breed/breed": 1551
    \# of unique breeds after replacement: 399
    
    # of unique colors in the original dataset: 491
    \# of mixed colors classified by "color/color": 435
    \# of unique primary colors after replacement: 57
    \# of unique secondary colors after replacement: 51

And finally the breed and color columns were converted into categorical features.

#### 2.3. Missing Values

Out of the 5 columns that contain missing entries, 'Outcome Subtype' and 'Secondary Color' have empty entries by necessity, since some outcome types do not have subclasses, and some animals do not have secondary colors. In addition, names may not be crucial to the other animal attributes, but it is crucial to keep records of animals with and without given names, since this fact may also influence the outcome type for that animal.

What is left are a handful of entries without outcome type, which is critical information that we are interested in, and without sex information. Since we are currently working with a dataset of more than 76,000 entries, these entries removed without any significant impact on the data.

#### 2.4. Outliers

Although many outliers were corrected with the previous formatting, one main column of interest that I explored for outlier values was 'Outcome Subtype'. The marginal subtypes (those with less than 100 instances each) were combined into an 'Other' Outcome Subtype category. After this was done, the outcome subtype column entries were converted into categorical features.

With these steps completed, the Austin Animal Center dataset was explored and prepared for analysis. By converting columns into their appropriate formatting, removing duplicate information, and correcting missing values/outliers where possible, the data can yield more information in analysis. This includes the dataset taking less space in memory to work more quickly, as well as having a richer set of data which we can probe.

## 3. Data Exploration <a class="anchor" id="EDA"></a>

### 3.1. How Likely are adoptions for Cats vs. Dogs?

It is very important to understand the general distributions of outcomes for cats and dogs, as well as the total number of each that the center recieves, in order to efficiently provide resources to shelter these animals. This section will break down the outcomes for both cats and dogs in order to gain more insight into the placement of these animals in permanent homes.



![png](images/fr_output_24_0.png)


We can see here that dogs are much more likely to have an outcome resulting in a permanent home than cats.

We can also break these outcomes down further by their specific outcome type:

<a class="anchor" id="skew"></a>

The skew of classes in the dataset is important to note, since it will need to be considered when evaluating our models in a [later section](#RF_eval).



![png](images/fr_output_26_0.png)


While numbers for adoption are similar for both cats and dogs, many more dogs are classified as 'Return to Owner' than cats, which denotes dogs that were lost and returned to their owners. A large majority of cats are transferred to other facilities, which may indicate that other facilities are either better equipped to handle the volume of cats, or simply that the real estate at the Austin Animal Center does not allow support for enough cats.

### 3.2. Analysis of Adoption Outcomes vs. Animal Attributes

In understanding the animal attributes that most affect the outcomes of animals at this center, we can identify which animals have a higher chance of being adopted for this area. This, in conjunction with data on neighboring or partner centers might allow for avenues to 'match' animals that can maximize their chance of adoption in each area.


#### i. Gender



![png](images/fr_output_28_0.png)



![png](images/fr_output_29_0.png)


The distribution of outcomes for male and females in the cases of both cats and dogs shows that there is not a strong preference for either gender. Naturally, since animals are spayed and neutered when possible at animal shelters, most adoptions occur for these types rather than intact gender animals.

#### ii. Age



![png](images/fr_output_31_0.png)


There seems to be a wide spread of ages for both cats and dogs, up to 22 years for cats and 20 years for dogs. Most of the animals are less than 4 years old in both cases. It would also be helpful to see the breakdown of outcomes for each of these age groups.



![png](images/fr_output_33_0.png)



![png](images/fr_output_34_0.png)




![png](images/fr_output_35_0.png)


As shown above, we can see that while all age groups have a higher frequency of dogs that are placed/returned to their homes, cats have a more complicated distribution. Both young (< 5 years old) and old (> 12 years old) seem to have mixed chances of being placed in a permanent home.

One interesting note is that in both cases, the oldest animals seem to have higher chances of adoption.

#### iii. Breed


    10 Most Common Cat Breeds
                          Cat Breed  # of Cats
    Rank                                     
    1       Domestic Shorthair Mix      22773
    2     Domestic Medium Hair Mix       2257
    3        Domestic Longhair Mix       1204
    4                  Siamese Mix        997
    5           Domestic Shorthair        378
    6       American Shorthair Mix        194
    7                 Snowshoe Mix        150
    8         Domestic Medium Hair        127
    9               Maine Coon Mix        103
    10                    Manx Mix         85
    
    Total Number of Distinct Cat Breeds: 55
    Fraction of Total Cats Occupied by 10 most common breeds: 98.53 %
    
    
    10 Most Common Dog Breeds
                           Dog Breed  # of Dogs
    Rank                                      
    1                  Pit Bull Mix       6283
    2        Labrador Retriever Mix       5628
    3       Chihuahua Shorthair Mix       5264
    4           German Shepherd Mix       2239
    5     Australian Cattle Dog Mix       1281
    6                 Dachshund Mix       1094
    7             Border Collie Mix        827
    8                     Boxer Mix        820
    9          Miniature Poodle Mix        743
    10                Catahoula Mix        581
    
    Total Number of Distinct Dog Breeds: 345
    Fraction of Total Dogs Occupied by 10 most common breeds: 57.78 %
    

In  both categories, we can see that mixed breeds are the most common. This is not surprising, though the distribution above shows that the breeds of dogs are much more varied than cats. The 10 most common breeds of dogs only account for about 58% of the total population of dogs that have gone through the center, but for cats the 10 most common breeds account for over 98% of the entries.



![png](images/fr_output_39_0.png)


In the plot shown above, we can see that Domestic Shorthair mixed breeds in cats account for almost 80% of the cat entries alone. All entries in the most common cat breeds are mixed, since 'Domestic Shorthair' and 'Domestic Medium Hair' breeds are themselves mixed breed classifications.

Next we can investigate the outcomes by breed:


    Cat Breeds with highest percentage of Homes Found
                            Breed  % of Breed that Found Home
    Rank                                                    
    1            Turkish Van Mix                       100.0
    2          British Shorthair                       100.0
    3              Devon Rex Mix                       100.0
    4            Cornish Rex Mix                       100.0
    5     Munchkin Shorthair Mix                       100.0
    6                 Ocicat Mix                       100.0
    7            Oriental Sh Mix                       100.0
    8           Havana Brown Mix                       100.0
    9                    Burmese                       100.0
    10    Pixiebob Shorthair Mix                       100.0
    
    Cat Breeds with lowest percentage of Homes Found
                              Breed  % of Breed that Found Home
    Rank                                                      
    1         Exotic Shorthair Mix                    0.000000
    2                         Manx                    0.000000
    3                    Devon Rex                    0.000000
    4                   Birman Mix                    0.000000
    5        Munchkin Longhair Mix                    0.000000
    6           Turkish Angora Mix                   25.000000
    7                    Himalayan                   33.333333
    8       American Shorthair Mix                   40.206186
    9       Domestic Shorthair Mix                   46.476090
    10    Domestic Medium Hair Mix                   48.958795
    

All of the cat breeds with the highest percentages of placement in permanent homes represent breeds that are somewhat exotic when compared to the population that can be found in Austin, TX. We can also see that the Domestic Shorthair Mix that dominates the cat population in this dataset has a fairly low rate of adoption with ~46%.


    Dog Breeds with highest percentage of Homes Found
                        Breed  % of Breed that Found Home
    Rank                                                
    1      Affenpinscher Mix                       100.0
    2        Norfolk Terrier                       100.0
    3               Boerboel                       100.0
    4       Mexican Hairless                       100.0
    5     Manchester Terrier                       100.0
    6      Bouv Flandres Mix                       100.0
    7          Silky Terrier                       100.0
    8            Lowchen Mix                       100.0
    9     Smooth Fox Terrier                       100.0
    10            Leonberger                       100.0
    
    Dog Breeds with lowest percentage of Homes Found
                              Breed  % of Breed that Found Home
    Rank                                                      
    1          Spanish Mastiff Mix                         0.0
    2                        Jindo                         0.0
    3                     Landseer                         0.0
    4                Japanese Chin                         0.0
    5             Irish Setter Mix                         0.0
    6            Dogue De Bordeaux                         0.0
    7              Entlebucher Mix                         0.0
    8              Sussex Span Mix                         0.0
    9                Bruss Griffon                         0.0
    10    Old English Sheepdog Mix                         0.0
    

The distribution for dogs similarly shows that exotic breeds seem to occupy many of the top ranking spots for adoption rates, although the wide variety of dog breeds also shows that there are many breeds that don't fare well. This might indicate that breed alone is not a good enough indication of the chances of adoption.



![png](images/fr_output_45_0.png)


We can see that there are two opposing trends for cats and dogs here. For cats, purebreeds have a noticeably higher rate of adoption, while dogs see a drop in adoption rates for those that are not mixed breeds. This may be related to the high occurences of Domestic Shorthair cats at the center. When people come in to browse for pet adoption, it is easier for purebreeds to stand out in appearance when most cats are similar. The distribution of breeds for dogs are much more varied, and so this may not have the same impact on adoptions for dogs.

#### iv. Colors



![png](images/fr_output_47_0.png)


Above are the 10 most common colors for both cats and dogs. If we investigate the rates of placement in permanent homes by color, it may be possible to extract information on which color animals are preferred by people looking for pets at the Austin Animal Center.


    Cat Colors with Highest percentage of Homes Found
             Primary Color  % of Color that Found Home
    Rank                                             
    1                Fawn                  100.000000
    2             Apricot                  100.000000
    3          Blue Smoke                   91.666667
    4              Agouti                   66.666667
    5        Tortie Point                   63.636364
    6         Black Smoke                   62.878788
    7     Chocolate Point                   61.016949
    8         Flame Point                   58.208955
    9           Chocolate                   57.692308
    10         Lynx Point                   55.230126
    
    Cat Colors with Lowest percentage of Homes Found
           Primary Color  % of Color that Found Home
    Rank                                           
    1          Tricolor                    0.000000
    2              Pink                    0.000000
    3     Black Brindle                    0.000000
    4      Orange Tiger                    0.000000
    5       Black Tiger                    0.000000
    6       Brown Merle                    0.000000
    7     Brown Brindle                    0.000000
    8              Buff                    9.090909
    9            Orange                   22.807018
    10       Gray Tabby                   25.603865
    

Now we can compare these rankings with those of the 10 most common cat colors that we saw earlier:


    Rankings of Colors Most Likely to Find Homes - for 10 Most Common Cat Colors
    Torbie: 11
    Calico: 15
    Cream Tabby: 16
    Blue Tabby: 17
    Blue: 22
    Tortie: 23
    Orange Tabby: 25
    Brown Tabby: 27
    White: 28
    Black: 29
    


    Dog Colors with Highest percentage of Homes Found
            Primary Color  % of Color that Found Home
    Rank                                            
    1             Agouti                  100.000000
    2              Ruddy                  100.000000
    3        Black Tiger                  100.000000
    4        Black Smoke                   92.307692
    5         Blue Tiger                   90.625000
    6     Yellow Brindle                   81.578947
    7         Blue Merle                   80.890052
    8             Silver                   80.373832
    9        Brown Merle                   80.368098
    10            Yellow                   78.360656
    
    Dog Colors with Lowest percentage of Homes Found
          Primary Color  % of Color that Found Home
    Rank                                          
    1      Brown Tiger                   60.000000
    2           Orange                   66.666667
    3       Blue Smoke                   66.666667
    4             Gold                   71.022727
    5       Liver Tick                   71.428571
    6       Blue Cream                   71.428571
    7            Cream                   71.698113
    8          Apricot                   71.875000
    9             Gray                   71.922246
    10            Fawn                   72.759857
    

Similarly, these rankings are now compared with those of the 10 most common dog colors:


    Rankings of Colors Most Likely to Find Homes - for 10 Most Common Dog Colors
    Chocolate: 14
    Tricolor: 15
    Blue: 17
    Red: 19
    Black: 20
    Brown Brindle: 21
    Tan: 22
    Sable: 24
    Brown: 25
    White: 26
    



![png](images/fr_output_55_0.png)


The respective ranks in highest adoption rates for cats and dogs are denoted above the bars for each of the 10 most common colors. We can see again that none of the most common colors for both cats and dogs appear in their respective top lists of adoption rates. This further supports that a sense of exotic appearance of a pet may be a primary driver in people's choice of a pet.



![png](images/fr_output_57_0.png)


The data above shows that for both cats and dogs, a secondary color slightly improves the rates of adoption. Animals with distinctive color combinations in their coats may stand out more visually to potential pet owners.

### 3.3. Analysis of Adoption Outcomes vs. Year

Finally, I will take a brief look at the trends of cat and dog adoptions by year. The dataset covers a time period between 2013-10-01 09:31:00 and 2017-12-10 12:59:00



![png](images/fr_output_60_0.png)


The graph above shows the average rates of placement in permanent homes for cats and dogs broken down by year. Although dogs have experienced a relative upward trend with time, cats seem to show a drop in rates from 2013 to 2014, but then the same relative upward trend. This may be an anomaly of our dataset, since we only have 2013 data for the months of October-December. If there is a dependence on adoptions vs. months of the year, this can introduce a bias into the 2013 data points.



![png](images/fr_output_62_0.png)


By looking at the average adoption rates broken down by month we can see that for both cats and dogs, there seems to be spikes in adoptions around winter months (Nov. - Feb.) and summer months (Jun. - Aug.). The main difference here is that cats seem to have a much stronger dependence on the month of the year than dogs, which remains relatively consistent.

This suggests that the average placement rate value for 2013 found in the previous graph may not be representative of the placement rates for the entire year due to the data only being collected in October-December.



![png](images/fr_output_64_0.png)


We can see that the variations in adoptions for cats is again much larger than that for dogs, which is relatively consistent. 

## 4. Data Exploration Findings <a class="anchor" id="Findings"></a>

In this project the Austin Animal Center dataset was investigated with a wide range of metrics to suggest which factors seem to influence the animals that are able to be placed in permanent homes vs. those which are not. It was shown that dogs have a much higher placement rate overall than cats, while attributes such as breed and color seem to have a strong influence on the placement rates for both cats and dogs.

Overall, there is a general sense that cats and dogs that have a visually distinctive look, such as purebred cats that do not have similar appearances to the domestic shorthair mix cats, or animals with distinctive coat colors or combinations or colors, seem to have an overall much better chance of being placed in permanent homes. One superficial suggestion that might be made would be to look at which cat breeds are most common across shelter (or better yet, geographical regions) and see if it is feasible for partner facilities to be matched up so that a wider distribution of different animals can have more exposure at each shelter.

In addition to the influence of the animal attributes themselves, over time it seems that the overall performance in placing animals in permanent homes for the Austin Animal Center is increasing, though more information or deeper analysis would be needed to find out the source of this improvement trend. One interesting finding was that there are times of year when people are more likely to adopt (during winter and summer months), and that the percentage of cats that find homes during these times are much more dependent on the time of year than those for dogs.

Now that the data has been explored visually from several different angles, the next step will be to build a model in attempts to predict the outcomes of animals based on their attributes and additional features of the data. Two predictive tasks will be addressed. The first is the general task of predicting whether or not an animal will find a home, denoted in the data's 'Found Home' feature that we have created as being Yes (1) or No (0). This will give us a baseline of predictive performance for animal outcomes. The second task will add more detail: the dependent variable of interest for this task will be the “outcome type” of the pet, which includes several classes, including: adoption, transfer, return to owner, death and euthanasia. The proposed model for both tasks fall within supervised learning problems, although the first task is a binomiall classification problem, while the second will require multinomial classification techniques due to the multiple outcome classes of the variable we are interested in.

## 5. Binomial Classification Models <a class="anchor" id="Binomial_Models"></a>

### 5.1 Logistic Regression (Home Found vs. No Home Found) <a class="anchor" id="Log_Regression"></a>

All of the data has been split into three subsets in order to build models. We will be using a training set to train the models; a CV, or cross-validation, set that will help us to test and optimize the model in order to increase performance where possible by fine tuning various parameters, and an independent test set which will only be used at the end to gauge the final performance of the models. The distribution is shown below:


    Number of training entries: 42921 -> 60% of data
    Number of CV entries: 14307 -> 20% of data
    Number of test entries: 14307 -> 20% of data
    

In order to use logistic regression on this dataset, I will begin by selecting a subset of the data. The data, which has been prepared [here](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%201/Classification%20Models%20-%20Pet%20Adoption.ipynb), contains 61 features after we formatted it to be fed into our classification models. It would not be efficient nor wise to use all 61 features, so we will instead use a subset of features that we can choose using a method called Best Subset Selection.

An example of this is shown below, where a best subset selection technique was applied to the data in order to approximate the top 5 predictive features in the data.





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Subset Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Intact Female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Intact Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Neutered Male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Spayed Female</td>
    </tr>
  </tbody>
</table>
</div>





![png](images/fr_output_74_0.png)


Here we can see a curve of the F1 score (which is a performance metric that will be described in greater detail later on in this report) vs. the number of features that we use for prediction in our best subset selection. We can see here that while we get pretty big increases in our score by increasing the number of features we use up to 5, after that the performance gains taper off. We will then use a subset of the 5 best features as selected by this calculation in order to get a good combination of predictive potential and relatively low complexity.



![png](images/fr_output_76_0.png)



![png](images/fr_output_76_1.png)


Confusion matrices, such as the one shown above, can give us a good visualization of the predictive performance of our model. We can see here that 90% of the animals that found permanent homes were categorized correctly, which is pretty good performance. This indicates a low rate of False Negatives, where we would predict that an animal did not find a home when in reality it did. On the other hand, our model has a fairly high occurence of False Positives, meaning that if we predicted that an animal would find a home, there is also a fairly large fraction of these animals that did not end up being placed in a home.

In order to tune the performance of our model, we can vary the threshold at which we predict that an animal will find a home. The default for the model that we used previously was 50%. This means that if an animal has a higher than 50% chance of finding a home as measured by our model, then our model will make a Yes prediction. The threshold can be raised or lowered for different results, as shown below.



![png](images/fr_output_78_0.png)


In order to give our model a single-number metric that we can use to gauge its performance, we will be using the F1 score, which is calculated as follows:  

    F1 = 2 * (precision * recall) / (precision + recall)  
    
where **precision** is the fraction of true positives divided by the total number of true positives and false positive fradulent values and **recall** represents the number of true positives divided by the number of true positives and false negative values.  

The graph above shows the ratio between precision and recall for all threshold values in the model. Although the F1 score gives us a standard baseline, in order to specialize the functionality of the trained model it is also good to consider whether it is important for the predictions to have either high precision, or high recall, since the graph above shows us that this is usually a trade-off.



![png](images/fr_output_80_0.png)


In the graph above, wew can see the F1 score as a function of the threshold we choose to predict "Home Found" for an animal.
  
This will give us guidance on the range in which we can set the threshold value to achieve the best standard combination of precision and recall. We will use the maximum value here and feed it back into our original model to see the change in performance.



![png](images/fr_output_82_0.png)


The performance is similar, though now there is a reduction in false negatives in our predictions. Now that the model has been optimized by both subset selection and by tuning the threshold for prediction, we can test the model performance on the test dataset.



![png](images/fr_output_84_0.png)


The confusion matrix above shows the model's performance on a test dataset. We can see that while the model captures almost all of the "Home Found" predictions, it still struggles to classify those animals that were not placed in permanent homes, with a fairly large proportion of false positives.

The next step we can try is to see how a different model can perform on the dataset.

### 5.2 Random Forest (Home Found vs. No Home Found)  <a class="anchor" id="RF"></a>



![png](images/fr_output_87_0.png)


Above we can see a very useful plot of the measured importance and ranking of each feature as measured by the 1000 samples we have taken in our random forest model gender seems to play a very important role, as does the 'Cat' feature, which simply indicates whether the animal was a cat (1) or a dog (0). Surprisingly, we see that the cat features "Domestic Shorthair" breed as well asa "Brown Tabby" color make the top list of most important features in our model.



![png](images/fr_output_89_0.png)



![png](images/fr_output_89_1.png)


Above are the normalized and non-normalized confusion matrices to see the performance of our model. The performance looks comparable to our logistic regression model, but now we will check it against the independent test set of data.



![png](images/fr_output_91_0.png)


We can see here that we have only a tiny increase in predictive accuracy on the test set for our random forest model when compared to our optimized logistic regression model. Rather than this indicating a limit to the model itself, it is much more likely that this is an indication that either the structure of our engineered features or our cost function that evaluates the model should be further improved.

Now that we have taken a look at the binomial classification models, we can turn the power of these models to see how well they can predict the specific outcome type of each animal in a multinomial classification setting.

## 6. Multinomial Classification Models <a class="anchor" id="Multinomial_Models"></a>

### 6.1 Logistic Regression (Outcome Type Prediction) <a class="anchor" id="Log_Regression2"></a>



![png](images/fr_output_95_0.png)


We will again use best subset selection for the logistic regression model. The subset features for the top 5 features are shown below. Note that the rankings of these features are different than those in the binomial classification model.





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Subset Features</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Age upon Outcome</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Intact Female</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Intact Male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Simple Breed_Domestic Shorthair</td>
    </tr>
  </tbody>
</table>
</div>





![png](images/fr_output_98_0.png)



![png](images/fr_output_98_1.png)


<a class="anchor" id="RF_eval"></a>
Above are expanded versions of the confusion matrices that were built in the previous sections with the 5 outcome types we are predicting. We can see here that while the model predicts well on the Adoption outcome, and relatively well on the Transfer outcome, for Death, Euthanasia and Return to Owner performance is notably lacking, even using our best subset. These categories have a much smaller distribution of entries, as we can see in reference to an [earlier visualization](#skew) that was made during exploration of the dataset. A different model input may need to be generated in order to better predict these small classes.



![png](images/fr_output_100_0.png)


### 6.2 Random Forest (Outcome Type Prediction)  <a class="anchor" id="RF2"></a>



![png](images/fr_output_102_0.png)




![png](images/fr_output_103_0.png)



![png](images/fr_output_103_1.png)



![png](images/fr_output_104_0.png)


Again we see that the dominant outcomes for our random forest model also strongly prefers classifications of Adoption and Transfer, with the three smaller subsets not being captured by the model predictions.

## 7. Conclusions and Next Steps <a class="anchor" id="Conclusions"></a>

#### Model Performance

As expected, the binomial classification model provides more interpretability and better overall performance than the multinomial model, though it loses the capability to predict the specific outcome type for each animal that is provided by the multinomial model. In the multinomial models, the main limitations became apparent in predicting cases for the outcomes with overall smaller distributions of animals such as death, euthanasia and return to owner when compared to the accuracy of predictions for Adoption and Transfer classes.

#### Next Steps for Improvement

Both models may be improved via several avenues. First, in order to combat the issue of skewed classes, a modified cost formula could be written which would impose a larger penalty during training for classes the edge case classes, which would help the models to learn all outcomes with more accuracy than what is achieved here. Secondarily, further optimization can be made into the pre-processing of the data (especially in the breeds and colors features, which ended up occupying most of the columns in the final dataset) in order to increase performance by feeding in higher quality engineered features. Finally, since only basic regularization has been performed on this dataset via subset selection, incorporating more sophisticated regularization penalties into the model could also lead to increases in predictive accuracy.

#### Actionable Recommendations

Based on the analysis in both the exploratory data analysis and feature importance analysis in the classification models, we have seen a connecting theme of animals that are (or simply look) more common having a harder time being placed in a home from the Austin Animal Center. This makes sense, since people who visit the shelter looking to adopt may naturally gravitate towards animals that look different, such as cats that are not Domestic Shorthair Mix breed, which accounts for about 80% of cats at the center as indicated by this dataset.

Although it might seem that this natural tendency of humans to 'spot the unique', there are ways around this. We know that there is a principle called the **["Mere-Exposure Effect"](https://en.wikipedia.org/wiki/Mere-exposure_effect)** wherein people who have some familiarity with something naturally tend to have an affinity towards it. This behavior can be leveraged in order to help animals who have a harder time being adopted, possibly by giving the animals of the most common breeds and colors which may otherwise be overlooked, exposure on social media or on the Austin Animal Center website. Short "Pet Bios", such as those written for animals up for adoption at the **[Austin Pets Alive!](https://www.austinpetsalive.org/)** animal shelter (see an example **[here](https://www.austinpetsalive.org/adopt/available-dog-details/?ID=40116)**) can give exposure to these otherwise common-looking animals which may be overlooked.

The effect of this social media exposure would be two-fold. First, it can draw attention directly to the animal shown on social media, but more importantly, people subscribed to the Austin Animal Center social media feeds that routinely see common animal breeds/colors (e.g. black shorthair domestic breed cats) can overtime naturally develop affinity for these animals via the mere-exposure effect. Skewing online exposure towards common varieties of animals is a solution that would be both low cost and straightforward to implement in order to help improve the placement of these animals in permanent homes.

## 8. Additional Resources <a class="anchor" id="Resources"></a>

* Dataset - [City of Austin - Open Data Portal](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)
* Austin Animal Center - [Website](http://www.austintexas.gov/department/aac)
* Austin Animal Center - [Facebook Page](https://www.facebook.com/AustinAnimalCenter/)
* Project Proposal - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%201/Erik%20Enriquez%20-%20Capstone%20Project%201%20Proposal.pdf)
* Code (IPython Notebooks):
    * Data Cleaning - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%201/Data%20Wrangling%20-%20Pet%20Adoption%20V2.ipynb)
    * Data Exploration - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%201/Data%20Story%20-%20Pet%20Adoption.ipynb)
    * Classification Models - [github link](https://github.com/emenriquez/Springboard-Coursework/blob/master/Capstone%20Project%201/Classification%20Models%20-%20Pet%20Adoption.ipynb)
