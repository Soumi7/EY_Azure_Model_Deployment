import requests 
import json
# api-endpoint 
API_ENDPOINT = "http://0.0.0.0:80/predict_api"
  
  
# defining a params dict for the parameters to be sent to the API 
#data = [[0, 1, 1, 0],[2, 3 , 4, 1]]

data = [[  101, 19719,  2005,  1996,  2005,  7077,   102,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,    0,     0,     0,
      0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0]]

#data_json= json.dumps(data)
#print(data_json)
  
# sending get request and saving the response as response object 
r = requests.post(url = API_ENDPOINT, json = data) 
  
# extracting data in json format 
data = r.json() 



print(r)
print(data)
print(data['results'])