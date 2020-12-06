import requests 
import json
# api-endpoint 
API_ENDPOINT = "http://0.0.0.0:5000/lists"
  
  
# defining a params dict for the parameters to be sent to the API 
data = {'sentence_tokens':[[0, 1, 1, 0],[2, 3 , 4, 1]]} 
data_json= json.dumps(data)
#print(data_json)
  
# sending get request and saving the response as response object 
r = requests.post(url = API_ENDPOINT, data = data_json) 
  
# extracting data in json format 
data = r.json() 

print(data)
print(data['resp'])