
def fill(x, y, z, sizex, sizey, sizez, block):
    sizex += x
    sizey += y
    sizez += z
    return  "/fill {0} {1} {2} {3} {4} {5} {6}".format(x, y, z, sizex, sizey, sizez, block)

AIR="minecraft:air"
TNT="minecraft:tnt"
IRONBAR="minecraft:iron_bars"
GLASS="minecraft:glass"
LAPIS="minecraft:lapis_block"
IRONDOOR="minecraft:iron_door"
def func(x, y, z, sizex, sizey, sizez):
    print(fill(x,y,z, sizex, sizey, sizez, AIR))
    print(fill(x,y,z, sizex, sizey, sizez, IRONBAR))
    print(fill(x+1, y+1, z+1, sizex-2, sizey-2, sizez-2, AIR))
    print(fill(x,y,z, sizex, 0, sizez, LAPIS))
    print(fill(x,y+sizey,z, sizex, 0, sizez, GLASS))
    a,b,c = x + (sizex//2), y+1, z
    print(fill(a,b,c,0,0,0, IRONDOOR))

func(236, 65, -328, 10, 10, 10)
