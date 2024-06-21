from PIL import Image
import argparse
from urllib.request import urlopen
import os
import time
from tqdm import tqdm

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Alamy downloader")
    parser.add_argument("FILE", help="file with links to download")
    parser.add_argument("OUTPUT_DIR", default=os.getcwd(),
                        help="output directory")
    parser.add_argument("-t", type=float, default=1.0,
                        help="delay in seconds between downloads, default is 1 second")

    args = parser.parse_args()

    outdir = args.OUTPUT_DIR
    if outdir[-1] == "/" or outdir[-1] == "\\":
        outdir = outdir[0:-1]

    try:
        os.mkdir(outdir)
    except:
        pass

    f = open(args.FILE)
    lines = f.readlines()

    for line in tqdm(lines):
        spl = line.split(sep="|", maxsplit=1)
        file = spl[0]
        full_name = spl[1].strip()

        spl = full_name.split(" - ")
        name = ""
        if len(spl) == 2:
            name = spl[0].strip()
        else:
            if full_name.endswith("Stock Photo"):
                name = full_name[0:-12].strip()

        img = Image.open(urlopen(file))

        s = img.size
        region = img.crop((0, 0, s[0], s[1]-90))

        region.save("{}/{}.jpg".format(outdir, name))
        time.sleep(args.t)
