import requests 
  
# api-endpoint 
API_ENDPOINT = "http://localhost:80/predict_api"
  
# location given here 
location = "case study"
  
# defining a params dict for the parameters to be sent to the API 
data = {'sentences':["case study"]} 
  
# sending get request and saving the response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting data in json format 
data = r.json() 

print(data)
print(data['predictions'])