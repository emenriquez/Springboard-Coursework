
# Understanding Factors in Animal Shelter Pet Adoption - Data Wrangling

In efforts to understand trends in pet adoption outcomes, the Austin Animal Center has provided data relating to the pets in their adoption center. Understanding this data and using it to model the factors that influence pet adoption could lead to recommendations that improve the performance of the center and help more pets find homes.

### Objective

In this project I will be exploring the dataset and using various data wrangling techniques to prepare the data via basic data wrangling techniques in order to prepare the data for analysis. This will include the following steps:

   1. Loading the data and extracting general info and structure
   2. Verifying that data is tidy
   3. Identifying & dealing with missing values
   4. Identifying & dealinig with outliers

### 1. Data Info and Structure

The dataset I am working with can be found **[here](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)**

**Note:** This dataset is updated hourly, and was accessed on Sunday, December 12th 2017 at 19:00 UTC for this project.


```python
# Display general information on dataset
data.info()
```

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


```python
# Display first 10 entries
data.head(10)
```




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
   
### 2. Data Cleaning

**i.** First the animal types were reduced to entries only containing cats and dogs, since they accounted for over 80% of the distribution of animals at the center and thus require the most resources to shelter and find homes.

**ii.** Next, for the 'Name' entries, I investigated those entries with and without asterisks. After contacting the custodians of this dataset, I recieved the following reply:

    "...ASO Staff are supposed to be using the asterisk when they name a pet at their review – after they come in.  
    If they came in with a name, then no asterisk."
    
Since the asterisks only denotes whether or not the name of the animal was given before they arrived at the shelter it is not a factor of interest for this analysis so were simply removed. The formatted names now appear without asterisks.

**iii.** Next up were the DateTime and MonthYear columns. Since these columns were proven to be identical, the MonthYear column was removed. The DateTime and Date of Birth columns were also converted to datetime objects.

**iv.** For the outcome types and subtypes columns, several steps were taken. Since the main investigation was into adoption and transfers, other outcomes were considered undesirable. Euthanasia and Death entries were maintained as-is, but entries labeled as 'Missing' and the small number of entries for animals that were brought to the center for 'Disposal' were removed. Additionally, the 'Rto-Adopt' entries were combined with the Adoption class.

This helps to significantly reduce the number of classes we are working with and thus improve the simplicity of the model. After refinement, the 'Outcome Type' column was converted into categorical value format.

**v.** Similarly, the 'Animal Type' and 'Sex upon Outcome' columns were converted into categorical features

**vi.** The Age upon Outcome column was converted into a timedelta object, since this format will allow for mathematical operations to be performed on it if needed.

**vii.** Next, the breed and color column categories were reduced significantly by selecting mixed breed entries of the format 'breed/breed' and replacing these entries with the first breed + 'Mix' (e.g. Chihuahua/Terrier => Chihuahua Mix). Similarly, colors of format 'color/color' were separated into 'Primary Color' and 'Secondary Color' entries. This process reduced the number of categories for breeds and colors to a manageable number for each.

    # of unique breeds in the original dataset: 1948
    # of mixed breeds classified by "breed/breed": 1551
    # of unique breeds after replacement: 399
    
    # of unique colors in the original dataset: 491
    # of mixed colors classified by "color/color": 435
    # of unique primary colors after replacement: 57
    # of unique secondary colors after replacement: 51

And finally the breed and color columns were converted into categorical features.

### 3. Missing Values

Out of the 5 columns that contain missing entries, 'Outcome Subtype' and 'Secondary Color' have empty entries by necessity, since some outcome types do not have subclasses, and some animals do not have secondary colors. In addition, names may not be crucial to the other animal attributes, but it is crucial to keep records of animals with and without given names, since this fact may also influence the outcome type for that animal.

What is left are a handful of entries without outcome type, which is critical information that we are interested in, and without sex information. Since we are currently working with a dataset of more than 76,000 entries, these entries removed without any significant impact on the data.

### 4. Outliers

Although many outliers were corrected with the previous formatting, one main column of interest that I will explored for outlier values was 'Outcome Subtype'. The marginal subtypes (those with less than 100 instances each) were combined into an 'Other' Outcome Subtype category. After this was done, the outcome subtype column entries were converted into categorical features.

## Closing Remarks

In this project, the Austin Animal Center dataset was explored and prepared for analysis. By converting columns into their appropriate formatting, removing duplicate information, and correcting missing values/outliers where possible, the data can yield more information in analysis. This includes the dataset taking less space in memory to work more quickly, as well as having a richer set of data which we can probe.

### Thanks for Reading!
