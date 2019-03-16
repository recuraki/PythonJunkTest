from datetime import datetime
from typing import List, Dict, Tuple


class checkConfigResultData():
    results: list
    timeStart: datetime = None
    timeEnd: datetime = None
    status: str = None
    judgeCounter: Tuple[int, int] = None

    def __init__(self, inputresult: list, timeStart: datetime=None, timeEnd: datetime=None):
        self.results = inputresult
        self.timeStart = timeStart
        self.timeEnd = timeEnd

    @staticmethod
    def judgeCount(inputResult: Dict):
        countOK = 0
        countNG = 0
        for nodeResult in inputResult:
            for testResult in nodeResult.get("test", []):
                if testResult["is_pass"]:
                    countOK = countOK + 1
                else:
                    countNG = countNG + 1
        return tuple(countOK, countNG)


class checkConfigResult():
    result: Dict[str, List[checkConfigResultData]] = {}

    def push(self, id: str, inputResult: list, timeStart: datetime=None, timeEnd: datetime=None):
        if id not in self.result:
            self.result[id] = list()
        self.result[id].append(checkConfigResultData(inputResult, timeStart, timeEnd))

    def getLastResultById(self, id: str):
        if id not in self.result:
            return None
        return self.result[id][len(self.result[id]) - 1].results

