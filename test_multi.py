from core.breadboard import Breadboard
from core.router import Router
from core.multi_router import MultiRouter

bb = Breadboard(rows=4, cols=4)
router = Router(bb)
multi = MultiRouter(bb, router)

# simulate circuit
chain = ["a1", "b3", "c4", "d1"]

path = multi.route_chain(chain)

print("Full Path:", path)
bb.print_board()