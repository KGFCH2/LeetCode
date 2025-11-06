from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        online = set()
        station_group = {}
        min_heaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_group[station] = group_id
            heappush(min_heaps[group_id], station)

            for nei in adj[station]:
                dfs(nei, group_id)

        for s in  range(1, c+1):
            dfs(s, s)

        res = []
        for q_type, q_station in queries:
            if q_type == 1:
                if q_station in online:
                    res.append(q_station)
                    continue
                group_id = station_group[q_station]
                min_heap = min_heaps[group_id]
                while min_heap and min_heap[0] not in online:
                    heappop(min_heap)
                if min_heap:
                    res.append(min_heap[0])
                else:
                    res.append(-1)
            else:
                online.discard(q_station)
        return res
        