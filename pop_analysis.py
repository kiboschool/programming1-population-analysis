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
    global configuration
    with open(file='conf.json', mode='r') as f:
        d = json.loads(f.read())
        # print(d)
        configuration = d
    return d


def get_indicator_from_dataset(filename, indicator='surface_area'):
    """
    This function gets needed data from a dataset file based on indicator value
    :param filename: dataset file path
    :param indicator: indicates what dataset are we working with 1)population 2)surface_area
    """
    filtered_data = []
    with open(filename, 'r') as data_reader:
        data = csv.reader(data_reader)

        for idx, line in enumerate(data):
            if idx == configuration['heading_line']:
                if indicator == "surface_area":
                    year_idx = line.index(str(configuration['surface_area_year']))
                elif indicator == "population":
                    year_idx = line.index(str(configuration['population_year']))
                else:
                    print("not supported indicator")
                    exit(-1)

            if idx > configuration['heading_line']:
                filtered_data.append(line[year_idx])

    return filtered_data


def get_countries(filename):
    """
    This function pulls country name and country code from a dataset and saves it to our internal data structure for further usage (updates global dictionary)
    :param filename: dataset file path
    """
    global pop_density
    with open(filename, 'r') as data_reader:
        data = csv.reader(data_reader)
        for idx, line in enumerate(data):
            if idx > configuration['heading_line']:
                pop_density['country_name'].append(line[0])
                pop_density['country_code'].append(line[1])


def create_densities():
    """
    Builds the whole structure we need - updates pop_density with all five needed pieces of information 1)country_name 2)country_code 3)population 4)surface_area 5)density
    """
    global pop_density
    idx = 0
    get_countries(filename=configuration['sa_file'])
    pop_density['surface_area'] = get_indicator_from_dataset(filename=configuration['sa_file'], indicator='surface_area')
    pop_density['population'] = get_indicator_from_dataset(filename=configuration['pop_file'], indicator='population')

    while idx < len(pop_density['surface_area']):
        density = float(pop_density['population'][idx]) / float(pop_density['surface_area'][idx])
        # print(density)
        pop_density['density'].append(density)
        idx = idx + 1


def customized_dataset():
    """
    Builds our customized dataset using all other utility functions and our internal data structure that holds all processed data
    """
    global pop_density

    with open('custom_dataset_2.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(pop_density.keys())
        for idx in range(0, len(pop_density['country_name'])):
            row = [pop_density['country_name'][idx],
                   pop_density['country_code'][idx],
                   pop_density['population'][idx],
                   pop_density['surface_area'][idx],
                   pop_density['density'][idx]]
            writer.writerow(row)


if __name__ == '__main__':
    read_json()
    create_densities()
    customized_dataset()
