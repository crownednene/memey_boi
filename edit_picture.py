# editpicture.py

from PIL import Image, Image, ImageDraw, ImageFont
import os, sys, random
from dotenv import load_dotenv

from imgurpython import ImgurClient
import imgur_downloader
#from google_images_search import GoogleImagesSearch

load_dotenv()

CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('IMGUR_ACCESS_TOKEN')
REFRESH_TOKEN =os.getenv('IMGUR_REFRESH_TOKEN')
imgur_client = ImgurClient(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, REFRESH_TOKEN)

path = os.getcwd()

#DEV_KEY = os.getenv('GOOGLE_DEV_API_KEY')
#PROJECT_KEY = os.getenv('GOOGLE_CX_KEY')
#gis = GoogleImagesSearch(DEV_KEY, PROJECT_KEY)

#define search params (for google custom search):
#_search_params = {
#	'q': 'pete buttigieg',
#	'fileType': 'jpg|gif|png'
#}


def find_image():
	os.chdir(path + '/imageDownload/image')
	clear_folder()

#	the google custom image search way of doing it
#	gis.search(search_params=_search_params, path_to_dir = path + '/imageDownload/image', width=500, height=500)

#	i = 1
#	for file in os.listdir():
#		src = file
#		dst = "image.png"
#		os.rename(src,dst)
#		i+=1
	
#	the imgur api way of doing it
	items = imgur_client.gallery_search('#'+'petebuttigieg', advanced=None, sort='time', window='all', page=0)

	i=1
	for item in items:
		if i < 3:
			imgur_downloader.ImgurDownloader(item.link, path + '/imageDownload/image', 'image'+ str(i), True).save_images()
			i+=1
		else:
			break


def clear_folder():
	os.chdir(path + '/imageDownload/image')
	i = 1
	for file in os.listdir(): 
		if file.startswith('image'):
			os.remove(file)
			i+=1


def write_blank():
	im = Image.new('RGBA', (800, 800), 'white')
	draw = ImageDraw.Draw(im)
	fontsFolder = 'Library/Fonts'
	comicSansFont = ImageFont.truetype(os.path.join(fontsFolder, 'comicz.ttf'), 50)

	draw.text((320, 350), 'Nudes', fill=(0, 0, 0), font=comicSansFont)
	im.save('text.png')

def quinns_birthday():
	k = random.randrange(21)
	randomButt = str(k) + '.jpg'

	r = random.randrange(256)
	g = random.randrange(256)
	b = random.randrange(256)

	os.chdir(path + '/imageDownload/buttigieg')
	hbButt = Image.open(randomButt)
	draw = ImageDraw.Draw(hbButt)
	fontsFolder = 'Library/Fonts'
	comicSansFont = ImageFont.truetype(os.path.join(fontsFolder, 'comicz.ttf'), 50)

	draw.text((100, 100), "HAPPY BIRTHDAY QUINN", fill=(r, g, b), font=comicSansFont)
	hbButt.save('generatedButt.jpg')