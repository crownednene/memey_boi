# editpicture.py
from google_images_search import GoogleImagesSearch

from PIL import Image, Image, ImageDraw, ImageFont
import os

from dotenv import load_dotenv

load_dotenv()
DEV_KEY = os.getenv('GOOGLE_DEV_API_KEY')
PROJECT_KEY = os.getenv('GOOGLE_PROJECT_KEY')

gis = GoogleImagesSearch(DEV_KEY, PROJECT_KEY)


# define search params:


def find_image():
	gis.search(search_params={'q': 'dog'})

def write_blank():
	im = Image.new('RGBA', (800, 800), 'white')
	draw = ImageDraw.Draw(im)
	fontsFolder = 'Library/Fonts'
	comicSansFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

	draw.text((100, 150), picTex, fill='gray', font=comicSansFont)
	im.save('text.png')