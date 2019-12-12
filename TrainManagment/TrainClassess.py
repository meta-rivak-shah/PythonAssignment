class TrainClass():
    __code = ""
    __available =""
    __name = ""

    def __init__(self,code,available,name):
        self.__code = code
        self.__available = available
        self.name = name
    def getCode(self):
        return self.__code
    def getAvailablity(self):
        return self.__available
    def getName(self):
        return self.__name