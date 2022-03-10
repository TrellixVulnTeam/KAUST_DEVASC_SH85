import base64
import requests
import json

from sqlalchemy import update

def encodeBasicAuthentication(username, password):
    """This method prepares base64 encoded basic string"""
    auth_type = 'Basic'
    creds = f"{username}:{password}"
    b_creds = bytes(creds, 'utf-8')
    creds_b64 = base64.b64encode(b_creds).decode('utf-8')
    header = f"Basic {creds_b64}"
    return header

def updateInterfaceDescription(interfaceType: str, interfaceId: str, description: str):
    username = 'cisco'
    password = 'cisco'
    url = "https://10.0.0.1:443/restconf/data/Cisco-IOS-XE-native:native/interface/\"@interfaceType=@interfaceId\""
    url = url.replace("@interfaceType", interfaceType)
    url = url.replace("@interfaceId", interfaceId)
    payload = "{\r\n    \"Cisco-IOS-XE-native:@interfaceType\": {\r\n        \"name\": \"@interfaceId\",\r\n        \"description\": \"@description\"           \r\n        }\r\n    }\r\n}"
    payload = payload.replace("@interfaceType", interfaceType)
    payload = payload.replace("@interfaceId", interfaceId)
    payload = payload.replace("@description", description)
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Authorization': f'{encodeBasicAuthentication(username, password)}'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload, verify=False)
    print(f"Updated {interfaceType}{interfaceId}.")

i = 1
while True:
    updateInterfaceDescription("GigabitEthernet",f"1/0/{i}", "This is python generated description, NOW.")
    i += 1
    if(i>48):
        break
