# Population Density

In this project, you will work with with a dataset about the population and
area of different countries to calcuate various statistics. 

## Background

The datasets for this project are taken from 
[**World Bank Open Data**](https://data.worldbank.org/). The datasets for the 
project are:

- Country Population (`datasets/API_SP.POP.TOTL_DS2.csv`): A dataset with the population of different countries between the years 1960 - 2021.
- Country Surface Area (`datasets/API_AG.TOTL.K2_DS2.csv`): A dataset with the surface area in square kilometers for all countries  between the years 1961 - 2018.

Each one is a `csv` file with a header row, then one row per country. The header
row describes the values in each column: the first are the country name, code,
the 'indicator' (population or surface area) name and code, and then each year
where the data is available.

> A **dataset** is a collection of related data. The data can be accessed and modified 
> to find useful insights and correlations. You can deal with a dataset by itself
> or in combination with other datasets.

## Your Task

Use the provided datasets to create a new dataset with each country's population 
density. 

Your program should write an output file as a CSV, similar to the input
datasets. Write your new dataset to the file `pop_density.csv`.

For each country, the new dataset should include:

- Name
- Country Code
- Population
- Surface Area
- Population Density 

The final dataset should have columns and values like this:

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

- country_name & country_code are available in both of the original datasets
- surface_area is available in the surface area dataset
- population is available in the population dataset
- the population density is a new column you'll add

Calculate the population density using the formula `pop_density = population / area`

If you encounter empty cells within the dataset, insert `"NA"` for Not Applicable 
for the data for that cell in your results.

## Starter Code

In addition to the CSV files in the `datasets` folder, you are provided with
starter code in a file called `country_analysis.py`. It includes function 
signatures, constant values, and some of the code for loading the files.

- `YEAR`: the year to use for calculating the data (meaning that our own data set will include this years' info only)
- `SURFACE_AREA_PATH`: location of the surface area dataset file
- `POPULATION_PATH`: location of the population dataset file

## Steps

- Use the CSV module to write each row to the output file. If you are storing
    each row as a dictionary, the DictWriter of the csv module may be useful.
https://docs.python.org/3/library/csv.html#csv.DictWriter

## Bonus: Other Metrics

After creating the dataset, you can also implement other metrics:

- Change the constant values and check that your program works for other years,
    or if there were other data files. 
- Country with highest density
- Country with highest surface area
- Countries with a population in range (X - Y)


