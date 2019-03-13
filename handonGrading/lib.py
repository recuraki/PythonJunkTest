import pathlib
from pprint import pprint, pformat

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
import yaml
import re

def load_yaml_file(p) -> dict:
    """
    指定されたファイルを開き、YAMLとして辞書を返す
    :param p: ファイルパス
    :return: 辞書
    """
    with open(p, "r+") as fp:
        r = yaml.load(fp)
        return r

def listDirFromDir(path: str) -> list:
    """
    指定されたディレクトリの配下にあるディレクトリをすべてlistとして返す
    :param path:
    :return:
    """
    p = pathlib.Path(path)
    # ディレクトリ配下のディレクトリなもの(is_dir)をすべて取得
    return [x for x in p.iterdir() if x.is_dir()]


def listYamlFromDir(path: str) -> list:
    """
    指定されたパスいかにあるYAMLfileのパスをすべてlistとして返す
    :param path:
    :return:
    """
    p = pathlib.Path(path)
    return list(p.glob("**/*.yaml"))


def loadYamlFromDir(path: str) -> list:
    """
    ディレクトリ配下にあるすべてのyamlファイルのyamlを読み込みtestAllとしてloadして返す
    """
    testsAll = []
    for filename in listYamlFromDir(path):
        d = load_yaml_file(filename)
        for test in d:
            testsAll.append(test)
        logger.info("LOAD file: {0}".format(filename))
    return testsAll


if __name__ == "__main__":
    logger.info(pformat(listDirFromDir("./scenario")))
    logger.info("---")
    logger.info(pformat(listYamlFromDir("./scenario")))
    logger.info("---")
    logger.info(pformat(listYamlFromDir("./scenario/test_cisco")))
    logger.info("---")
    logger.info(pformat(loadYamlFromDir("./scenario/test_cisco")))
    logger.info("---")
    logger.info(pformat(loadYamlFromDir("./scenario")))

