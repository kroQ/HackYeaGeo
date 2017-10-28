import time
from utils import *

def csv_loadHeader(filename, columns=[]):
    with open(filename, encoding="utf-8-sig") as f:
        return get_elements(f.readline().lower().strip().split(";"), columns)


def csv_load(filename, skip_first_line=False, columns=[]):
    data = []
    with open(filename, encoding="utf-8-sig") as f:
        if skip_first_line:
            f.readline()

        content = f.readlines()
        for line in content:
            data.append(get_elements(line.lower().strip().split(";"), columns))

    return data


if __name__ == '__main__':
    filename = '''C:/Users/wiedmo/Desktop/Hack/dane_wsadowe/dd.csv'''

    columns = [1, 6]
    h = csv_loadHeader(filename, columns=columns)
    print(h)
    t1 = time.time()
    df = csv_load(filename, skip_first_line=True, columns=columns)
    t2 = time.time()
    print(df[0])
    print("Time: ", t2 - t1)