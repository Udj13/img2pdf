import argparse
from PIL import Image
from time import strftime,localtime

baseheight = 3000

parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='*')
args = parser.parse_args()

imagelist = []
# args.filename = ['15.jpeg']

if args.filename is not None:
    for filename in args.filename:
        image = Image.open(filename)

        wpercent = (baseheight / float(image.size[1]))
        wsize = int((float(image.size[0]) * float(wpercent)))
        imageResized = image.resize((wsize, baseheight), Image.ANTIALIAS)
        imagelist.append(imageResized)
        print(f'-- {filename}')

imageResized.save(f'Готовое {strftime("%Y-%m-%d %H-%M", localtime())}.pdf', save_all=True, append_images=imagelist[1:])
