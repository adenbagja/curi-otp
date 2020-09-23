#code by aden bagja
# importing the requests library 
import requests 
import re  
  
# defining the api-endpoint  
API_ENDPOINT = ""
  

nomor = raw_input("no telp: ")
  
# data to be sent to api 
data = {'user_phone':nomor} 
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 


# extracting response text  
response = r.text 

#regex find otp
match = re.search(r'["]otp.*[}]', response).group()[1:-1]
#menghilangkan " pada response
x = re.sub('"', "", match)
print(x)
