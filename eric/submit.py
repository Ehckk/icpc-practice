from argparse import ArgumentParser
from subprocess import Popen, PIPE
from pathlib import Path

parser = ArgumentParser()
parser.add_argument("file", type=str,
    help="Path to the python file to submit")
parser.add_argument("-o", "--out", nargs="?", type=str,
    help="The name of the file to write to")
parser.add_argument("-d", "--dir", nargs="?", type=str,
    help="The directory to write to", default=None)
args = parser.parse_args()

sub_path = Path.cwd()
if args.dir:
    sub_path = sub_path.joinpath(Path(args.dir))
    sub_path.mkdir(parents=True, exist_ok=True)
sub_path = sub_path.joinpath(Path(f"{args.out or args.file}.sub"))

with open(sub_path, "w") as file:
    command = f"python {args.file}.py"
    process = Popen(command, stdout=PIPE, text=True)
    file.write(process.stdout.read())

exit()