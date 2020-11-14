import re, os, base64, sys
from random import choice

ID_size = 32

def getID():
    return "".join([choice("0123456789") for _ in range(ID_size)])

def decodeMHT(filename):
    fp = open(filename, 'r')
    content = fp.read()

    boundary = re.compile("--=+NextP.*\n")
    locationFieldRE = re.compile("Content-Location: (.*)\n")

    try:
        os.mkdir("out")
    except Exception as e:
        pass

    parts = boundary.split(content)

    for part in parts:
        print(part)
        print()
        print("!" * 64)
        print()
        if "Content-Transfer-Encoding: base64" in part:
            location = locationFieldRE.search(part).group(1).strip()
            body = None
            for line in part.splitlines():
                if body != None:
                    body += line
                    continue
                if line.strip() == "":
                    body = ""
            of = open(os.path.join("out", location), "w")
            value = base64.b64decode(body)
            of.write(value)
            of.sclose()


