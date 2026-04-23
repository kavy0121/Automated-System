from core.breadboard import Breadboard
from core.router import Router

bb = Breadboard(rows=4, cols=4)

# simulate occupied nodes
bb.occupy("b1")
bb.occupy("b2")

router = Router(bb)

path = router.shortest_path("a1", "d4")

print("Path:", path)