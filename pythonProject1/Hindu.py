# # import requests
# #
# # url = "https://the-hindu-national-news.p.rapidapi.com/news/23"
# #
# # headers = {
# # 	"x-rapidapi-key": "395fe02882msha49d5c47032d750p1a6f36jsn249dcd8ef479",
# # 	"x-rapidapi-host": "the-hindu-national-news.p.rapidapi.com"
# # }
# #
# # response = requests.get(url, headers=headers)
# #
# # # print(response.json())
# # print(response.status_code)
#
# # import http.client
# #
# # conn = http.client.HTTPSConnection("the-hindu-national-news.p.rapidapi.com")
# #
# # headers = {
# #     'x-rapidapi-key': "395fe02882msha49d5c47032d750p1a6f36jsn249dcd8ef479",
# #     'x-rapidapi-host': "the-hindu-national-news.p.rapidapi.com"
# # }
# #
# # conn.request("GET", "/news/23", headers=headers)
# #
# # res = conn.getresponse()
# # data = res.read()
# #
# # print(data.decode("utf-8"))
#
import http.client

conn = http.client.HTTPSConnection("google-news13.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "395fe02882msha49d5c47032d750p1a6f36jsn249dcd8ef479",
    'x-rapidapi-host': "google-news13.p.rapidapi.com"
}

conn.request("GET", "/business?lr=en-US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# import http.client
# import json
#
# # Establishing a connection to the API
# conn = http.client.HTTPSConnection("india-today-unofficial.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-key': "395fe02882msha49d5c47032d750p1a6f36jsn249dcd8ef479",
#     'x-rapidapi-host': "india-today-unofficial.p.rapidapi.com"
# }
#
# # Sending the GET request to fetch India news
# conn.request("GET", "/news/India", headers=headers)
#
# # Getting the response
# res = conn.getresponse()
#
# # Reading the response data
# data = res.read()
#
# # Decoding the response to a string
# response_json = data.decode("utf-8")
#
# # Printing the raw JSON response (optional)
# print(response_json)
#
# # Saving the data to a JSON file
# with open('IndiaToday_news_data.json', 'w') as json_file:
#     # Convert string to JSON and write it to a file
#     json.dump(json.loads(response_json), json_file, indent=4)
#
# print("Data has been stored in 'IndiaToday_news_data.json'")

import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-11-19&'
       'sortBy=popularity&'
       'apiKey=82ae1a6402f14af19e76a11d95ff2017')

response = requests.get(url)

print (response.json())