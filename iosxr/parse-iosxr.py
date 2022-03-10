import argparse
import json
from py import process
import yaml


def processFile(jsonFile):
    device = 'ASR-1'
    segment = 'Controller'
    contents = ''
    #parse JSON from device
    with open(jsonFile,'r') as json_file:
        jsonObj = json.load(json_file)
        for c in jsonObj["Response"]["Get"]["Operational"]["Controllers"]["ControllerDescriptionTable"]["Controller"]:
            controllerName = c['Controller']
            state = c['State']
            contents += f'{device}\t{segment}\t{controllerName}\t{state}\n'
            print(f'{device}\t{segment}\t{controllerName}\t{state}\n')
    #save the file
    with open("parsedContent.txt", "w") as f:
        f.write(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonFile", help="JSON file to process", type=str)
    args = parser.parse_args()
    print('-------------------------------------------------------')
    processFile(args.jsonFile)
    print('-------------------------------------------------------')
    print(f'File {args.jsonFile} was successfully processed.')
