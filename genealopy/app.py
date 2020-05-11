from common.constant import constant
import glob
import json
import matplotlib.pyplot as pyplot
import networkx
# import pygraphviz  # Microsoft Visual C++ 14.0 is required to build pygraphviz._graphviz extension.


def run():
    files = get_files(constant.DATA)
    list_ = list()

    for file in files:
        # Read JSON data
        with open(file, encoding='utf-8') as stream:
            list_.append(json.load(stream))

    # Create directional graph
    graph = networkx.OrderedDiGraph()

    # Loop on every JSON document
    for json_document in list_:
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
                graph.add_edge(node, get_name(list_, edge), color=color, style=style)

    # Add colors to nodes
    node_colors = []

    for key in graph:
        # Get gender
        gender = get_gender(list_, key)

        # Set node color by gender
        if gender == 'F':
            node_colors.append('pink')

        elif gender == 'M':
            node_colors.append('cyan')

        else:
            node_colors.append('gray')

    nodes = graph.nodes()

    # Add colors and styles to edges
    edges = graph.edges()
    edge_colors = [graph[node1][node2]['color'] for node1, node2 in edges]
    edge_styles = [graph[node1][node2]['style'] for node1, node2 in edges]

    if constant.DEBUG:
        print(nodes)
        print(edges)

    # Write dot file to use with graphviz
    # networkx.nx_agraph.write_dot(graph, 'data/genealopy.dot')

    # Set title
    pyplot.title('Genealopy')

    # layout = graphviz_layout(graph, prog='dot')

    # Draw graph
    networkx.draw(graph, edge_color=edge_colors, node_color=node_colors, node_size=1000, style=edge_styles,
                  with_labels=True)

    # Save to image file format
    pyplot.savefig('data/genealopy.png')

    # Maximize window
    manager = pyplot.get_current_fig_manager()
    manager.full_screen_toggle()

    # Show graph
    pyplot.show()


def get_files(path):
    files = glob.glob(path)

    return files


def get_gender(list_, id_):
    for json_document in list_:
        for key, value in json_document.items():
            if f"{value['first_name']}\n{value['last_name']}" == id_:
                return value['gender']

    return None


def get_name(list_, id_):
    for json_document in list_:
        for key, value in json_document.items():
            if key == id_:
                return f"{value['first_name']}\n{value['last_name']}"

    return None
