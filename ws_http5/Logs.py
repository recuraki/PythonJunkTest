"""
Logs
ログの記録を行うモジュール
"""
from pprint import pprint
import datetime

class Log(object):
    seq: int = 0
    limitCount: int = 255
    buffer: list = []

    def dp(self, log):
        if self.isdebug:
            pprint(log)

    def __init__(self, debug: bool=False, limitCount: int=256):
        self.isdebug = debug
        self.limitCount = limitCount
        self.reset_log()

    def set_sequence(self, seq: int) -> bool:
        """
        ログシーケンスの初期化(reset時に使う)
        :param seq:
        :return:
        """
        # 設定するシーケンスが限界値以上の場合は異常とする
        if seq > self.limitCount:
            raise False
        self.seq = seq
        return True

    def get_sequence(self) -> int:
        return self.seq

    def reset_log(self) -> bool:
        """
        ログバッファの初期化
        :return:
        """
        self.buffer = []
        self.set_sequence(0)
        return bool

    def get_logs(self) -> list:
        return self.buffer

    def write_log(self, msg: str, category: str = "default") -> bool:
        """
        ログ記録
        :param msg: ログ本文の完全なる文字列
        :param category:
        :return:
        """
        if self.seq < self.limitCount:
            self.buffer.append({"seq": self.seq,
                                "category": category,
                                "msg": msg,
                                "date": datetime.datetime.now(),
                                })
            self.seq = self.seq + 1
            return True
        else:
            self.dp("log limit")
            return False

    def count_logs(self) -> int:
        """
        ログの数量を得る
        :return:
        """
        return len(self.buffer)

    def read_log_by_index(self, index: int) -> dict:
        """
        index番号に対応するログの取得
        :param index:
        :return:
        """
        # indexが不正の場合はエラーを返す
        if index > self.count_logs() or index < 0:
            raise IndexError

        return self.buffer(index)

    def dumpLog(self):
        """
        ログをテキストでdumpする
        :return:
        """
        out = []
        for d in self.buffer:
            out = "[{0}:{1}] {2}".format(d["seq"], d["category"], d["msg"])
        return "\n".join(out)


if __name__ == "__main__":
    l = Log()
    l.write_log("test")
