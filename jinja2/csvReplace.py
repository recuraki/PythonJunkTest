"""
usage:
python3.11 csvReplace.py -t test.templ -c test.csv


hostname {{ hostname }}
int gi 0
 ip address {{ ipaddr }} 255.255.255.0
というテンプレートに
# hostname,ipaddr
router1,192.168.0.1
router2,192.168.0.2
を入力すると
output/router1 に jinja2 renderした出力を吐きます。

この時、csvの1つめの要素がoutput/<filename>になります。
"""

from jinja2 import Environment, FileSystemLoader
import sys
import optparse
from pathlib import Path
basepath = Path("./output")

sep=","

parser = optparse.OptionParser()
parser.add_option("-t", "--TEMPLATEFILE", dest="fn_temp")
parser.add_option("-c", "--CSVFILE", dest="fn_csv")
(options, args) = parser.parse_args()

fn_temp = options.fn_temp
fn_csv =  options.fn_csv

is_readfromfile = False
if fn_temp is None or fn_csv is None:
    parser.print_help()
    sys.exit(-1)

env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template(fn_temp)

with open(fn_csv, 'r') as fc:
    datalist = fc.readlines()
    assert len(datalist) > 0
    assert datalist[0][0] == '#'
    label = datalist[0][1:].strip().replace(" ", "").split(sep)
    argc = len(label)
    args = []
    filenames = []
    for l in datalist[1:]:
        l = l.strip()
        d = dict()
        if len(l) == 0: continue
        if l[0] == '#': continue
        arg = l.split(sep)
        assert len(arg) == argc
        for i in range(argc): d[label[i]] = arg[i]
        args.append(d)
        filenames.append(arg[0])
    for x in args: print(x)

    for i in range(len(args)):
        rendered_s = tmpl.render(args[i])
        with open(basepath / filenames[i], "w") as fp:
            print("write...",filenames[i])
            fp.write(rendered_s)


