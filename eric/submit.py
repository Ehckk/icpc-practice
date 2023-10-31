from argparse import ArgumentParser
from pathlib import Path
import subprocess

parser = ArgumentParser()
parser.add_argument("submission", type=str,
                    help="Path to the python file to submit")
parser.add_argument("-d", "--dir", type=str,
                    help="Path to directory with input and answer files", default=None)
parser.add_argument("-i", "--in-ext", type=str,
                    help="File extension for input files", default="in")
parser.add_argument("-a", "--ans-ext", type=str,
                    help="File extension for answer files", default="ans")
parser.add_argument("-t", "--time-limit", type=int,
                    help="Time limit in milliseconds", default=None)
args = parser.parse_args()

verdicts = {
    "AC": "Accepted",
    "WA": "Wrong Answer",
    "TLE": "Time Limit Exceeded",
    "RE": "Runtime Error"
}


def test_submission(cmd, testcase, answer, time_limit=None):
    try:
        solution = subprocess.run(cmd, input=testcase, timeout=time_limit, text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = solution.stdout
        type(output)
        if not output == answer:
            verdict_args = [f"Received:\n{output}", f"Expected:\n{answer}"]
            return "WA", verdict_args
        return "AC", []
    except subprocess.TimeoutExpired:
        return "TLE", []
    except subprocess.CalledProcessError as err:
        return "RE", [err.stderr]


CWD = Path.cwd()
path = CWD.joinpath(Path(args.dir))
testcases = []
for in_path in path.glob(f"*.{args.in_ext}"):
    ans_path = path.joinpath(Path(f"{in_path.stem}.{args.ans_ext}"))
    if not ans_path.exists():
        continue
    testcases.append((in_path, ans_path))

if len(testcases) == 0:
    raise NotImplementedError("No testcase files found!")

submission_path = CWD.joinpath(Path(args.submission))
command = f"python {submission_path}"  # TODO: more than python?
result = "WA"
for i in range(len(testcases)):
    in_path, ans_path = testcases[i]
    print(f"{i + 1}/{len(testcases)}: ", end="")
    with open(in_path, "r") as in_file, open(ans_path, "r") as ans_file:
        result, result_args = test_submission(
            command, in_file.read(), ans_file.read(), args.time_limit)
    print(verdicts[result])
    if result == "AC":
        continue
    if result_args:
        print("\n".join(result_args))
    break
print(f"Result: {verdicts[result]}")
