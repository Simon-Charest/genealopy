from common.constant import constant
import json
import matplotlib.pyplot as pyplot
import networkx


def run():
    # Read JSON data
    with open(constant.DATA, encoding='utf-8') as stream:
        json_document = json.load(stream)

    # Create directional graph
    graph = networkx.DiGraph()

    # Loop on every person
    for key, value in json_document.items():
        node = f"{value['first_name']}\n{value['last_name']}"

        # Add person to graph
        graph.add_node(node)

        # Loop on every link
        for edge in value['relationship']:
            # Set node color by gender
            type_ = value['relationship'][edge]['type']

            # Set color by edge type
            if type_ == 'mother':
                color = 'red'
                style = 'solid'

            elif type_ == 'father':
                color = 'blue'
                style = 'solid'

            else:
                color = 'gray'
                style = 'dotted'

            # Add link to graph
            graph.add_edge(node, get_name(json_document, edge), color=color, style=style)

    # Add colors to nodes
    node_colors = []

    for key in graph:
        # Get gender
        gender = get_gender(json_document, key)

        # Set node color by gender
        if gender == 'F':
            node_colors.append('pink')

        elif gender == 'M':
            node_colors.append('cyan')

        else:
            node_colors.append('gray')

    edges = graph.edges()
    edge_colors = [graph[node1][node2]['color'] for node1, node2 in edges]
    edge_styles = [graph[node1][node2]['style'] for node1, node2 in edges]

    # Draw graph
    networkx.draw(graph, edge_color=edge_colors, node_color=node_colors, node_size=5000, style=edge_styles,
                  with_labels=True)

    # Maximize window
    manager = pyplot.get_current_fig_manager()
    manager.full_screen_toggle()

    # Show graph
    pyplot.show()


def get_gender(json_document, id_):
    for key, value in json_document.items():
        if f"{value['first_name']}\n{value['last_name']}" == id_:
            return value['gender']

    return None


def get_name(json_document, id_):
    for key, value in json_document.items():
        if key == id_:
            return f"{value['first_name']}\n{value['last_name']}"

    return None
