def pluralize(word, count=2):
    return word if count <= 1 else f"{word}s"


def print_stats(node_count, edge_count, node_label='family member', edge_label='relationship'):
    print(f"{node_count} {pluralize(node_label)}")
    print(f"{edge_count} {pluralize(edge_label)}")
