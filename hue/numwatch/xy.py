def rgb2xy(r, g, b):
    # thanks: https://stackoverflow.com/questions/22564187/rgb-to-philips-hue-hsb
    if r==0 and g == 0 and b==0:
        r = 1
        g = 1
        b = 1

    red, green, blue = r/255, g/255, b/255
    import math

    if red > 0.04045:
        red = math.pow((red + 0.055) / (1.0 + 0.055), 2.4)
    else:
        red = (red / 12.92)
    if green > 0.04045:
        green = math.pow((green + 0.055) / (1.0 + 0.055), 2.4)
    else:
        green = (green / 12.92)

    if blue > 0.04045:
        blue = math.pow((blue + 0.055) / (1.0 + 0.055), 2.4)
    else:
        blue = (blue / 12.92)

    X = red * 0.664511 + green * 0.154324 + blue * 0.162028;
    Y = red * 0.283881 + green * 0.668433 + blue * 0.047685;
    Z = red * 0.000088 + green * 0.072310 + blue * 0.986039;
    x = X / (X + Y + Z);
    y = Y / (X + Y + Z);
    x, y = round(x, 4), round(y, 4)

    return (x, y)


def num2rgb(n, max):
    """
    この関数はmaxに対するnの割合によって色を変えます
    0%: 青
    25%: 水色
    50%: 緑
    75%: 黄色
    100%: 赤色
    :param n:
    :param max:
    :return:
    """
    r, g, b = 0, 0, 0
    maxhalf = max // 2
    if n > max:
        r = 255
    elif n > (max// 2):
        n -= maxhalf
        r = (n / maxhalf * 255)
        g = 255 - (n / maxhalf * 255)
    else:
        g = (n / maxhalf * 255)
        b = 255 - (n / maxhalf * 255)
    return r, g, b


if __name__ == "__main__":
    print(rgb2xy(0, 0 ,255))
