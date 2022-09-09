import json
import csv

configuration = {}

pop_density = {"country_name": [],
               "country_code": [],
               "surface_area": [],
               "population": [],
               "density": []
               }


def read_json():
    """
    This function reads JSON files and returns an internal dictionary
    """
    pass


def get_indicator_from_dataset(filename, indicator='surface_area'):
    """
    This function gets needed data from a dataset file based on indicator value
    :param filename: dataset file path
    :param indicator: indicates what dataset are we working with 1)population 2)surface_area
    """
    pass


def get_countries(filename):
    """
    This function pulls country name and country code from a dataset and saves it to our internal data structure for further usage (updates global dictionary)
    :param filename: dataset file path
    """
    pass

def create_densities():
    """
    Builds the whole structure we need - updates pop_density with all five needed pieces of information 1)country_name 2)country_code 3)population 4)surface_area 5)density
    """
    pass


def customized_dataset():
    """
    Builds our customized dataset using all other utility functions and our internal data structure that holds all processed data
    """
    pass


if __name__ == '__main__':
    read_json()

    create_densities()
    customized_dataset()
