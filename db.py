import json
def readDB(filename="db.json"):
    with open(filename, mode="r") as jsonFile:
        data = json.load(jsonFile)
    return data

def writeDB(obj,filename="db.json",old=-1,delete=0):
    with open(filename,mode="r") as jsonFile:
        data = json.load(jsonFile)
        if(old!=-1):
            data.pop(old)
        if(delete==0):
            data.append(obj)
    with open(filename,mode="w") as jsonFile:
        json.dump(data, jsonFile)
