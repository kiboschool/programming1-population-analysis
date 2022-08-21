import json
import csv


def read_json(item_to_read='countries'):
    with open(file='countries.json', mode='r') as f:
        d = json.loads(f.read())[item_to_read]
        # print(d)
    return d


def pop_density():
    countries = read_json()
    densities = {}
    for country, data in countries.items():
        densities[country] = (float(data[0]) / float(data[1]))
    return dict_sort(densities)


def csv_out(dict_to_write):
    header = ['Country', 'Density']
    with open('countries.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for country, density in dict_to_write.items():
            row = [country, density]
            writer.writerow(row)


def dict_sort(dict_to_sort):
    mod_dict = {}
    values = sorted(dict_to_sort.values(), reverse=True)
    for item in values:
        mod_dict[get_key(dict_to_sort, item)] = item

    print(mod_dict)
    return mod_dict


def get_key(dict_to_check, val):
    for key, value in dict_to_check.items():
        if val == value:
            return key


def create_json_with_density():
    meta_dict = read_json()
    for country, data in meta_dict.items():
        data.append((float(data[0]) / float(data[1])))
    print(meta_dict)
    with open("all_country_data.json", "w") as outfile:
        json.dump(meta_dict, outfile, indent=4)


if __name__ == '__main__':
    # pop_density()
    # csv_out(pop_density())
    create_json_with_density()