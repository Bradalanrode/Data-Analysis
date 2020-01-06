import json
import urllib.request as url
import requests as request

# obtain an access key and enter it below
access_key = 'obtainyourownaccesskey'

# I last pulled page 5, change each time
r = request.get('https://api.unsplash.com/search/photos?query=german-shepherd&page=5&per_page=20&client_id={0}'.format(access_key))

# return the json data as python dictionary format
data = r.json()
data.keys()

# details and keys of the first photo
data['results'][0].keys()

# retrieves download link for the first photo
link = data['results'][0]['links']['download']

# download a specific number of german shepherd pictures
# change file_name each time
for i in range(20):
	download_link = data['results'][i]['links']['download']
	file_name = "shepherds{0}".format(i) + ".jpg"
	print(file_name + " has been downloaded")
	url.urlretrieve(download_link, file_name)

