import requests 
  
# api-endpoint 
URL = "http://localhost:80/predict_api"
  
# location given here 
location = "case study"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'sentences':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
#data = r.json() 

print(r.json() )