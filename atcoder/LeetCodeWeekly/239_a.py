
from typing import List, Tuple
from pprint import pprint


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        candidate = []
        for i in range(len(nums)):
            if nums[i] == target:
                candidate.append(i)
        res = 10 ** 18
        for x in candidate:
            res = min(res, abs(x-start))
        return res

st = Solution()

print(st.getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3) == 1)
print(st.getMinDistance(nums = [1], target = 1, start = 0) == 0)
print(st.getMinDistance(nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0) == 0)
print(st.getMinDistance([5838,9029,4439,9310,5840,7765,4017,3930,1730,9214,5861,2600,1908,665,5140,6921,5674,4154,913,7125,6799,6166,5878,4816,5591,7226,3901,9989,8504,2366,919,5596,1860,8406,2822,8898,7987,5587,1991,9549,355,7869,3428,6279,2863,6509,3733,1634,4070,5499,5392,7559,7720,6055,8072,3175,7078,7219,6535,8881,1973,9363,8000,4366,2052,2456,196,6163,6794,1786,430,1223,2998,7517,6178,8226,4727,2548,2528,8596,1733,4172,308,7610,6498,3742,8811,6403,88,8915,4088,6930,2604,2934,5612,3919,1247,8788,9140,2637,2878,6156,9591,354,8407,3554,7003,3862,663,8449,3117,8259,8795,1266,4062,6524,7618,1952,9290,793,6341,1470,9175,1550,7847,737,8495,200,342,5112,7642,4556,6809,2732,9748,2183,9203,5216,8761,7352,8219,6843,9074,2747,6480,6375,3289,8117,4562,5899,2482,4251,9288,4580,2870,1371,5907,5507,2339,4235,4179,4134,5724,6296,4574,9265,7664,221,2442,2135,4141,3702,3220,1155,9493,8808,3251,8897,7033,9464,2281,9076,7545,6412,3209,1353,1265,2509,943,496,6642,6269,6837,2253,9684,9780,2117,8823,8952,1216,3953,6254,2285,4681,3317,6508,5847,2922,3689,4880,2357,5698,8063,8772,4781,1452,8427,4898,3422,7594,359,4757,9710,1689,6106,7268,4177,955,854,5171,2620,2169,1693,1844,7132,9610,4029,3406,8262,8319,6502,1992,3477,6289,8478,2195,9476,60,1981,3303,9220,6194,7898,8930,3780,4386,618,2749,9083,8239,3820,6725,4485,6901,6530,4457,8094,1602,2124,3059,9168,261,7438,735,8003,3512,6455,8826,5510,3990,1541,1264,699,6925,7239,3094,2839,9754,8225,3113,8352,6305,8550,5908,3229,3813,5894,9602,1057,5588,849,7512,725,2897,2420,4679,7687,706,9558,8210,1063,6493,1508,6553,8385,9379,4937,6462,4390,5771,7711,805,9048,7818,286,6994,4991,9645,5199,2448,9767,9656,9106,4552,1080,9948,5915,6802,6407,8517,388,9432,9532,606,9402,8677,236,1654,5441,5517,6035,9026,565,6065,9548,7946,1373,8841,7311,5481,8194,56,2634,5326,5913,3506,2395,9507,2429,9660,1768,6619,5198,8334,6896,5594,4257,9976,6038,617,1040,4042,4351,6506,9018,4651,9401,1368,1228,2792,4380,6780,1365,2069,4628,9025,4306,3848,3451,1620,4541,7872,772,8392,3341,8908,1231,9023,5169,5566,4851,8457,2184,578,7246,5963,611,471,6841,2684,9126,666,9640,8616,6957,3021,3235,3815,1881,9625,2131,9613,8295,2007,4368,7510,3217,906,5920,7474],3702,314)==143)

print(st.getMinDistance([5812,3601,154,229,8008,529,2694,4151,9044,654,151,3770,1387,8591,2840,576,8654,3281,3432,7258,4732,3982,8037,8289,6085,5324,6423,1204,3199,9738,2974,3073,4866,9524,6984,7767,5956,380,7985,339,1717,9470,7086,9539,5630,5553,1214,6885,3200,8426,8100,9961,9235,9018,8210,7826,9830,9433,7375,9892,7720,2710,4396,8593,4941,9232,6496,9952,8843,4246,4185,5084,241,9906,752,7497,5826,3804,8323,7278,3427,7799,5499,2373,6290,7166,889,1823,5838,135,4192,8866,886,5021,6206,246,5317,5541,5060,9654,815,3418,1340,5385,1965,1086,2104,4822,6712,9953,5584,3811,446,2999,8261,9406,5994,4957,4813,6194,6889,8625,7561,1216,3261,6680,3795,9960,692,3945,3680,3990,6467,6216,3444,2491,4903,5900,24,5035,7279,8158,2800,2399,511,6075,7160,9076,5602,8409,8024,5204,9893,1828,9562,4789,8980,4524,7038,186,5091,1417,8060,1884,8211,3614,9923,4337,7157,6107,3778,1680,9780,8442,8425,8378,2672,2126,4786,792,1120,3576,52,1013,6930,345,1085,902,147,572,8814,5557,5452,308,145,9160,3463,7684,3279,4363,4840,9531,9023,8545,4119,3826,2993,3453,6414,980,3910,9099,7416,580,5430,5353,6665,1962,263,9217,3032,8284,1535,3029,3578,3685,2893,4984,1603,964,5143,2397,1030,7261,2459,3784,707,4690,5642,956,9660,1463,7251,3733,3033,1953,942,3316,1900,1433,3602,4688,4131,8638,6928,4074,4125,3192,5338,5734,5853,7443,6267,6333,1465,6982,4006,8018,5632,2927,9912,1866,3928,1185,7154,4538,8721,4978,5490,6072,6706,7477,5970,5766,5176,6489,7723,8377,281,6067,2087,4955,2753,4952,9287,2077,8988,2450,2735,7499,2495,2215,2640,1306,4160,3858,5832,5165,2811,4543,7751,5075,1266,7019,2524,9011,5788,7368,1761,2553,5175,1134,3061,7858,8759,573,768,3141,5833,5998,8319,5822,8252,6137,5605,1973,3026,6152,535,4439,1023,4047,4988,5359,9230,6603,4004,5894,811,3798,4761,9314,112,3201,1592,2220,3650,6044,8293,4367,2308,2661,3737,1236,5103,9395,8368,8344,8839,9835,8879,7080,7199,9517,8385,7783,2997,8396,5827,3203,7096,3363,3751,2332,2189,3412,348,2681,7958,5946,3014,808,5904,1352,9990,3889,3464,1427,7230,3217,9857,5611,2704,9423,295,3565,5179,7871,9046,594,859,6010,8192,9162,5727,2221,7999,8376,5224,9293],4988,159)==183)