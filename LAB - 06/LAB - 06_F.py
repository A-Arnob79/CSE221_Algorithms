from collections import defaultdict
import heapq

def find_order(words):
    graph = defaultdict(list)
    indegree = {}

    for w in words:
        for ch in w:
            indegree[ch] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w1) > len(w2) and w1.startswith(w2):
            return "-1"

        for a, b in zip(w1, w2):
            if a != b:
                if b not in graph[a]:
                    graph[a].append(b)
                    indegree[b] += 1
                break

    Q = []
    for c in indegree:
        if indegree[c] == 0:
            heapq.heappush(Q, c)

    result = []
    while Q:
        ch = heapq.heappop(Q)
        result.append(ch)
        for N in sorted(graph[ch]):
            indegree[N] -= 1
            if indegree[N] == 0:
                heapq.heappush(Q, N)

    if len(result) != len(indegree):
        return "-1"
    return ''.join(result)

n = int(input())
words = []
for _ in range(n):
    l = input()
    a = l.strip()
    words.append(a)
print(find_order(words))