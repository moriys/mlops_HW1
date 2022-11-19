import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_lstat = []
    arr_rm = []
    arr_ptratio = []
    arr_medv = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        if line[0]:
            arr_lstat.append(line[0])
        else:
            arr_lstat.append(0)
        if line[1]:
            arr_rm.append(line[1])
        else:
            arr_rm.append(0)
        if line[2]:
            arr_ptratio.append(line[2])
        else:
            arr_ptratio.append(0)
        if line[3]:
            arr_medv.append(line[3])
        else:
            arr_medv.append(0)

    s_lstat = sum(arr_lstat)
    for i in range(len(arr_lstat)):
        if arr_lstat[i] == 0:
            arr_lstat[i] = round(s_lstat / len(arr_lstat), 2)

    s_rm = sum(arr_rm)
    for i in range(len(arr_rm)):
        if arr_rm[i] == 0:
            arr_rm[i] = round(s_rm / len(arr_rm), 2)

    s_medv = sum(arr_medv)
    for i in range(len(arr_medv)):
        if arr_medv[i] == 0:
            arr_medv[i] = round(s_medv / len(arr_medv), 2)

    s_ptratio = sum(arr_ptratio)
    for i in range(len(arr_ptratio)):
        if arr_ptratio[i] == 0:
            arr_ptratio[i] = round(s_ptratio / len(arr_ptratio), 2)

    for lstat, rm, ptratio, medv in zip(arr_lstat, arr_rm, arr_ptratio, arr_medv):
        fd_out.write("{},{},{},{}\n".format(lstat, rm, ptratio, medv))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)

