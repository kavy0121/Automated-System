class MultiRouter:
    def __init__(self, breadboard, router):
        self.bb = breadboard
        self.router = router

    def route_chain(self, nodes):
        """
        nodes = ["a1", "c2", "d3", "rail_gnd"]
        """

        full_path = []

        for i in range(len(nodes) - 1):
            start = nodes[i]
            end = nodes[i + 1]

            path = self.router.shortest_path(start, end)

            if not path:
                print(f"❌ No path from {start} to {end}")
                return None

            # avoid duplicate node overlap
            if full_path:
                path = path[1:]

            full_path.extend(path)

            # 🔥 mark nodes as occupied
            for node in path:
                self.bb.occupy(node)

        return full_path