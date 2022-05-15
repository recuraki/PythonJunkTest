import heapq
from collections import deque
class dijkstra():
    INF = 2 ** 62 + 10000
    INF = float("inf")
    INF = -1
    def __init__(self, numV):
        self.numV = numV
        self.e = [[] for _ in range(numV)]

    def makeEdge(self, s, t, cost):
        self.e[s].append((t, -cost))

    def solve(self, nodeS, nodeT):
        self.distance = [self.INF] * self.numV
        self.cost = [self.INF] * self.numV # cost
        self.parent = [-1] * self.numV # parent node
        q = [(10**9, nodeS)]
        self.cost[nodeS] = 10**9
        heapq.heapify(q)
        while len(q) > 0:
            curcost, curnode = heapq.heappop(q)
            if curcost < self.cost[curnode]:
                continue
            for nextnode, edgecost in self.e[curnode]:
                edgecost = -edgecost
                nextcost = min(curcost , edgecost)
                if self.cost[nextnode] < nextcost:
                    self.cost[nextnode] = nextcost
                    self.parent[nextnode] = curnode
                    heapq.heappush(q, (nextcost, nextnode))

    def findRoute(self, s, t):
        # THIS FUNCTION should be called after solve()
        route = deque([])
        nextnode = t
        while nextnode != -1:
            route.appendleft(str(nextnode))
            nextnode = self.parent[nextnode]
        return route

class IOIVoting:
    def winners(self, n, inputdata):
        dat = [[0] * n for _ in range(n)]
        buf = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dat[i][j] = inputdata[i*n + j]
        from pprint import pprint
        print()
        #pprint(dat)

        for i in range(n):
            for j in range(n):
                buf[i][j] = dat[i][j] - dat[j][i]
        #print("--")
        #pprint(buf)

        dj = dijkstra(n)
        for i in range(n):
            for j in range(n):
                if i ==j: continue
                if buf[i][j] > 0:
                    dj.makeEdge(i, j, buf[i][j])
        res = []
        battle = []
        for i in range(n):
            dj.solve(i, i) # query
            l = list(dj.cost)
            battle.append(l)
        #pprint(battle)
        for i in range(n):
            can = True
            for j in range(n):
                if i == j:
                    continue
                if buf[i][j] > 0:
                    continue
                if battle[i][j] >= battle[j][i]:
                    continue
                can = False
            if can:
                res.append(i)
        #print(res)
        return res







# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(N, votes, __expected):
    startTime = time.time()
    instance = IOIVoting()
    exception = None
    try:
        __result = instance.winners(N, votes);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("IOIVoting (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("IOIVoting.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            votes = []
            for i in range(0, int(f.readline())):
                votes.append(int(f.readline().rstrip()))
            votes = tuple(votes)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, votes, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1624619103
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
