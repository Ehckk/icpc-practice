from argparse import ArgumentParser
from os import path
import subprocess

parser = ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-o", "--out")
args = parser.parse_args()

output = f"output\\{args.out}.out"
with open(path.join(path.dirname(__file__), output), "w") as file:
    process = subprocess.Popen(f"python {args.file}.py", stdout=subprocess.PIPE, text=True)
    file.write(process.stdout.read())
exit()