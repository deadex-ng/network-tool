from functools import reduce

def unique(nodes: list[str]) -> list[str]:
    """Returns a list with unique elemets.

    Args:
    nodes: List[str]. Graph nodes.
    """
    unique_values = reduce(lambda x, y: x + [y] if y not in x else x, nodes, [])
    return unique_values