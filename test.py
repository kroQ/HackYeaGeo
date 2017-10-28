from data import *

input_data_filename = '''C:/Users/wiedmo/Desktop/Hack/dane wsadowe/dane wejściowe.csv'''
address_dict_filename = '''C:/Users/wiedmo/Desktop/Hack/dane wsadowe/Słownik Adresów.csv'''

def dict_by_column(data_header, data, column_name, column_number):
    if column_name not in data_header:
        raise Exception("Cannot find column " + str(column_name) + " in " + str(data_header))

    dict_data = {}
    cols = list(range(0, len(data[0])))
    cols.pop(column_number)
    print(column_name, type(cols), cols)
    for row in data:
        key = data[column_number]
        print("key", type(key), key)
        if key not in dict_data:
            dict_data[key] = []
        dict_data[key].append(get_elements(row, cols))

    return dict_data


if __name__ == '__main__':
    input_data_header  = csv_loadHeader(input_data_filename)

    columns = [1, 2, 4, 5]
    input_data_header = csv_loadHeader(input_data_filename, columns=columns)
    input_data = csv_load(input_data_filename, skip_first_line=True, columns=columns)

    print(input_data_header)
    print(len(input_data), input_data[0])

    print("-------------------")

    address_dict_header = csv_loadHeader(input_data_filename, columns=[])
    address_dict = csv_load(input_data_filename, skip_first_line=True, columns=[])

    print(address_dict_header)
    print(len(address_dict), address_dict[0])

    print("++++++++++++++++++++")

    #ddh = csv_loadHeader(input_data_filename, columns=[])
    dd = dict_by_column(address_dict_header, address_dict, address_dict_header[2], 1)

    print(len(dd), len(dd[address_dict_header[2]]), dd[address_dict_header[2]][0])