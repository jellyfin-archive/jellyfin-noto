newlines = []

with open("font-faces.css", "r") as f:
    lines = f.readlines()

for key, line in enumerate(lines):
    if "url(fonts/notosans/woff2/" in line:
        if ("woff2" in line):
            filepath = line.split("url(fonts/notosans/woff2/")
            name = filepath[1]
            name = name.replace("woff2", "woff")
            name = name.replace("\n", "")
            line = line.replace(";", ",\n    url(fonts/notosans/woff/" + name)
    newlines.append(line)

with open("font-faces.css","w") as f:
    for line in newlines:
        f.write(line)