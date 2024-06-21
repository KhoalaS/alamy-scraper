from PIL import Image
import argparse
from urllib.request import urlopen
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Alamy downloader")
    parser.add_argument("FILE", help="file with links to download")
    parser.add_argument("OUTPUT_DIR", default=os.getcwd(), help="output directory")

    args = parser.parse_args()

    outdir = args.OUTPUT_DIR
    if outdir[-1] == "/" or outdir[-1] == "\\":
        outdir = outdir[0:-1]
    
    try:
        os.mkdir(outdir)
    except:
        pass

    f = open(args.FILE)

    for line in f:
        spl = line.split(sep="|", maxsplit=1)
        file = spl[0]
        name = spl[1].strip()
        print("processing", file)
        img = Image.open(urlopen(file))

        s = img.size
        print(s)

        region = img.crop((0, 0, s[0], s[1]-90))

        region.save("{}/{}.jpg".format(outdir, name))
        break
