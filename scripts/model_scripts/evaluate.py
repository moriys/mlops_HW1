import os
import sys
import pickle
import json

import pandas as pd

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py data-file model\n")
    sys.exit(1)

df = pd.read_csv(sys.argv[1], header=None)
X = df.iloc[:,[0,1,2]]
y = df.iloc[:,3]

with open(sys.argv[2], "rb") as fd:
    model = pickle.load(fd)

score = model.score(X, y)

prc_file = os.path.join("evaluate", "score.json")
os.makedirs(os.path.join("evaluate"), exist_ok=True)

with open(prc_file, "w") as fd:
    json.dump({"score": score}, fd)
