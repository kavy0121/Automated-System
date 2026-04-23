class Breadboard:
    def __init__(self, rows=5, cols=10):
        self.rows = rows
        self.cols = cols

        self.graph = {}
        self.state = {}

        self._create_nodes()
        self._create_connections()   # 🔥 this must exist


    # 🔹 CREATE NODES
    def _create_nodes(self):
        for r in range(self.rows):
            row_char = chr(ord('a') + r)
            for c in range(1, self.cols + 1):
                node = f"{row_char}{c}"
                self.graph[node] = []
                self.state[node] = "free"


    # 🔹 CREATE CONNECTIONS (FIXED)
    def _create_connections(self):

        # COLUMN CONNECTIONS
        for c in range(1, self.cols + 1):
            column_nodes = [f"{chr(ord('a') + r)}{c}" for r in range(self.rows)]

            for i in range(len(column_nodes)):
                for j in range(i + 1, len(column_nodes)):
                    n1 = column_nodes[i]
                    n2 = column_nodes[j]

                    self.graph[n1].append(n2)
                    self.graph[n2].append(n1)

        # ROW CONNECTIONS
        for r in range(self.rows):
            row_char = chr(ord('a') + r)
            row_nodes = [f"{row_char}{c}" for c in range(1, self.cols + 1)]

            for i in range(len(row_nodes)):
                for j in range(i + 1, len(row_nodes)):
                    n1 = row_nodes[i]
                    n2 = row_nodes[j]

                    self.graph[n1].append(n2)
                    self.graph[n2].append(n1)


    # 🔹 STATE FUNCTIONS
    def is_free(self, node):
        return self.state.get(node) == "free"

    def occupy(self, node):
        self.state[node] = "occupied"

    def free_node(self, node):
        self.state[node] = "free"
    
    def print_board(self):
        print("\n📋 Breadboard State:\n")
        for node in sorted(self.state):
            print(f"{node}: {self.state[node]}")