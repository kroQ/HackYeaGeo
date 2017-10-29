from threading import Thread
from Queue import Queue

threads = []

def message(lista1):
    sum = 0
    for par in lista1:
        sum += par

    print(sum)

    return sum

if __name__ == "__main__":
    for i in range(10):
        process = Thread(target=message, args=[[3, 6, 32, 12]])
        process.start()
        threads.append(process)

    for process in threads:
        process.join()