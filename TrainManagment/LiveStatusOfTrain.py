from util import createFunctionName
from TrainManagmentSystem import TrainManagmentSystem

#list used to store object of all train data

trainOperation = {1:"Train Route" , 2:"Train Between Station" , 3:"Train NameOrNumber" , 4:"Fair Enquiry"}

#for loop is used to show all train operations
for key , operationName in  trainOperation.items():
    print(str(key)+ "*****" +operationName)

operationInput = 0
trainAppObject = TrainManagmentSystem()
while(operationInput != -1):
    try:
        operationInput = int(input("Enter operation number =>"))
        if(trainOperation.setdefault(operationInput , "Not Found") is not "Not Found"):
             getattr(trainAppObject,createFunctionName(trainOperation.get(operationInput)))()
        elif(operationInput == -1):
            print("You are exit from app")
        else:
            print("Enter Valid opertaion")
    except Exception:
        print("your Operation is invalid insert valid number")
