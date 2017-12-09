
# World Bank Dataset

### Problem Statement

For this mini-project, the following objectives are outlined:

Using data in file **'data/world_bank_projects.json'**:
1. Find the 10 countries with most projects
2. Find the top 10 major project themes (using column 'mjtheme_namecode')
3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

To start, the relevant packages and the dataset will be loaded so that we can get a look at what we are working with.


```python
# required to work with data as dataframe
import pandas as pd

# required to load json data and manipulate nested lists within the json file
import json
from pandas.io.json import json_normalize
```


```python
# load JSON dataset into DataFrame
df = pd.read_json('data/world_bank_projects.json')
```

Before tackling the objectives, we will first take a look at the general structure and properties of the data we are working with.


```python
# Display general info of the World Bank Dataset
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 500 entries, 0 to 499
    Data columns (total 50 columns):
    _id                         500 non-null object
    approvalfy                  500 non-null int64
    board_approval_month        500 non-null object
    boardapprovaldate           500 non-null object
    borrower                    485 non-null object
    closingdate                 370 non-null object
    country_namecode            500 non-null object
    countrycode                 500 non-null object
    countryname                 500 non-null object
    countryshortname            500 non-null object
    docty                       446 non-null object
    envassesmentcategorycode    430 non-null object
    grantamt                    500 non-null int64
    ibrdcommamt                 500 non-null int64
    id                          500 non-null object
    idacommamt                  500 non-null int64
    impagency                   472 non-null object
    lendinginstr                495 non-null object
    lendinginstrtype            495 non-null object
    lendprojectcost             500 non-null int64
    majorsector_percent         500 non-null object
    mjsector_namecode           500 non-null object
    mjtheme                     491 non-null object
    mjtheme_namecode            500 non-null object
    mjthemecode                 500 non-null object
    prodline                    500 non-null object
    prodlinetext                500 non-null object
    productlinetype             500 non-null object
    project_abstract            362 non-null object
    project_name                500 non-null object
    projectdocs                 446 non-null object
    projectfinancialtype        500 non-null object
    projectstatusdisplay        500 non-null object
    regionname                  500 non-null object
    sector                      500 non-null object
    sector1                     500 non-null object
    sector2                     380 non-null object
    sector3                     265 non-null object
    sector4                     174 non-null object
    sector_namecode             500 non-null object
    sectorcode                  500 non-null object
    source                      500 non-null object
    status                      500 non-null object
    supplementprojectflg        498 non-null object
    theme1                      500 non-null object
    theme_namecode              491 non-null object
    themecode                   491 non-null object
    totalamt                    500 non-null int64
    totalcommamt                500 non-null int64
    url                         500 non-null object
    dtypes: int64(7), object(43)
    memory usage: 195.4+ KB
    

The dataset presented here has 500 entries and 50 main features for each. We can see from this info that there are some missing entries in the data, and the column labels are a bit messy. In order to get a better idea of the data we should look at a few entries.


```python
# Extract a preview of the first few rows of data
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>_id</th>
      <th>approvalfy</th>
      <th>board_approval_month</th>
      <th>boardapprovaldate</th>
      <th>borrower</th>
      <th>closingdate</th>
      <th>country_namecode</th>
      <th>countrycode</th>
      <th>countryname</th>
      <th>countryshortname</th>
      <th>...</th>
      <th>sectorcode</th>
      <th>source</th>
      <th>status</th>
      <th>supplementprojectflg</th>
      <th>theme1</th>
      <th>theme_namecode</th>
      <th>themecode</th>
      <th>totalamt</th>
      <th>totalcommamt</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>{'$oid': '52b213b38594d8a2be17c780'}</td>
      <td>1999</td>
      <td>November</td>
      <td>2013-11-12T00:00:00Z</td>
      <td>FEDERAL DEMOCRATIC REPUBLIC OF ETHIOPIA</td>
      <td>2018-07-07T00:00:00Z</td>
      <td>Federal Democratic Republic of Ethiopia!$!ET</td>
      <td>ET</td>
      <td>Federal Democratic Republic of Ethiopia</td>
      <td>Ethiopia</td>
      <td>...</td>
      <td>ET,BS,ES,EP</td>
      <td>IBRD</td>
      <td>Active</td>
      <td>N</td>
      <td>{'Percent': 100, 'Name': 'Education for all'}</td>
      <td>[{'code': '65', 'name': 'Education for all'}]</td>
      <td>65</td>
      <td>130000000</td>
      <td>130000000</td>
      <td>http://www.worldbank.org/projects/P129828/ethi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>{'$oid': '52b213b38594d8a2be17c781'}</td>
      <td>2015</td>
      <td>November</td>
      <td>2013-11-04T00:00:00Z</td>
      <td>GOVERNMENT OF TUNISIA</td>
      <td>NaN</td>
      <td>Republic of Tunisia!$!TN</td>
      <td>TN</td>
      <td>Republic of Tunisia</td>
      <td>Tunisia</td>
      <td>...</td>
      <td>BZ,BS</td>
      <td>IBRD</td>
      <td>Active</td>
      <td>N</td>
      <td>{'Percent': 30, 'Name': 'Other economic manage...</td>
      <td>[{'code': '24', 'name': 'Other economic manage...</td>
      <td>54,24</td>
      <td>0</td>
      <td>4700000</td>
      <td>http://www.worldbank.org/projects/P144674?lang=en</td>
    </tr>
    <tr>
      <th>2</th>
      <td>{'$oid': '52b213b38594d8a2be17c782'}</td>
      <td>2014</td>
      <td>November</td>
      <td>2013-11-01T00:00:00Z</td>
      <td>MINISTRY OF FINANCE AND ECONOMIC DEVEL</td>
      <td>NaN</td>
      <td>Tuvalu!$!TV</td>
      <td>TV</td>
      <td>Tuvalu</td>
      <td>Tuvalu</td>
      <td>...</td>
      <td>TI</td>
      <td>IBRD</td>
      <td>Active</td>
      <td>Y</td>
      <td>{'Percent': 46, 'Name': 'Regional integration'}</td>
      <td>[{'code': '47', 'name': 'Regional integration'...</td>
      <td>52,81,25,47</td>
      <td>6060000</td>
      <td>6060000</td>
      <td>http://www.worldbank.org/projects/P145310?lang=en</td>
    </tr>
    <tr>
      <th>3</th>
      <td>{'$oid': '52b213b38594d8a2be17c783'}</td>
      <td>2014</td>
      <td>October</td>
      <td>2013-10-31T00:00:00Z</td>
      <td>MIN. OF PLANNING AND INT'L COOPERATION</td>
      <td>NaN</td>
      <td>Republic of Yemen!$!RY</td>
      <td>RY</td>
      <td>Republic of Yemen</td>
      <td>Yemen, Republic of</td>
      <td>...</td>
      <td>JB</td>
      <td>IBRD</td>
      <td>Active</td>
      <td>N</td>
      <td>{'Percent': 50, 'Name': 'Participation and civ...</td>
      <td>[{'code': '57', 'name': 'Participation and civ...</td>
      <td>59,57</td>
      <td>0</td>
      <td>1500000</td>
      <td>http://www.worldbank.org/projects/P144665?lang=en</td>
    </tr>
    <tr>
      <th>4</th>
      <td>{'$oid': '52b213b38594d8a2be17c784'}</td>
      <td>2014</td>
      <td>October</td>
      <td>2013-10-31T00:00:00Z</td>
      <td>MINISTRY OF FINANCE</td>
      <td>2019-04-30T00:00:00Z</td>
      <td>Kingdom of Lesotho!$!LS</td>
      <td>LS</td>
      <td>Kingdom of Lesotho</td>
      <td>Lesotho</td>
      <td>...</td>
      <td>FH,YW,YZ</td>
      <td>IBRD</td>
      <td>Active</td>
      <td>N</td>
      <td>{'Percent': 30, 'Name': 'Export development an...</td>
      <td>[{'code': '45', 'name': 'Export development an...</td>
      <td>41,45</td>
      <td>13100000</td>
      <td>13100000</td>
      <td>http://www.worldbank.org/projects/P144933/seco...</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 50 columns</p>
</div>



The data above shows that our JSON data contains several features comprised of lists of subfeatures. This is important to note and will be addressed in the second and third problems we are given.

### 1. Find the 10 countries with most projects

Working with a dataframe here has a few advantages. We can easily count the number of times each country appears in the list of projects. 


```python
# List number of occurances for each country
df['countryname'].value_counts()
```




    People's Republic of China                  19
    Republic of Indonesia                       19
    Socialist Republic of Vietnam               17
    Republic of India                           16
    Republic of Yemen                           13
    Kingdom of Morocco                          12
    Nepal                                       12
    People's Republic of Bangladesh             12
    Republic of Mozambique                      11
    Africa                                      11
    Federative Republic of Brazil                9
    Burkina Faso                                 9
    Islamic Republic of Pakistan                 9
    Republic of Armenia                          8
    Republic of Tajikistan                       8
    United Republic of Tanzania                  8
    Kyrgyz Republic                              7
    Hashemite Kingdom of Jordan                  7
    Lao People's Democratic Republic             7
    Federal Republic of Nigeria                  7
    West Bank and Gaza                           6
    Democratic Republic of the Congo             6
    Islamic State of Afghanistan                 6
    Republic of Peru                             6
    Republic of Kenya                            6
    Republic of Nicaragua                        6
    Republic of Uzbekistan                       5
    Republic of Haiti                            5
    Republic of Moldova                          5
    Republic of Liberia                          5
                                                ..
    Jamaica                                      2
    Republic of Ecuador                          2
    United Mexican States                        2
    Republic of Malawi                           2
    Republic of Mauritius                        2
    Republic of Sierra Leone                     2
    Republic of Kosovo                           2
    People's Republic of Angola                  1
    Republic of Kiribati                         1
    Republic of Zimbabwe                         1
    Europe and Central Asia                      1
    Republic of Costa Rica                       1
    East Asia and Pacific                        1
    Republic of Panama                           1
    Republic of Cape Verde                       1
    Kingdom of Thailand                          1
    Republic of Congo                            1
    Central African Republic                     1
    Romania                                      1
    Republic of Belarus                          1
    Republic of Poland                           1
    Republic of Serbia                           1
    Democratic Socialist Republic of Sri Lan     1
    Republic of Namibia                          1
    Republic of Chad                             1
    Bosnia and Herzegovina                       1
    Antigua and Barbuda                          1
    Tuvalu                                       1
    Kingdom of Tonga                             1
    Republic of Chile                            1
    Name: countryname, Length: 118, dtype: int64



We can see that the generated table automatically lists the country occurences in descending order, so the first 10 entries correspond to the top 10 countries with the most projects in this dataset.

Closer inspection reveals that the 10th entry is Africa. Africa is not a country. Just to double check, if we follow one of the url links from the 'url' column of a row for Africa (http://www.worldbank.org/projects/P144902?lang=en) we can see that indeed on the World Bank website, the country for the project is listed as Africa so it doesn't appear to be a reporting error in our dataset. We will leave it as is for now.


```python
# List previews of urls from the Africa rows
df[df['countryname'] == 'Africa']['url'][:5]
```




    45    http://www.worldbank.org/projects/P125018/west...
    46    http://www.worldbank.org/projects/P118213/rcip...
    51    http://www.worldbank.org/projects/P130888/buil...
    58    http://www.worldbank.org/projects/P144902?lang=en
    65    http://www.worldbank.org/projects/P075941/nels...
    Name: url, dtype: object



We can now use the previous list to generate a table with the top 10 countries that had the most projects funded in this dataset, shown below.


```python
# Generate dataframe with top 10 countries with most projects in this dataset
top10 = pd.DataFrame(data= {'Country': df['countryname'].value_counts().index.values[:10],
                   '# of Projects': df['countryname'].value_counts().values[:10]},
             columns = ['Country', '# of Projects'],
             index=range(1,11)
                    )

# Label the index as ranking
top10.index.name = 'Rank'

# Display top10 rankings
print(top10)
```

                                  Country  # of Projects
    Rank                                                
    1          People's Republic of China             19
    2               Republic of Indonesia             19
    3       Socialist Republic of Vietnam             17
    4                   Republic of India             16
    5                   Republic of Yemen             13
    6                  Kingdom of Morocco             12
    7                               Nepal             12
    8     People's Republic of Bangladesh             12
    9              Republic of Mozambique             11
    10                             Africa             11
    

The resulting table celarly shows the top 10 countries (read: 9 countries and 1 continent) that had projects in this dataset.

### 2. Find the top 10 major project themes (using column 'mjtheme_namecode')

Although the second problem we will address looks very similar to the first, we cannot simply plug in the same method due to the structure of the 'mjtheme_namecode' column we are working with. We can see below that calling the first few entries in the column returns entries comprised of lists.


```python
df['mjtheme_namecode'].head()
```




    0    [{'code': '8', 'name': 'Human development'}, {...
    1    [{'code': '1', 'name': 'Economic management'},...
    2    [{'code': '5', 'name': 'Trade and integration'...
    3    [{'code': '7', 'name': 'Social dev/gender/incl...
    4    [{'code': '5', 'name': 'Trade and integration'...
    Name: mjtheme_namecode, dtype: object



In order to get a better look and more easily deal with the JSON nested list data, we will load the data as a list instead directly into a pandas dataframe.


```python
# import the World Bank data as a nested list structure
json1 = json.load((open('data/world_bank_projects.json')))

# Extract 'mjtheme_namecode' column from the JSON data
themes = json_normalize(json1, 'mjtheme_namecode')

# Print the first 10 rows of the extracted themes column
print(themes.head(10))
```

      code                                          name
    0    8                             Human development
    1   11                                              
    2    1                           Economic management
    3    6         Social protection and risk management
    4    5                         Trade and integration
    5    2                      Public sector governance
    6   11  Environment and natural resources management
    7    6         Social protection and risk management
    8    7                   Social dev/gender/inclusion
    9    7                   Social dev/gender/inclusion
    

We can see by looking at the entries above that now we have parsed the entries of the themes column into codes and respective names of project themes. There are missing entries in the 'name' column, as shown above. The task of filling in these missing values will be addressed in the next section, but for now we will work with the data as-is.


```python
# Display occurences in the 'name' column of themes
print('Top Occurences of Themes by Name: \n{0}'.format(themes['name'].value_counts()))

print('\nTop Occurences of Themes by Code: \n{0}'.format(themes['code'].value_counts()))

# Display message showing number of NA entries in the 'code' column
print('\n# of missing entries in "code" column: {0}'.format(themes['code'].isnull().sum()))
```

    Top Occurences of Themes by Name: 
    Environment and natural resources management    223
    Rural development                               202
    Human development                               197
    Public sector governance                        184
    Social protection and risk management           158
    Financial and private sector development        130
                                                    122
    Social dev/gender/inclusion                     119
    Trade and integration                            72
    Urban development                                47
    Economic management                              33
    Rule of law                                      12
    Name: name, dtype: int64
    
    Top Occurences of Themes by Code: 
    11    250
    10    216
    8     210
    2     199
    6     168
    4     146
    7     130
    5      77
    9      50
    1      38
    3      15
    Name: code, dtype: int64
    
    # of missing entries in "code" column: 0
    

We can see that although there are a large amount of missing entries in the 'name' column, there do not appear to be any missing values in the 'code' column. The missing entries in the 'name' column are interesting, since they are "" entries. They are not null, but since they are strings of length 0 they can be found quite easily.

Although we have the list of top occurences of themes by code without missing entries above to generate our top 10 (only theme code 3 doesn't make the top 10 list), using project theme codes doesn't have much meaning. We should translate the theme codes back into names before we make our list.

In order to build our top 10 list, the first step will be to build a dictionary that can translate theme codes into the respective theme names.


```python
# Initialize empty lists to fill with keys and values for dictionary
themes_names = []
themes_codes = []
themes_dict = []

# Iterate over the entries in themes and extract only unique values to create key-value pairs for dictionary
for entry in range(themes['name'].shape[0]):
    if (len(themes['name'][entry]) > 0) & (themes['name'][entry] not in themes_names):
        themes_codes.append(themes['code'][entry])
        themes_names.append(themes['name'][entry])

        
# Generate dictionary to relate project theme codes to their name values
themes_dict = dict(zip(themes_codes, themes_names))
```

Now that we have a translator, we can build our top 10 list with a similar process to the one we used in the previous section.


```python
# Generate Series with codes translated to names using themes_dict
code2name = pd.Series([themes_dict[x] for x in themes['code']])

# Generate ranking of top 10 Project Themes
top10 = pd.DataFrame(data= {'Project Theme': code2name.value_counts().index.values[:10],
                   '# of Projects': code2name.value_counts().values[:10]},
             columns = ['Project Theme', '# of Projects'],
             index=range(1,11)
                    )

# Label the index as ranking
top10.index.name = 'Rank'

# Display top10 rankings
print(top10)
```

                                         Project Theme  # of Projects
    Rank                                                             
    1     Environment and natural resources management            250
    2                                Rural development            216
    3                                Human development            210
    4                         Public sector governance            199
    5            Social protection and risk management            168
    6         Financial and private sector development            146
    7                      Social dev/gender/inclusion            130
    8                            Trade and integration             77
    9                                Urban development             50
    10                             Economic management             38
    

The resulting table is much neater!

### 3. Create a dataframe with the missing names filled in for 'mjtheme_namecode' column

Since we have already created a dictionary to translate project theme codes into names, this problem becomes quite simple to address. There are a few options to do this: 1) We can search the 'name' column in our themes data for any entries that are strings of 0 length and replace them with their corresponding theme according to the codes for those entries. 2) A much quicker option would be to use the complete list of names we already generated in the previous section (code2name) and replace the original 'name' column of themes.


```python
# Display list of values before replacement of missing entries
print('List of unique values occuring in "names" column of themes \n', themes['name'].unique())

# Replace missing values with code2name
themes['name'] = code2name

# Display list of values after replacement of missing entries
print('\nList of unique values occuring in "names" after replacement \n', themes['name'].unique())
```

    List of unique values occuring in "names" column of themes 
     ['Human development' '' 'Economic management'
     'Social protection and risk management' 'Trade and integration'
     'Public sector governance' 'Environment and natural resources management'
     'Social dev/gender/inclusion' 'Financial and private sector development'
     'Rural development' 'Urban development' 'Rule of law']
    
    List of unique values occuring in "names" after replacement 
     ['Human development' 'Environment and natural resources management'
     'Economic management' 'Social protection and risk management'
     'Trade and integration' 'Public sector governance'
     'Social dev/gender/inclusion' 'Financial and private sector development'
     'Rural development' 'Urban development' 'Rule of law']
    

We can see now that in the second table there are no "" entries found. We can also visualize this by returning to the count of occurrences for each value in the 'name' column of themes.


```python
themes['name'].value_counts()
```




    Environment and natural resources management    250
    Rural development                               216
    Human development                               210
    Public sector governance                        199
    Social protection and risk management           168
    Financial and private sector development        146
    Social dev/gender/inclusion                     130
    Trade and integration                            77
    Urban development                                50
    Economic management                              38
    Rule of law                                      15
    Name: name, dtype: int64



### Thank you for reading!
