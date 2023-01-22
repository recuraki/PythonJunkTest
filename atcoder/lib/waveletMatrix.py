# https://miti-7.hatenablog.com/entry/2018/04/15/155638


import math
fullbit = 0xffffffffffffffff

#https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

class SuccinctBitVector(object):
    size = 0
    blockLarge = []
    blockSmall = []
    blockBit = []
    numBlockLarge = 512
    numBlockSmall = 16
    numBlockBit = 16
    numOne = 0



    def __init__(self, size: int):
        # bit vectorを生成する．sizeは長さ
        self.size = size
        self.blockBit = [0] *  (math.ceil(size / self.numBlockBit))
        self.blockSmall = [0] * (size // self.numBlockSmall)
        self.blockLarge = [0] * (size // self.numBlockLarge)

    def setBit(self, bit: int, pos: int):
        assert bit == 0 or bit == 1
        assert pos < self.size

        posBlock  = pos // self.numBlockBit
        offset = pos % self.numBlockBit

        if bit == 1:
            self.blockBit[posBlock] |= 1 << offset
        else:
            self.blockBit[posBlock] &= fullbit & (1 << offset)

    def access(self, pos):
        assert pos < self.size
        posBlock  = pos // self.numBlockBit
        offset = pos % self.numBlockBit
        return (self.blockBit[posBlock] >> offset) & 1

    def build(self):
        num = 0


