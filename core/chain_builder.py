def build_node_chain(plan, pin_map, placed):
    chain = []

    for item in plan["chain"]:
        if item.startswith("PIN") or item in ["VCC", "GND"]:
            chain.append(pin_map.get_node(item))
        else:
            chain.append(placed[item])

    return chain