import os

dirName = "woff"
for path, subdirs, files in os.walk(dirName):
    for name in files:
        fullpath = os.path.join(path, name)
        if "woff2" in fullpath:
            os.system("fontforge -script convert.pe " + fullpath)
            os.remove(fullpath)