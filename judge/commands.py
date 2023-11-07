import os


commands = {
    # "posix"   - For Mac and Linux
    # "nt"      - For Windows
    "py": {
        "posix": "python3",
        "nt": "python"
    }
    # ...
}


def find_command(lang):
    result = commands[lang]
    if isinstance(result, str):
        return result
    return result[os.name]
