import requests
import json
import wget


NASA_API_KEY="YX9c6p7NC3aOpJZVEdirYjSShn9BJY8FvWkhG9DZ"
LAT=32.790760
LON=97.346127
CLOUD_SCORE=True

#URL="https://api.nasa.gov/planetary/earth/imagery/?lon=97.346127&lat=32.790760&cloud_score=True&api_key=" + NASA_API_KEY

URL="https://api.nasa.gov/planetary/earth/imagery/"
PARAMS = {'lon':LON, 'lat':LAT, 'cloud_score':CLOUD_SCORE, 'api_key':NASA_API_KEY}

print("Requesting image url.")
response_image_details = requests.get(url = URL, params = PARAMS)

if response_image_details.status_code==200:
  print("received valid reponse from server")
  request_json=json.loads(response_image_details.text)
  print("downloading image from server")
  #print(request_json['url'])
  #wget.download(request_json['url'])
  response_image=requests.get(request_json['url'])
  print("saving file")
  with open('image.jpg', 'wb') as f:
    f.write(response_image.content)
else:
  print("Error: getting valid response from the server")
