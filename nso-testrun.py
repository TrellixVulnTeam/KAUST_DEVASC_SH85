import requests
import json

def updateInterfaceDecription(interfaceID, description):
    url = f"http://172.17.237.21:8080/restconf/data/devices/device=pe-xr/config/tailf-ned-cisco-ios-xr:interface/\"TenGigE={interfaceID}\""

    payload = json.dumps({
    "tailf-ned-cisco-ios-xr:TenGigE": {
        "id": f"{interfaceID}",
        "description": f"{description}"
    }
    })
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46YWRtaW4='
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(f"Interface {interfaceID} was successfully updated.")


updateInterfaceDecription("0/0/0/6", "This was modified by PYTHON.")
updateInterfaceDecription("0/0/0/7", "This was modified by PYTHON.")
updateInterfaceDecription("0/0/0/14", "This was modified by PYTHON.")
updateInterfaceDecription("0/0/0/15", "This was modified by PYTHON.")
