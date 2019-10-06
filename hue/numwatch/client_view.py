from xy import num2rgb
from hue import hue
import argparse

parser = argparse.ArgumentParser(description='hue test')
parser.add_argument('-k', '--key', help='hue key')
parser.add_argument('-s', '--hostname', help='bridge server hostname')
parser.add_argument('-l', '--lights', help='lights number', default="1")
parser.add_argument('-m', '--max', help='max')
parser.add_argument('-n', '--number', help='cur number')
parser.add_argument('--bri', help='bri', default=128)

args = parser.parse_args()

if __name__ == "__main__":
    h = hue(hostname = args.hostname, key = args.key, light=args.lights)
    r, g, b = num2rgb(int(args.number), int(args.max))
    h.setrgb(r, g, b, bri=args.bri)
