from argparse import ArgumentParser
from pathlib import Path
from importlib.machinery import SourceFileLoader
from commands import find_command
import subprocess


parser = ArgumentParser()
parser.add_argument("submission", type=str,
                    help="Path to the python file to judge")
parser.add_argument("-d", "--dir", type=str,
                    help="Path to directory with input and answer files", default=None)
parser.add_argument("-i", "--in-ext", type=str,
                    help="File extension for input files", default="in")
parser.add_argument("-a", "--ans-ext", type=str,
                    help="File extension for answer files", default="ans")
parser.add_argument("-t", "--time-limit", type=int,
                    help="Time limit in milliseconds", default=None)
parser.add_argument("-r", "--rules", type=str,
                    help="Ignore this unless your problem has special rules", default="")
parser.add_argument("-s", "--show", type=bool,
                    help="Show the testcases you got wrong", default=False)
parser.add_argument("-l", "--lang", type=str,
                    help="Language of the submission", default="py")
parser.add_argument("-e", "--exec", type=bool,
                    help="Submission is an executable file", default=False)
args = parser.parse_args()

verdicts = {
    "AC": "Accepted",
    "WA": "Wrong Answer",
    "TLE": "Time Limit Exceeded",
    "RE": "Runtime Error"
}


def test_submission(cmd, testcase, answer, rules, time_limit=None):
    try:
        solution = subprocess.run(cmd, input=testcase, timeout=time_limit, text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = solution.stdout
    except subprocess.TimeoutExpired:
        return "TLE", []
    except subprocess.CalledProcessError as err:
        return "RE", [err.stderr]
    if not rules.judge(output, answer, testcase):
        verdict_args = [
            f"Input:\n{testcase}"
            f"Received:\n{output}",
            f"Expected:\n{answer}"
        ]
        return "WA", verdict_args
    return "AC", []


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
testcases.sort(key=lambda x: len(x[0].stem))

submission_path = CWD.joinpath(Path(args.submission))
if not args.exec:
    command = f"{find_command(args.lang)} {submission_path}"
else:
    command = submission_path

# Load rules file
judge_module = "rules"
judge_path = Path(__file__).parent.joinpath(Path(f"rules\\{judge_module}.py"))
if args.rules:
    rules_module = f"rules_{args.rules}"
    rules_path = Path(__file__).parent.joinpath(Path(f"rules\\{rules_module}.py"))
    if rules_path.exists():
        judge_module = rules_module
        judge_path = rules_path
rules_file = SourceFileLoader(judge_module, str(judge_path)).load_module()

# Judge solution
result = "WA"
for i in range(len(testcases)):
    in_path, ans_path = testcases[i]
    if args.show:
        print(f"{i + 1}/{len(testcases)}: ({in_path.stem}{in_path.suffix})", end=" ")
    with open(in_path, "r") as in_file, open(ans_path, "r") as ans_file:
        result, result_args = test_submission(command, in_file.read(), ans_file.read(),
                                              rules_file, args.time_limit)
    if args.show:
        print(verdicts[result])
    if result == "AC":
        continue
    if result_args and args.show:
        print("\n".join(result_args))
    break
print(f"Result: {verdicts[result]}")
