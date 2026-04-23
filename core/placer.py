class Placer:
    def __init__(self, breadboard):
        self.bb = breadboard

    def place_components(self, chain_nodes):
        placed = {}

        for item in chain_nodes:
            if item.startswith("PIN") or item in ["VCC", "GND"]:
                continue

            node = self.find_nearest_free("a1")  # start near MCU

            self.bb.occupy(node)
            placed[item] = node

        return placed

    def find_nearest_free(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)

                if self.bb.is_free(node):
                    return node

                for n in self.bb.graph[node]:
                    queue.append(n)

        return None