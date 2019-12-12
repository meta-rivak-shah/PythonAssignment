def createFunctionName(functionName):
    createdFunction = ""
    for i in functionName:
        if(i is functionName[0]):
            createdFunction = createdFunction + i.lower()
        elif(i is not " "):
              createdFunction = createdFunction + i
    return createdFunction