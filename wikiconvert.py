#!/usr/bin/env python

import os
import re

wikipath = os.path.join(os.path.expanduser('~'), 'wiki/vimwiki')
os.chdir(wikipath)

def getwikifiles():
    wikifiles = []
    for (root, _, files) in os.walk(wikipath):
        for file in files:
            if re.search(r".md$", file):
                wikifiles.append(os.path.join(root, file))
    return wikifiles

def getspacefiles():
    spacefiles = []
    for filename in getwikifiles():
        if " " in filename:
            spacefiles.append(filename)
    return spacefiles


def fixname(filename):
    newname = filename.replace(" ", "_")
    os.rename(filename, newname)
    oldlink = re.search(r".*/(.*)\.md$", filename)
    if not oldlink:
        return
    oldlink = oldlink.group(1)
    newlink = oldlink.replace(" ", "_")
    for file in getwikifiles():
        with open(file, 'r+') as f:
            text = f.read()
            text = text.replace(oldlink, newlink)
            f.seek(0)
            f.write(text)
            f.truncate()
            f.close()
    print("newlink: " + newlink)

for i in getspacefiles():
    print(i)
    fixname(i)




