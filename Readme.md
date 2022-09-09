# Population Density
At this project, we will be working with country datasets. A dataset is a collection of data that has different relations. This data can be accessed and modified to creating useful information.
We can deal with a dataset as a whole entity or in combination with other sets.

Our datasets for this projects are taken from the **World Bank Open Data**. Our sets for the project are:
- Country Population: A dataset that includes each country (and other predefined geographical areas) population between the years 1960 - 2021.
- Country Surface Area: A dataset that includes surface area in sq.km for all countries (including same predefined geographical areas) between the years 1961 - 2018.

We will use both of these datasets to create our own customized population density dataset.

## Requirements
You are asked to use both given datasets to create a new dataset which shows each country's population density. Our new dataset should include:
- Country Name
- Country Code
- Country Population
- Country Surface Area
- Population Density 

You can access both of the mentioned dataseta at the `datasets` folder attached to the project.
The final set should look like this:

|country_name |country_code| surface_area | population | density |
|-----|------------------------------|-------------|------------------|---------------|
Aruba|	ABW	|107195	|180	|595.5277778
Africa Eastern and Southern|	AFE|	694665117|	15121155.64|	45.93994887|
Afghanistan|	AFG|	39835428|	652860|	61.01679993|
Africa Western and Central |	AFW|	470898870|	9166270|	51.37300887|
Angola|	AGO|	33933611|	1246700|	27.21874629|
Albania|	ALB|	2811666|	28750|	97.79707826|
Andorra|	AND|	77354|	470|	164.5829787|
Arab World|	ARB|	444517783|	13142338.82|	33.82333914|
United Arab Emirates|	ARE|	9991083|	98647.9|	101.2802401|

As you can see, columns are available as follows:
- country_name & country_code are available at both datasets
- surface_area is available at the surface area indicator dataset
- population is available at the population indicator surface area
- density is the additional column that you are asked to calculate using `(pop_density = population/area)`

## Configuration file
You will be given a configuration file that looks like:
```
{
  "surface_area_year": 2017,
  "population_year": 2021,
  "sa_file": "datasets/API_AG.SRF.TOTL.K2_DS2.csv",
  "pop_file": "datasets/API_SP.POP.TOTL_DS2.csv",
  "heading_line": 4,
  "list_size": 6
}
```
This file has some inputs to your code that you can later change without the need to modify values within the code:
- surface_area_year: is the year that we will use to pull surface areas from the first dataset (meaning that our own data set will include this years' info only)
- population_year: is the year that we will use to filter population values from the second dataset (meaning that our own data set will include this years' info only)
- sa_file: location for the first dataset file
- pop_file: location for the second datraset file
- heading_line: number of lines in the dataset that are used for heading data
- list_size: length of the list that should be rendered using the flask endpoint

##
After creating your own dataset, you need to create a free style flask endpoint that renders the data within your new set.
You can also add new metrics to the page like:
- Country with highest density
- Country with highest surface area
- Countries with a population in range (X - Y)

# Starter Code
You are given a file called `country_analysis.py` that shows function signatures and some suggested starter code that you can start with. 
Functions are documented so you can understand what would be the input and output for each one of them.

# Testing
WIP

# Hints
- Datasets format is the same. That means no more work is needed when merging columns from different datasets. Same column of countries is available at both sets.
- Based on what you have learnt in the course - think of the most suitable data structure that you can use to save the data internally before pasting it to your own dataset.
- Start by implementing your functions one by one and check their performance before you move forward.