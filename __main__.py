import requests, json
from PIL import Image

def main():
	#Load current API keys
	with open('Keys.json','r') as file:
		keys = json.load(file)
	#Greet User
	print("Welcome to Python API Wrapper.")
	print("	Available Commands: ")

	APOD = get_APOD(keys['NASA'])
	
	for key in APOD.keys():
		print(key+': '+APOD[key])

	
def get_APOD(NASA_key):
	print('Getting Astronomy Photo of the Day...')
	r = requests.get('https://api.nasa.gov/planetary/apod'+'?api_key='+NASA_key)
	print("Request status code " + str(r.status_code))
	APOD = r.json()
	return APOD

def add_key(key, value):
	with open('Keys.json','r') as file:
		keys = json.load(file)
	
	keys[key] = value

	with open('Keys.json', 'r') as file:
		json.dump(keys, file)

def remove_key(key):
	with open('Keys.json','r') as file:
		keys = json.load(file)
	
	del keys[key]

	with open('Keys.json', 'r') as file:
		json.dump(keys, file)

if __name__=='__main__':
	main()