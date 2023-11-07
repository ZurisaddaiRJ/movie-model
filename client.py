import requests
body = {
  "Year": 2008,
  "Rating": 10,
  "Votes": 757074,
  "Metascore": 70,
  "Action": 1,
  "Adventure": 0,
  "Aniimation": 1,
  "Biography": 0,
  "Comedy": 1,
  "Crime": 1,
  "Drama": 1,
  "Family": 1,
  "Fantasy": 0,
  "History": 0,
  "Horror": 1,
  "Music": 0,
  "Musical": 0,
  "Mystery": 1,
  "Romance": 1,
  "Sport": 0,
  "Thriller": 1,
  "War": 0,
  "Western": 0,
  "Success": 1
}

response = requests.post(url= 'http://127.0.0.1:8000/score', json=body)
print(response.json())