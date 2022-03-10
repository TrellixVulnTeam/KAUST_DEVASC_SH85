import argparse
import json
import yaml
import base64
import requests

def add(a: int, b: int):
    """This is a simple method that adds a and b"""
    c = a * b
    return c

def doSomething(i:int, j:int):
    x = add(i,j)
    return x

def encodeBasicAuthentication(username, password):
    """This method prepares base64 encoded basic string"""
    auth_type = 'Basic'
    creds = f"{username}:{password}"
    b_creds = bytes(creds, 'utf-8')
    creds_b64 = base64.b64encode(b_creds).decode('utf-8')
    header = f"Basic {creds_b64}"
    return header

def NXExample(username:str, password: str):
    """This is a simple 'show interface brief' example based on NX-OS sandbox"""
    url = "https://sandbox-nxos-1.cisco.com/ins"

    payload = json.dumps({
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "sid",
            "input": "show interface brief",
            "output_format": "json"
        }
        })
    headers = {
        'Authorization': f"{encodeBasicAuthentication(username, password)}",
        'Content-Type': 'application/json'
        }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    jsonObj = json.loads(response.text)
    print(response.text)


if __name__ == "__main__":
    # NX Sandbox credentials
    username = "admin"
    password = "Admin_1234!"
    NXExample(username, password)
    
    # How to construct Basic auth header (see NXExample)
    user = 'admin'
    password = 'I will never tell'
    result = encodeBasicAuthentication(user, password)
    print(f"Authorization header would be: {result}")

    # Some basic testing
    i = 4
    j = 5
    c = doSomething(i,j)
    if c == 8:
        print("We have a match.")
    print(f"Hello world! The number is: {c}")
