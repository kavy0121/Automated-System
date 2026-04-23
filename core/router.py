import heapq

class Router:
    def __init__(self, breadboard):
        self.bb = breadboard   # 🔥 access graph + state

    def shortest_path(self, start, end):
        queue = [(0, start, [])]   # (cost, current_node, path)
        visited = set()

        while queue:
            cost, node, path = heapq.heappop(queue)

            # skip visited
            if node in visited:
                continue

            # build path
            path = path + [node]
            visited.add(node)

            # 🎯 target reached
            if node == end:
                return path

            # explore neighbors
            for neighbor in self.bb.graph.get(node, []):

                # 🔥 SKIP OCCUPIED NODES
                if not self.bb.is_free(neighbor) and neighbor != end:
                    continue

                heapq.heappush(queue, (cost + 1, neighbor, path))

        return None