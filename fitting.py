import time

def read_xdata_from_file(filename, sep):
    xdata = []
    f = open(filename, "r")
    line = f.readline()
    while line:
        aux = []
        array = line.split(sep)
        for elem in array:
            aux.append(float(elem))
        xdata.append(aux)
        line = f.readline()
    f.close()
    return xdata


FILENAME = "35K.csv"
SEP = ", "
if __name__ == "__main__":
    print("READING DATA.......")
    start = time.time()
    xdata = read_xdata_from_file(FILENAME, SEP)
    fin = time.time()
    print("FINISHED THE READING.......")
    print(xdata)
    print("Time => ", fin - start)
