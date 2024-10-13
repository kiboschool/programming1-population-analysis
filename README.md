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

The first few rows of the final dataset should jave values like this:

```
Country Name,Country Code,Population,Surface Area,Population Density
Aruba,ABW,105361,180,585.3388888888888
Africa Eastern and Southern,AFE,626392880,15121155.64,41.424934370955256
Afghanistan,AFG,36296111,652860,55.595550347700886
Africa Western and Central,AFW,423769930,9166270,46.231447469908694
Angola,AGO,29816769,1246700,23.916554904949066
Albania,ALB,2873457,28750,99.94633043478261
Andorra,AND,76997,470,163.82340425531916
Arab World,ARB,411942825,13142338.82,31.344711975702968
United Arab Emirates,ARE,9487206,98647.9,96.17240711662387
```

- Country Name & Country Code are available in both of the original datasets
- Population is available in the population dataset
- Surface Area is available in the surface area dataset
- Population Density is a new column you'll calculate and add

Here's the same data as a table, for clarity:

| Country Name | Country Code | Population | Surface Area | Population Density |
|--------------|--------------|------------|--------------|--------------------|
Aruba | ABW | 105361 | 180 | 585.3388888888888
Africa Eastern and Southern | AFE | 626392880 | 15121155.64 | 41.424934370955256
Afghanistan | AFG | 36296111 | 652860 | 55.595550347700886
Africa Western and Central | AFW | 423769930 | 9166270 | 46.231447469908694
Angola | AGO | 29816769 | 1246700 | 23.916554904949066
Albania | ALB | 2873457 | 28750 | 99.94633043478261
Andorra | AND | 76997 | 470 | 163.82340425531916
Arab World | ARB | 411942825 | 13142338.82 | 31.344711975702968
United Arab Emirates | ARE | 9487206 | 98647.9 | 96.17240711662387

Calculate the population density using the formula:

```
pop_density = population / area`
```

If you encounter empty cells within the dataset, insert `"NA"` for Not Applicable
for the data for that cell in your results.

## Starter Code

In addition to the CSV files in the `datasets` folder, you are provided with
starter code in a file called `country_analysis.py`. It includes function
signatures, constant values, and some of the code for loading the files.

- `YEAR`: the year to use for calculating the data (meaning that our own data set will include this years' info only)
- `SURFACE_AREA_PATH`: location of the surface area dataset file
- `POPULATION_PATH`: location of the population dataset file
- `RESULT_PATH`: location to write the results

## Steps

You need to fill in the functions `main`, `calculate_pop_densities`, and
`write_results`.

Use the CSV module to write each row to the output file. If you are storing
each row as a dictionary, the [DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter) of the csv module may be useful.

Test your code, check that the results make sense, and submit your solution once
you have a working project.

## Bonus: Other Metrics

After creating the dataset, you can also implement other metrics:

- Change the constant values and check that your program works for other years,
    or if there were other data files.
- Find the country with highest density
- Find the country with highest surface area
- Countries with a population within a given range (X - Y)

There are a lot of interesting things you can explore with the data, so feel
free to be creative!
