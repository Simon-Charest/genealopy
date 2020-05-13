import networkx
import random


def get_hierarchy_positions(graph, root=None, width=1., vertical_gap=0.2, vertical_loc=0.0, x_center=0.5):
    """
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    graph: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vertical_gap: gap between levels of hierarchy

    vertical_loc: vertical location of root

    x_center: horizontal location of root
    """

    if not networkx.is_tree(graph):
        raise TypeError('Cannot use get_hierarchy_positions function on a graph that is not a tree.')

    if root is None:
        if isinstance(graph, networkx.DiGraph):
            root = next(iter(networkx.topological_sort(graph)))  # Allows backward compatibility with nx version 1.11

        else:
            root = random.choice(list(graph.nodes))

    def _get_hierarchy_positions(graph, root, width=1., vertical_gap=0.2, vertical_loc=0.0, x_center=0.5, pos=None,
                                 parent=None):
        """
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed
        """

        if pos is None:
            pos = {root: (x_center, vertical_loc)}

        else:
            pos[root] = (x_center, vertical_loc)

        children = list(graph.neighbors(root))

        if not isinstance(graph, networkx.DiGraph) and parent is not None:
            children.remove(parent)

        if len(children) != 0:
            dx = width / len(children)
            next_x = x_center - width / 2 - dx / 2

            for child in children:
                next_x += dx
                pos = _get_hierarchy_positions(graph, child, width=dx, vertical_gap=vertical_gap,
                                               vertical_loc=vertical_loc - vertical_gap, x_center=next_x, pos=pos,
                                               parent=root)

        return pos

    return _get_hierarchy_positions(graph, root, width, vertical_gap, vertical_loc, x_center)
