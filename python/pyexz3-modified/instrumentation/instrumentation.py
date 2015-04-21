class Instrumentation:

    def __init__(self):
        self.node_name = ""
        self.next_node = None

    def print_connected_nodes(self):

        current_node = self

        while current_node != None:
            if current_node.next_node != None:
                print(current_node.node_name, " -> ", end="")
            else:
                print(current_node.node_name)

            current_node = current_node.next_node

