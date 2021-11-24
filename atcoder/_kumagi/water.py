s = """7 7
0 0 0 1 0 0 0
0 0 0 1 0 0 0
0 0 0 1 0 0 0
1 1 1 1 1 1 1
0 0 0 1 0 0 0
0 0 0 1 0 0 0
0 0 0 1 0 0 0
"""
s = """7 7
0 0 0 1 0 0 0
0 1 0 1 0 0 0
0 1 1 1 1 0 0
1 1 1 1 1 1 1
0 1 1 1 1 0 0
0 1 1 1 1 0 0
0 1 0 1 0 0 0
"""

from pprint import pprint


def func(s):
    s = s.split("\n")

    # 周りを海にしてloadする
    hnum, wnum = map(int, s[0].split())
    maze = []
    maze.append([0] * (wnum + 2))
    for i in range(hnum):
        maze.append([0] + list(map(int, s[i+1].split())) + [0])
    maze.append([0] * (wnum + 2))
    hnum += 2
    wnum += 2
    # ここからコード
    dmove = (( (0, -1), (-1, 0), (1, 0), (0, 1)))
    from collections import deque
    nextq = deque([])
    pprint(maze)
    # まず、初期位置の海の位置を全部読む
    for h in range(hnum):
        for w in range(wnum):
            if maze[h][w] == 0:
                nextq.append( (h, w) )
    ans = 0
    while len(nextq) > 0: # 次に処理する海がないなら抜ける
        pprint(maze) # 沈む様子が見えるよ
        q = nextq # このターンのキューを設定する
        nextq = deque([]) # 次のターンのキュー
        while len(q) > 0: # このターンの海について処理
            h, w = q.popleft()
            for dh, dw in dmove:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < hnum): continue
                if not (0 <= nw < wnum): continue
                # 今の海の四方に陸地があるなら、海にして、次のターンはそこを処理
                if maze[nh][nw] == 1:
                    maze[nh][nw] = 0
                    nextq.append( (nh, nw) )
        # もし、このターンに、陸を海にしたことがあるなら、有益だったので++する。
        if len(nextq) > 0: ans += 1
    return ans

func(s)
