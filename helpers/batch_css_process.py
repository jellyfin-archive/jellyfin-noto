newlines = []

def addwoff(path):
    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "url(fonts/notosans/woff2/" in line:
            if ("woff2" in line):
                filepath = line.split("url(fonts/notosans/woff2/")
                name = filepath[1]
                name = name.replace("woff2", "woff")
                name = name.replace("\n", "")
                line = line.replace(";", ",\n    url(fonts/notosans/woff/" + name)
        newlines.append(line)

    with open(path,"w") as f:
        for line in newlines:
            f.write(line)

def removewoff(path):
    with open(path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "format('woff2')," in line:
            line = line.replace(",", ";")
        if "format('woff')" in line:
            continue
        newlines.append(line)

    with open(path,"w") as f:
        for line in newlines:
            f.write(line)

while True:
    try:
        path = input("Type the path of the file to process: ")
        newlines.clear()
        removewoff(path)
        newlines.clear()
    except KeyboardInterrupt:
        break