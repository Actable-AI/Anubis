# Made by 0sir1ss @ https://github.com/0sir1ss/Anubis
import ast, io, tokenize, os, sys, platform, re, random, string, base64, hashlib, subprocess, requests, glob, base64, time

from pathlib import Path
from regex import F
from Crypto import Random
from Crypto.Cipher import AES

is_windows = True if platform.system() == "Windows" else False

if is_windows:
    os.system("title Anubis @ github.com/0sir1ss/Anubis")

def clear():
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

def pause():
    if is_windows:
        os.system(f"pause >nul")
    else:
        input()

def leave():
    try:
        sys.exit()
    except:
        exit()

def error(error):
    print(red(f"        [!] Error : {error}"), end="")
    pause(); clear(); leave()

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded

def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

def remove_docs(source):
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out

def do_rename(pairs, code):
    for key in pairs:
        code = re.sub(fr"\b({key})\b", pairs[key], code, re.MULTILINE)
    return code

def carbon(code):
    code = remove_docs(code)
    parsed = ast.parse(code)

    funcs = {
        node for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    classes = {
        node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
    }
    args = {
        node.id for node in ast.walk(parsed) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
    }
    attrs = {
        node.attr for node in ast.walk(parsed) if isinstance(node, ast.Attribute) and not isinstance(node.ctx, ast.Load)
    }
    for func in funcs:
        if func.args.args:
            for arg in func.args.args:
                args.add(arg.arg)
        if func.args.kwonlyargs:
            for arg in func.args.kwonlyargs:
                args.add(arg.arg)
        if func.args.vararg:
            args.add(func.args.vararg.arg)
        if func.args.kwarg:
            args.add(func.args.kwarg.arg)

    pairs = {}
    used = set()

    for arg in args:
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[arg] = newname

    for attr in attrs:
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[attr] = newname

    string_regex = r"('|\")[\x1f-\x7e]{1,}?('|\")"

    original_strings = re.finditer(string_regex, code, re.MULTILINE)
    originals = []

    for matchNum, match in enumerate(original_strings, start=1):
        originals.append(match.group().replace("\\", "\\\\"))

    placeholder = os.urandom(16).hex()
    code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

    for i in range(len(originals)):
        for key in pairs:
            originals[i] = re.sub(r"({.*)(" + key + r")(.*})", "\\1" + pairs[key] + "\\3", originals[i], re.MULTILINE)

    cycles = [
        "[   > >                                                                                           ]", 
        "[   > > > >                                                                                       ]", 
        "[   > > > > > >                                                                                   ]", 
        "[   > > > > > > > >                                                                               ]", 
        "[   > > > > > > > > > >                                                                           ]", 
        "[   > > > > > > > > > > > >                                                                       ]", 
        "[   > > > > > > > > > > > > > >                                                                   ]", 
        "[   > > > > > > > > > > > > > > > >                                                               ]", 
        "[   > > > > > > > > > > > > > > > > > >                                                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > >                                                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > >                                                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > >                                               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > >                                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > >                                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >   ]", 
    ]

    i = int(0)

    while True:
        print("\r"+f"        {cycles[i]}", end="")
        i += 1
        if i == len(cycles):
            i = int(0)
        found = False
        code = do_rename(pairs, code)
        for key in pairs:
            if re.findall(fr"\b({key})\b", code):
                found = True
        if found == False:
            break

    replace_placeholder = r"('|\")" + placeholder + r"('|\")"
    for original in originals:
        code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)
    print("\r"+f"        {cycles[len(cycles) -1]}\n\n", end="")

    return code

def anubis(code):
    newcode = "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    newcode += code + "\n"
    classes = ["".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(2, 5))]
    for i in classes:
        newcode += f"class {i}:\n    def __init__(self):\n"
        funcs = ["__"+"".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(8, 20))) for i in range(random.randint(5, 15))]
        for i in funcs:
            newcode += f"        self.{i}()\n"
        for i in funcs:
            newcode += f"    def {i}(self, {', '.join([''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(random.randint(5, 20))) for i in range(random.randint(1, 7))])}):\n        return self.{random.choice(funcs)}()\n"
    return newcode

class Encryption:

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(str(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)


    def write(self, key, source):
        wall = "__ANUBIS_ENCRYPTED__" * 25
        newcode = f"{wall}{key}{wall}"
        for line in source.split("\n"):
            newcode += self.encrypt(line) + wall
        code = f"import ancrypt\nancrypt.load(__file__)\n'''\n{newcode}\n'''"
        return code


source_dir = "/tmp/actableai-app/superset"

def get_url_path(parent, filename):
    return f"{parent}/{filename}"

print("Obfuscating...")
path = os.getcwd()

print(path)

for path in Path(source_dir).rglob('*.py'):
    print(get_url_path(path.parent, path.name))
    with open(path, "r", encoding='utf-8') as f:
        src = f.read()

    # src = anubis(src)
    src = carbon(src)

    with open(path, "w", encoding='utf-8') as f:
        f.write(src)
        f.close()

print(blue("Done"), end="")