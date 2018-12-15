"""
特定のカラーだけ特定フレーム数分だけ遅れさせてみるテスト
"""
import cv2
import numpy

# read元
cap = cv2.VideoCapture("test.avi")

# 最初の1フレームを犠牲に、画像の大きさを取得
ret, frame = cap.read()
if len(frame.shape) == 3:
    height, width, channels = frame.shape[:3]
else:
    height, width = frame.shape[:2]
    channels = 1

# 描画先のファイルを開く
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width,height))

# depthフレーム分のバッファを作る
zeros = numpy.zeros((height, width), frame.dtype)
layer_blue = []
depth = 5
for i in range(depth):
    layer_blue.append(zeros)

while(cap.isOpened()):
    # 1フレーム読み込む
    ret, frame = cap.read()

    # EoFまでloop
    if ret==True:

        # RGBにばらす
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame)

        # バッファの先頭を読み込み、最後を削る
        layer_blue.append(img_blue_c1)
        layer_blue = layer_blue[1:]
        img_blue_c1 = layer_blue[0]

        # フレームを作る
        frame = cv2.merge((img_red_c1, img_green_c1, img_blue_c1))

        # ファイルに書き出す
        out.write(frame)

        # 画面に表示させたいときはこっち
        #cv2.imshow('frame', frame)

        #　画面表示モードの場合、"q"を押すと狩猟
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 後処理
out.release()
cap.release()
