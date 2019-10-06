hueを使った値の可視化
===

# これはなに？
ネットワークトラフィックなどなにかの利用率をHueで可視化します。
```
青: 0%
水: 25%
緑: 50%
黄色: 75%
赤: 100%
```
です。

# 使い方
```
usage: client_view.py [-h] [-k KEY] [-s HOSTNAME] [-l LIGHTS] [-m MAX]
                      [-n NUMBER] [--bri BRI]

optional arguments:
  -k KEY, --key KEY     hueのkeyです
  -s HOSTNAME, --hostname BridgeサーバのIPアドレスを指定します
  -l LIGHTS, --lights Bridge内でユニークなライトの番号を指定します
  -m MAX, --max MAX "-n"の分母となる整数値
  -n NUMBER, --number maxに対する分子となる整数値
  --bri BRI 明るさ(0 - 255)
```

# 例
```
python3 /home/sun2019/hue/client_view.py -k 198f098f09809h83dTxWwyVpRWAurhZQKvqYXDadui6 -s 192.168.255.240 -l 1 -m 500 -n 100 --bri=100
 > max 500に対して 100 = 20% を192.168.255.240に管理されているlight 1に明るさ100で表示します
```

# RGB直指定
```
usage: hue.py [-h] [-k KEY] [-s HOSTNAME] [-l LIGHTS] [-r RED] [-g GREEN]
              [-b BLUE] [--bri BRI]
  -k KEY, --key KEY     hueのkeyです
  -s HOSTNAME, --hostname BridgeサーバのIPアドレスを指定します
  -l LIGHTS, --lights Bridge内でユニークなライトの番号を指定します
  -r RED, --red RED(0-255)
  -g GREEN, --green (0-255)
  -b BLUE, --blue BLUE (0-255)
  --bri BRI 明るさ(0 - 255)
```