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
        arr_lstat.append(line[0])
        arr_rm.append(line[1])
        arr_ptratio.append(line[2])
        arr_medv.append(line[3])

    for lstat, rm, ptratio, medv in zip(arr_lstat, arr_rm, arr_ptratio, arr_medv):
        fd_out.write("{},{},{},{}\n".format(lstat, rm, ptratio, medv))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)

