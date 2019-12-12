class TrainRunWeekDays():
    __code = ""
    __runs  = ""

    def __init__(self, code , runs):
        self.__runs = runs
        self.__code = code

    def getRuns(self):
        return self.__runs
    def getCode(self):
        return self.__code