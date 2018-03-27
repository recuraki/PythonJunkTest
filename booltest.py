#! env python3
# -*- coding: utf-8 -*-

def proc_before(src, dst):
    if src == "any" and dst == "any":
        print(" > src dst")
    elif src != "any" and dst == "any":
        print(" > src eq {0} dst".format(src))
    elif src == "any" and dst != "any":
        print(" > src dst eq {0}".format(dst))
    elif src != "any" and dst != "any":
        print(" > src eq {0} dst eq {1}".format(src, dst))

def proc_after(src, dst):
    if (src == "any" and dst == "any") or (src == "" and dst == ""):
        print(" > src dst")
    elif (src != "any" and dst == "any") or (src != "" and dst == ""):
        print(" > src eq {0} dst".format(src))
    elif (src == "any" and dst != "any") or (src == "" and dst != ""):
        print(" > src dst eq {0}".format(dst))
    else:
        print(" > src eq {0} dst eq {1}".format(src, dst))

def proc_after2(src, dst):

    if (src == "any" or src == "") or (dst == "" or dst == "any"):
        print(" > src dst")
    elif (src != "any" and src != "" ) or (dst == "" or dst == "any"):
        print(" > src eq {0} dst".format(src))
    elif (src == "any" or src == "" ) or (dst != "any" and dst != ""):
        print(" > src dst eq {0}".format(dst))
    else:
        print(" > src eq {0} dst eq {1}".format(src, dst))

def proc_after3(src, dst):
    if src == "":
        src = "any"
    if dst == "":
        dst = "any"
    if src == "any" and dst == "any":
        print(" > src dst")
    elif src != "any" and dst == "any":
        print(" > src eq {0} dst".format(src))
    elif src == "any" and dst != "any":
        print(" > src dst eq {0}".format(dst))
    elif src != "any" and dst != "any":
        print(" > src eq {0} dst eq {1}".format(src, dst))


def test(func):
    print("any, any")
    func("any", "any")

    print("80, any")
    func("80", "any")

    print("any, 80")
    func("any", "80")

    print("80, 443")
    func("80", "443")

    print("(),()")
    func("", "")

    print("80, ()")
    func("80", "")

    print("(), 80")
    func("", "80")

    print("80, 443")
    func("80", "443")

    print("any, ()")
    func("any", "")

    print("(), any")
    func("", "any")


print("=== before ===")
test(proc_before)
print("=== after ===")
test(proc_after3)