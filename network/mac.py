# -*- coding: utf-8 -*-
import unittest

def splitchar2list(s: str, n: int):
    assert (len(s) % n) == 0
    return [int(s[i*n:(i+1)*n], 16) for i in range(len(s) // 2)]

class macaddress(object):
    __macaddr = None

    def __init__(macaddr: str = None):
        if macaddr is None: return

    @property
    def macaddr(self):
        return self.__macaddr

    @macaddr.setter
    def macaddr(self, s):
        assert len(s) <= 17
        s = s.lower()
        import re
        if re.match(r"^[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}$", s):
            t = s.split(":")
            t = list(map(lambda x: int(x, 16), t))
            t = list(map(lambda x: f"{x:02x}", t))
            t = "".join(t)
            l = splitchar2list(t, 2)
            self.__macaddr = l
            return
        if re.match(r"^[0-9a-f]{1,2}-[0-9a-f]{1,2}-[0-9a-f]{1,2}-[0-9a-f]{1,2}-[0-9a-f]{1,2}-[0-9a-f]{1,2}$", s):
            t = s.split("-")
            t = list(map(lambda x: int(x, 16), t))
            t = list(map(lambda x: f"{x:02x}", t))
            t = "".join(t)
            l = splitchar2list(t, 2)
            self.__macaddr = l
            return
        if re.match(r"^[0-9a-f]{1,4}.[0-9a-f]{1,4}.[0-9a-f]{1,4}$", s):
            t = s.split(".")
            t = list(map(lambda x: int(x, 16), t))
            t = list(map(lambda x: f"{x:04x}", t))
            t = "".join(t)
            l = splitchar2list(t, 2)
            self.__macaddr = l
            return
        raise ValueError

    @property
    def macaddrlist(self):
        return self.__macaddr

    @property
    def macaddrplain(self):
        return "".join(map(lambda x: f"{x:02x}", self.__macaddr))

    @property
    def macaddrcolon(self):
        return ":".join(map(lambda x: f"{x:02x}", self.__macaddr))

    @property
    def macaddrdash(self):
        return "-".join(map(lambda x: f"{x:02x}", self.__macaddr))

    @property
    def macaddrdot(self):
        return "{:02x}{:02x}.{:02x}{:02x}.{:02x}{:02x}".format(*self.__macaddr)

class TestMac2plain(unittest.TestCase):
    def test_simpleplain(self):
        st = macaddress()
        st.macaddr = "0001.0001.0301"
        self.assertEqual(st.macaddrplain, '000100010301')
        st.macaddr = "aAaa.BBbb.CCCc"
        self.assertEqual(st.macaddrplain, 'aaaabbbbcccc')
        st.macaddr = "00:00:00:00:00:00"
        self.assertEqual(st.macaddrplain, '000000000000')
        st.macaddr = "99:00:0b:00:0a:00"
        self.assertEqual(st.macaddrplain, '99000b000a00')
        st.macaddr = "00-00-00-00-00-00"
        self.assertEqual(st.macaddrplain, '000000000000')
        st.macaddr = "99-00-0b-00-0a-00"
        self.assertEqual(st.macaddrplain, '99000b000a00')

    def test_simpledot(self):
        st = macaddress()
        st.macaddr = "0001.0001.0301"
        self.assertEqual(st.macaddrdot, "0001.0001.0301")

    def test_simpledash(self):
        st = macaddress()
        st.macaddr = "0001.0001.0301"
        self.assertEqual(st.macaddrdash, '00-01-00-01-03-01')

    def test_simplecolon(self):
        st = macaddress()
        st.macaddr = "0001.0001.0301"
        self.assertEqual(st.macaddrcolon, '00:01:00:01:03:01')

    def test_simplelist(self):
        st = macaddress()
        st.macaddr = "0001.0001.0301"
        self.assertEqual(st.macaddrlist, [0, 1, 0, 1, 3, 1])
        st.macaddr = "aaaaaaaaaaab"
        self.assertEqual(st.macaddrlist, [170, 170, 170, 170, 170, 171])

    def test_simplify(self):
        st = macaddress()
        st.macaddr ="1.1.1"
        self.assertEqual(st.macaddrplain, '000100010001')
        st.macaddr ="aaaa.bbbb.cccc"
        self.assertEqual(st.macaddrplain, 'aaaabbbbcccc')
        st.macaddr ="0:0:0:0:0:0"
        self.assertEqual(st.macaddrplain, '000000000000')
        st.macaddr ="99:0:b:0:a:0"
        self.assertEqual(st.macaddrplain, '99000b000a00')
        st.macaddr ="0-0-0-0-0-0"
        self.assertEqual(st.macaddrplain, '000000000000')
        st.macaddr ="99-0-b-0-a-0"
        self.assertEqual(st.macaddrplain, '99000b000a00')

    def test_error(self):
        st = macaddress()
        with self.assertRaises(ValueError):
            st.macaddr = "1.1.1.1"
        with self.assertRaises(ValueError):
            st.macaddr = "1.g.1"
        with self.assertRaises(ValueError):
            st.macaddr = " aaaa.aaaa.aaaa"

if __name__ == '__main__':
    unittest.main()