from operator import itemgetter


def get_elements(data, columns):
    if isinstance(columns, list):
        if len(columns) > 0:
            return itemgetter(*columns)(data)
        else:
            return data
    else:
        raise Exception("Columns mu be integer list")