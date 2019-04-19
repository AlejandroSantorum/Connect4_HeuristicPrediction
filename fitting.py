import time

def read_data_from_file(filename, sep):
    xdata = []
    ydata = []
    f = open(filename, "r")
    line = f.readline()
    while line:
        aux = []
        array = line.split(sep)
        for elem in array:
            aux.append(float(elem))
        xdata.append(aux[:-1])
        ydata.append(aux[-1])
        line = f.readline()
    f.close()
    return xdata, ydata


FILENAME = "35K.csv"
SEP = ", "
if __name__ == "__main__":
    print("READING DATA.......")
    start = time.time()
    xdata, ydata = read_data_from_file(FILENAME, SEP)
    fin = time.time()
    print("FINISHED THE READING.......")
    print(xdata)
    print(ydata)
    print("Length: ", len(ydata))
    print("Time => ", fin - start)
