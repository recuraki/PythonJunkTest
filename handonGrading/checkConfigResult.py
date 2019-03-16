from datetime import datetime
from typing import List, Dict, Tuple


class checkConfigResultData():
    results: list = []
    timeStart: datetime = None
    timeEnd: datetime = None
    status: str = None
    judgeCounter: Tuple[int, int] = None

    def __init__(self):
        self.status = "created"
        self.timeStart = datetime.now()

    def push(self, inputresult: Dict, timeStart: datetime=None, timeEnd: datetime=None):
        self.judgeCounter = self.judgeCount(inputresult)
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

    def push(self, id: str, inputResult: dict):
        self.result[id].append(inputResult)