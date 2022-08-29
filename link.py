import requests
import json
for i in range(10):
    re = requests.get("https://catfact.ninja/fact")
    content = re.text
    content_json = json.loads(content)
    print(content_json.get("fact"),content_json.get("length"))

    