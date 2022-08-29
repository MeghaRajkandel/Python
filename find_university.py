import requests
import json
un=input("Enter a country :")
re=requests.get(f"http://universities.hipolabs.com/search?country={un}")
content= re.text
content_json = json.loads(content)
# print(content_json("comme"),content_json.get("length"))
# print(content_json)
for i in content_json :
    print(i)
    
