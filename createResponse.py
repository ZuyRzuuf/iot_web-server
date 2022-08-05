import json

def createResponse(dataMock: dict) -> dict:
    try:
        templateFile = open("response.json", "r")
    except:
        print("Response template is kept in response.json file, please add them there!")
        raise
        
    responseTemplate = json.load(templateFile)
    templateFile.close()
    
    for k, v in responseTemplate.items():
        if k in dataMock:
            responseTemplate.update({k:dataMock[k]})
    
    return responseTemplate
