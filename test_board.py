from core.breadboard import Breadboard

bb = Breadboard(rows=4, cols=4)

bb.print_board()

print("\nConnections of a1:", bb.graph["a1"])

bb.occupy("a1")
bb.occupy("b1")

bb.print_board()