class Routes():
    __no = ""
    __distance = ""
    __sourceTime = ""
    __stationCode=""
    __stationName = ""
    __destinationTime = ""
    __days = ""

    def __init__(self,no,distance,sourceTime,stationCode,stationName,destinationTime,days):
        self.__no = no
        self.__distance = distance
        self.__sourceTime = sourceTime
        self.__stationCode = stationCode
        self.__stationName = stationName
        self.__destinationTime = destinationTime
        self.__days = days
    def getNo(self):
        return self.__no
    def setNo(self,no):
        self.__no = no
    def getDistance(self):
        return self.__distance
    def setDistance(self,distance):
        self.__distance = distance
    def getSourceTime(self):
        return self.__sourceTime
    def getStationCode(self):
        return self.__stationCode
    def getStationName(self):
        return self.__stationName
    def getDays(self):
        return self.__days