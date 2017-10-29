import time
from utils import *

def csv_loadHeader(filename, columns=[]):
    with open(filename, encoding="utf-8-sig") as f:
        return [e.strip() for e in get_elements(f.readline().lower().strip().split(";"), columns)]


def csv_load(filename, skip_first_line=False, columns=[], add_id_column=False):
    data = []
    with open(filename, encoding="utf-8-sig") as f:
        if skip_first_line:
            f.readline()

        content = f.readlines()
        counter = 0
        for line in content:
            if add_id_column:
                counter += 1
                line = str(counter) + ';' + line
            es = [e.strip() for e in get_elements(line.lower().strip().split(";"), columns)]
            data.append(es)

    return data

def save_ready_csv(data_queue, filename, header=None):
    with open(filename, "w", encoding="utf-8-sig") as f:
        if header is not None:
            f.write(header.strip() + '\n')

        while not data_queue.empty():
            row = data_queue.get()
            print("row:", row)
            str_line = ";".join(row) + '\n'
            print(filename, "Save:", str_line)
            f.write(str_line)


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