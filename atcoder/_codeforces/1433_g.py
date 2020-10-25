import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import re
    import heapq

    def initialize_graph(n):
        graph = {}
        for i in range(n):
            node1, node2, cost = map(int, input().split())
            graph = set_new_node(graph, node1, node2)
            graph[node1][node2] = cost
            graph[node2][node1] = cost
        return graph

    def set_new_node(graph, node1, node2):
        if not node1 in graph.keys():
            graph[node1] = {}
        if not node2 in graph.keys():
            graph[node2] = {}
        return graph

    def solve_by_dijkstra(graph, st, en):
        min_dist_dict = {}
        prev_node_dict = {}
        q = []
        heapq.heappush(q, (0, st))
        prev_node = ''
        while True:
            dist, node = heapq.heappop(q)
            min_dist_dict[node] = dist
            prev_node_dict[node] = prev_node
            if node == en:
                return min_dist_dict, prev_node_dict
            prev_node = node
            culc_min_dist_and_put(graph, q, node, min_dist_dict, prev_node_dict)

    def culc_min_dist_and_put(graph, q, departure_node, min_dist_dict, prev_node_dict):
        for arrival_node in graph[departure_node].keys():
            tmp_d = min_dist_dict[departure_node] + graph[departure_node][arrival_node]
            if arrival_node in min_dist_dict.keys():
                if tmp_d < min_dist_dict[arrival_node]:
                    min_dist_dict[arrival_node] = tmp_d
                    heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))
                else:
                    min_dist_dict[arrival_node] = tmp_d
                    heapq.heappush(q, (min_dist_dict[arrival_node], arrival_node))

    def main():
        min_dist_dict, prev_node_dict = solve_by_dijkstra(graph)
        # GOALノードからprev_node_dictをたどって経路を復元
        print('Route : GOAL ', end='')
        node = 'GOAL'
        while True:
            if node == 'START':
                print()
            break
            print(' ← ' + prev_node_dict[node], end='')
            node = prev_node_dict[node]
        print('Min Cost : ' + str(min_dist_dict['GOAL']))

    a,b,c = map(int, input().split())
    graph = initialize_graph(b)
    print(graph)
    min_dist_dict, prev_node_dict = solve_by_dijkstra(graph, 1, 3)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """6 5 2
1 2 5
2 3 7
2 4 4
4 5 2
4 6 8
1 6
5 3"""
        output = """22"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5 4
1 2 5
2 3 4
1 4 3
4 3 7
3 5 2
1 5
1 3
3 3
1 5"""
        output = """13"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()