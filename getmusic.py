#!/usr/bin/env python
import argparse
import subprocess
import uuid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get some music.')
    parser.add_argument('url', type=str)
    parser.add_argument('-t', '--title', type=str)
    parser.add_argument('-a', '--artist', type=str)
    parser.add_argument('-b', '--album', type=str)

    args = parser.parse_args()

    filename = args.artist + " - " + args.title + ".m4a"
    tempname = str(uuid.uuid4())

    subprocess.call(["youtube-dl", "-f", "140", "-o", tempname, args.url])
    subprocess.call(["ffmpeg", "-i", tempname, "-c:a", "copy", filename])
    subprocess.call(["rm", tempname]);

    atomic_call = ["atomicparsley", filename, "--overWrite"]

    if args.artist:
        atomic_call += ["--artist", args.artist]

    if args.title:
        atomic_call += ["--title", args.title]

    if args.album:
        atomic_call += ["--album", args.album]

    subprocess.call(atomic_call)

    print "Music saved as: " + filename
