import requests, json
from PIL import Image
from pathlib import Path

def main():
	#Load current API keys
	with open('Keys.json','r') as file:
		keys = json.load(file)
	#Greet User
	print("Welcome to Python API Wrapper.")
	command = {}
	print("	Available Commands: ")
	print("	1. Astronomy Photo of the Day")
	command['1'] = get_apod
	print("	2. Download Perseverance Photo Album")
	command['2'] = perseverance	
	command[input("Enter Choice: ")](keys['NASA'])
	
def get_apod(NASA_key):
	print('Getting Astronomy Photo of the Day...')
	r = requests.get('https://api.nasa.gov/planetary/apod'+'?api_key='+NASA_key)
	print("Request status code " + str(r.status_code))
	apod = r.json()
	for key in apod.keys():
		print(key+': '+apod[key])
	return apod

def perseverance(NASA_key):
	print("Perseverance photos")
	sol = int(input("(1- 18) SOL: "))
	path ='SOL'+str(sol).zfill(2)+'/'
	Path(path).mkdir(parents=True, exist_ok=True)
	r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/photos?sol='+str(sol)+'&api_key='+NASA_key)
	photo_directory = r.json()
	n = len(photo_directory["photos"])
	print("Photos: "+str(n))
	for page in range(0, n):
		image_url = photo_directory['photos'][page]["img_src"]
		image = Image.open(requests.get(image_url,stream = True).raw)
		image.save(path+'/SOL-'+str(sol).zfill(2)+'page-'+str(page).zfill(len(str(n)))+'.jpg')
	return 

if __name__=='__main__':
	main()