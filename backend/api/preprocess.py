# lol no working parser on the net for the mhtml 
from string import ascii_lowercase, ascii_uppercase
import re
import base64
import os

j = 0 


base64chars = ascii_lowercase + ascii_uppercase + "0123456789+/="
keywords = ['Content-Type', 'Content-ID', 'Content-Transfer-Encoding', 'Content-Location', "Content-Transfer-Encoding"]
supported_extensions = ["jpg", "jpeg", "png"]

def preprocess_base64(data):
    pre = []
    for el in data:
        if el in base64chars:
            pre.append(el)
    return "".join(pre)

def save_images(file):
    global i, j
    f = open(file, "r").read()
    lines = [line.strip() for line in f.split("\n")]
    boundary = [line for line in lines if line.startswith('boundary')]
    pattern = boundary[0].split("=")[1][1:-1]
    content = f.split(pattern)

    content_parsed = []

    for c in content:
        if "Content-Type" in c.strip():
            content_parsed.append(c.strip())

    header = content_parsed[0]

    parsed = []
    img_data = []
    try:
        os.mkdir(f"images_{j}")
    except Exception as e:
        pass

    i = 0  
    for c in content_parsed[1:]:
        config = {}
        lines = c.split("\n")
        data_content = []
        for l in lines:
            cnt = True
            for keyword in keywords:
                if  (l.strip()).startswith(keyword):
                    config[keyword] = ((l.strip()).split(":")[1]).strip()
                    cnt = False
            if cnt:
                data_content.append(l)

        data = "\n".join(data_content)


        if config["Content-Type"].startswith("image"):
            ext = ""
            for e in supported_extensions:
                if config["Content-Type"].endswith(e):
                    raw = base64.b64decode(preprocess_base64(data))
                    img_handle = open(f"images_{j}/img{i}.{e}", "wb")
                    img_handle.write(raw)   
                    i += 1
                    break

        config["data"] = data
        parsed.append(config)
    j += 1
    return i