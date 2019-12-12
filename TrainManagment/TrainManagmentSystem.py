from datetime import datetime
import requests , json
from RouteModel import Routes
from TrainClassess import TrainClass
from TrainRunWeekDays import TrainRunWeekDays
class TrainManagmentSystem():
    #constant Varible which will not chnage
    __API_KEY  = "lre5y5cdj8"
    def trainRoute(self):
         #insert the train number
        train_number = (input("Enter Train Number ->"))
        #current Date
        current_date = datetime.datetime.now()
        #change the formate of datetime to date
        current_date = current_date.strftime("%d-%m-%Y")
        #Complete url of API
        COMPLETE_URL = "https://api.railwayapi.com/v2/route/train/"+train_number+"/apikey/"+self.__API_KEY+"/"
        trainData = requests.get(COMPLETE_URL)
        result = trainData.json() 
        routesList = []
        classList = []
        trainRunsStatusList = []
        statioNameSwitchCaseDist = {}
        #loop to extract route from jasno data
        if(len(result) > 0):
            for i in result["route"]:
                routesList.append(Routes(str(i.get("no")) , str(i.get("distance")) ,str(i.get("scharr")) , str(i.get("station").get("code")) , 
                str(i.get("station").get("name")) , str(i.get("schdep")) , str(i.get("day"))))
                statioNameSwitchCaseDist[(i.get("no"))] = str(i.get("station").get("name"))
                print("Number ->"+str(i.get("no")))
                print("distance->"+str(i.get("distance")))
                print("SOourceTime->"+str(i.get("scharr")))
                print("stationCode->"+str(i.get("station").get("code")))
                print("stationName->"+str(i.get("station").get("name")))
                print("DestinationTime->"+str(i.get("schdep")))
                print("Day->"+str(i.get("day")))
                print("******************************************************************")

            #loop to extract train class from jason data
            for i in result["train"]["classes"]:
                classList.append(TrainClass(i.get("code") , i.get("available") , i.get("name")))
                print("Type -> "+i.get("code"))
                print("available -> "+i.get("available"))
                print("name -> "+i.get("name"))
                print("******************************************************************")

            #loop to extract train avaliblity in weekdays in jason data
            for i in result["train"]["days"]:
                trainRunsStatusList.append(TrainRunWeekDays(i.get("code") , i.get("runs")))
                print("WeeKDay ->"+i.get("code"))
                print("available ->"+i.get("runs"))
                print("******************************************************************")
            print("Train Name ->"+result["train"]["name"])

            for key , value  in statioNameSwitchCaseDist.items():
                print(str(key)+"-----"+value)
            print("Enter -1 to exit from loop")
            userInput = 0
            while (userInput != -1):    
                try:
                    userInput = int(input("Enter Station sequence to get Imfomation :-"))
                    for routes in routesList:
                        if (routes.getStationName() is statioNameSwitchCaseDist.setdefault(userInput,"NotFound")):
                            print("No->"+str(routes.getNo()))
                            print("Distance->"+str(routes.getDistance()))
                            print("Arrive day->"+str(routes.getDays()))
                            print("Reach Time ->"+str(routes.getSourceTime()))
                            print("Station Code"+str(routes.getStationCode()))
                            print("Station Name"+str(routes.getStationName()))
                            break
                except Exception:
                    print("Enter Only integer value")
        else:
            print("No Data Found")


    def trainBetweenStation(self):
        source = input("Enter the source city =: ")
        destination = input("Enter destination city =: ")
        date = datetime.now().strftime("%d-%m-%Y")
        print(date)
        completeUrl = "https://api.railwayapi.com/v2/between/source/"+source+"/dest/"+destination+"/"+date+"/apikey/"+self.__API_KEY+"/"
        print(completeUrl)
        result = requests.get(completeUrl)
        data = result.json()
        print(data)

    def trainNameOrNumber(self):
        trainNameOrNumber = input("Enter train name or number to get Imformation \n")
        completeUrl = "https://api.railwayapi.com/v2/name-number/train/"+trainNameOrNumber+"/apikey/lre5y5cdj8/"
        trainNameOrNumber = requests.get(completeUrl)
        trainNameOrNumberInJson  = trainNameOrNumber.json()
        print("Train-Name ->"+trainNameOrNumberInJson.get("train").get("name"))
        trainRunsStatusList=list()
        #loop to extract the avalability of train in week
        for i in trainNameOrNumberInJson.get("train").get("days"):
            trainRunsStatusList.append(TrainRunWeekDays(i.get("code") , i.get("runs")))

        #loop is used to find the all class in train
        classList = list()
        for i in trainNameOrNumberInJson.get("train").get("classes"):
             classList.append(TrainClass(i.get("code") , i.get("available") , i.get("name")))

        #find the given code exit in classtrainRunsStatusListList if then show all details
        userInputCode = input("Enter the Days in Code form EG:(MON,TUE,WED,THU,FRI,SAT,SUN) -:")
        for i in trainRunsStatusList:
            if(i.getCode() == userInputCode):
                print("Code ->",i.getCode())
                print("RunningStatus"+i.getRuns())
                break
    def fairEnquiry(self):
        #insert tclassListhe train number
        train_number = (input("Enter Train Number ->"))
        source = input("Enter the source code =: ")
        destination = input("Enter destination code =: ")
        age = input("Enter your Age ->")
        classCode = input("Enter Class Code Eg:1A,2A,3A,SL")
        date = datetime.now().strftime("%d-%m-%Y")
        print(date)
        completeUrl = "https://api.railwayapi.com/v2/fare/train/"+train_number+"/source/"+source+"/dest/"+destination+"/age/"+age+"/pref/"+classCode+"/quota/GN/date/"+date+"/apikey/lre5y5cdj8/"
        #print(completeUrl)
        requestResult = requests.get(completeUrl)
        fairData = requestResult.json()
        for key , value in fairData.get("journey_class").items():
            print(key , "-:" , value)
        print("Total-Price",fairData.get("fare"))
