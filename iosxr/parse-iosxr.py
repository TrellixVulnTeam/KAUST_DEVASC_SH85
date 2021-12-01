import argparse
import json
import yaml

def processFile(jsonFile):
    with open(jsonFile,'r') as json_file:
        jsonObj = json.load(json_file)
        for c in jsonObj["Response"]["Get"]["Operational"]["Controllers"]["ControllerDescriptionTable"]["Controller"]:
            controllerName = c['Controller']
            state = c['State']
            print(f'{controllerName}\t{state}')

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFile", help="JSON file to process", type=str)
    args = parser.parse_args()
    print('-------------------------------------------------------')
    processFile(args.jsonFile)
    print('-------------------------------------------------------')
    print(f'File {args.jsonFile} was successfully processed.')
