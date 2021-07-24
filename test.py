import requests
BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "trending_language")

print(" number of languages :", response.json()['languages_count'])
for i in range(len(response.json()['languages'])):
    print(response.json()['languages'][i], sep = "\n")
    
# your can get the results by running the scripts 
# or you can 
# run on your localhost : http://127.0.0.1:5000/trending_language
