from email import header
import requests
import json
user = {
    "name":"sujan",
    "email":"sujan@entechbook.com",
    "gender":"male",
    "status":"active"
}
post = {
    ""
}
header={
    "content-Type":"application/json",
    "Authorization":"Bearer f7bae3a11027622aa634972ff20458c7eb106628180ab420209244abf678b44e"

}

user_data=json.dumps(user)
print(user_data)

re=requests.post("https://gorest.co.in/public/v2/users",data=user_data, headers=header)
print(re.status_code)
print(re.text)