# from html import escape
from jinja2 import Environment, FileSystemLoader
from pprint import pprint
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)


class SimpleTextLineTestDecorator:
    env = None
    tpl = None

    def __init__(self):
        # Jinja2エンジンの初期化
        self.env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
        self.env.filters["filter_positive"] = self.j2_filter_positive
        self.env.filters["filter_negative"] = self.j2_filter_negative
        self.env.filters["classname"] = self.j2_classname
        # Jinja2テンプレートのロード
        self.tpl = self.env.get_template('templ/result.templ')

    def render(self, res=[]):
        # Render。基本的にそのまま吐き出す。
        pprint("render")
        pprint(res)
        final_pass = True
        for n in res:
            pprint("hogehoge")
            pprint(n)
            final_pass = final_pass & n["header"]["pass"]
        html = self.tpl.render(data=res, final_pass = final_pass)
        return html

    @staticmethod
    def j2_filter_date(date):
        pass

    @staticmethod
    def j2_filter_positive(d):
        return list(filter(lambda x: x[1] == "p", d))

    @staticmethod
    def j2_filter_negative(d):
        return list(filter(lambda x: x[1] == "n", d))

    @staticmethod
    def j2_classname(d):
        if d[0] == True:
            return "rulecorrect"
        if d[0] == False:
            return "ruleincorrect"
        return "rulenoeval"

    @staticmethod
    def j2_classname_nodes(d):
        if d == True:
            return "nodescorrect"
        return "nodesincorrect"
