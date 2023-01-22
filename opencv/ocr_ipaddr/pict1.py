# thx:
# https://qiita.com/shinya187/items/f9a70fd52cc91ddb4ed7
# https://blog.machine-powers.net/2018/08/04/pyocr-and-tips/

# Windows Tesseract
# https://github.com/UB-Mannheim/tesseract/wiki
# add  "c:\Program Files\Tesseract-OCR" to path

"""
request
 opencv-python
 pyocr
"""

import cv2
import pyocr
import sys
from PIL.PIL import Image
import dns.resolver

import ipaddress
def is_ipaddr(s: str):
    try:
        s = s.split("/")[0]
        ip = ipaddress.IPv4Address(s)
        return True
    except ValueError:
        return False

def ipaddrToAsInfo(s):
    queryAddr = "{0}.{1}.{2}.{3}.origin.asn.cymru.com"
    queryAs = "AS{0}.asn.cymru.com"
    print("Try:", s)
    try:
        s = s.split("/")[0]
        ip = ipaddress.IPv4Address(s)
        s = str(ip)
        sarry = s.split(".")
        q = queryAddr.format(*sarry[::-1])
        try:
            answer = dns.resolver.resolve(q, "TXT")
        except dns.resolver.NXDOMAIN:
            return None
        if len(answer) == 0 :
            raise EnvironmentError
        addrInfo = str(answer[0])[1:-1].split("|")
        addrInfo = list(map(lambda x: x.strip(), addrInfo))
        asnum = addrInfo[0]

        q = queryAs.format(asnum)
        try:
            answer = dns.resolver.resolve(q, "TXT")
        except dns.resolver.NXDOMAIN:
            return None
        if len(answer) == 0:
            raise EnvironmentError
        asInfo = str(answer[0])[1:-1].split("|")
        asInfo = list(map(lambda x: x.strip(), asInfo))
        asname = asInfo[4].split(" ")[0]
        return [asnum, asname]
    except ValueError:
        return False

#path_tesseract = "C:\\Program Files\\Tesseract-OCR"
#if path_tesseract not in os.environ["PATH"].split(os.pathsep):
#    os.environ["PATH"] += path_tesseract
#    print("add")

fn = "./pict1.PNG"
im = cv2.imread(fn)
sizey, sizex, _ = im.shape
print("size x,y : {0} x {1}".format(sizex, sizey))

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#im = cv2.GaussianBlur(im, (1,1), 0)

#threshold
#im = cv2.adaptiveThreshold(
#    im    , 255
#    , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY
#    , 11 , 1)


#bitwise
im = cv2.bitwise_not(im)


im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
cv2.imwrite("pict1_out.png",im_rgb)
im_txt = Image.open("pict1_out.png")

# ocr prep
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

# べたーっと文字で吐く
#builder = pyocr.builders.TextBuilder()
#txt = tool.image_to_string(
#    im_txt,lang="eng")
#print(txt)

word_box  = tool.image_to_string(im_txt,
    builder=pyocr.builders.WordBoxBuilder())

im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGRA)

# 左下座標系
boxIpaddr = filter(lambda x: is_ipaddr(x.content), word_box)
for box in boxIpaddr:
    asinfo = ipaddrToAsInfo(box.content)
    print(asinfo)
    if asinfo is None:
        asnum, asname = "",""
    else:
        asnum, asname = asinfo

    if asnum != "":
        print("word: {}, pos: {}".format(box.content, box.position), asnum, asname)
        xy1, xy2 = box.position
        x1, y1 = xy1
        cv2.circle(im, (x1, y1-6), 6, (0,0,255), thickness=-1)
        cv2.line(im, (x1, y1-6), (x1 + 10, y1 - 6 - 3), (0,0,255), thickness=2)
        outstr = "AS:{0}({1})".format(asname.replace(",", ""), asnum)
        xlength = int(len(outstr) * 7.5)
        cv2.rectangle(im, (x1 + 10, y1 - 6 - 3 - 10), (x1 + 10 + xlength, y1 - 6 - 3+3) , (255,255,255), -1)
        cv2.putText(im, outstr, (x1 + 10, y1 - 6 - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 1)


# sys.exit(0)
cv2.imshow("debug", im)
cv2.waitKey(0)