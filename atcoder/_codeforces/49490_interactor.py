import sys
ans, qcount = 10, 0
while qcount < 26:
    qcount += 1
    s = input()
    #print("recv raw:", s, file=sys.stderr)
    if s[0] == "!":
        if int(s.split(" ")[1]) == ans: print("OK!"), sys.exit(0)
        else: print("NG!"), sys.exit(20)
    if ans < int(s): print("<")
    else: print(">=")
print("GAMEOVER!")
sys.exit(10)


