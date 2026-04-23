from core.breadboard import Breadboard
from core.router import Router
from core.multi_router import MultiRouter
from core.placer import Placer
from core.pin_mapper import PinMapper
from core.chain_builder import build_node_chain
from ai.planner import plan_circuit
from ai.codegen import generate_code

bb = Breadboard(rows=5, cols=5)
router = Router(bb)
multi = MultiRouter(bb, router)
placer = Placer(bb)
mapper = PinMapper()

# 🔥 USER INPUT
command = "Blink LED"

# STEP 1: AI PLAN
plan = plan_circuit(command)

# STEP 2: PLACE COMPONENTS
placed = placer.place_components(plan["chain"])

# STEP 3: BUILD NODE CHAIN
chain = build_node_chain(plan, mapper, placed)

# STEP 4: ROUTE
path = multi.route_chain(chain)

# STEP 5: GENERATE CODE
code = generate_code(plan)

print("CHAIN:", chain)
print("PATH:", path)
print("CODE:\n", code)