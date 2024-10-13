import csv

YEAR = 2017
SURFACE_AREA_PATH = "datasets/API_AG.SRF.TOTL.K2_DS2.csv"
POPULATION_PATH = "datasets/API_SP.POP.TOTL_DS2.csv"
RESULT_PATH = "pop_density.csv"

def csv_to_list(filename):
    """
    Read a csv file and turn it into a list
    :param filename: dataset file path
    """
    with open(filename, 'r', encoding="utf-8-sig") as file:
        data = csv.DictReader(file)
        return list(data)


def write_results(densities):
    """
    Write a csv file based on the list of results
    :param densities: list of dictionaries to write to the output file
    """
    pass

def calculate_pop_densities(pop_data, sa_data, year):
    """
    Calculate the population density based on the population and surface area
    for each country for a given year.
    :param pop_data: list of dictionaries of population data
    :param sa_data: list of dictinoaries of surface area data
    :param year: the year to calculate the population density

    :return: list of dictionaries with the data per country (Country Name,
    Country Code, Population, Surface Area, Population Density)
    """
    pass

def main():
    """
    Use utility functions to read the data, process datasets, write to output
    """
    pop_data = csv_to_list(POPULATION_PATH)
    sa_data = csv_to_list(SURFACE_AREA_PATH)

if __name__ == '__main__':
    main()
