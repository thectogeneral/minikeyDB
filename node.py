# Import XML RPC server to receive data
from xmlrpc.server import SimpleXMLRPCServer

# Import XML RPC client to send data
import xmlrpc.client

# Import threading to update other without waiting
import threading

import nodes_config as kvNodes

def node_init(address, port, nodeId, mode, verbose):
    server = SimpleXMLRPCServer((address, port), allow_none=True, logRequests=False)

    if mode == "eventual":
        server.register_instance(EventualNode(address, port, nodeId, verbose))

    print("Node {} started on {}:{}: Using {} consistency ...".format(nodeId, address, port, mode))

    if verbose:
        print("Node {} Verbose Logginf Enables!".format(nodeId))
    else:
        print("Node {} Verbose Logging Disabled!".format(nodeId))


class EventualNode:
    def __init__(self, address, port, nodeId, verbose):
        self.address = address
        self.port = port
        self.nodeId = nodeId
        self.data = {}
        self.other_nodes = []
        self.verbose = verbose

        for node in kvNodes.nodes:
            if node.get("nodeId") == self.nodeId:
                continue

            else:
                self.other_nodes.append(xmlrpc.client.ServerProxy("http://" + node.get("address") + ":" + str(node.get("port"))))

        def put(self, key, value):
            self.data[key] = value
            t = threading.Thread(target=update_others_eventual, args=(self.other_nodes, key, value))
            t.start()

            if self.verbose:
                print("Node {} -> Key {}, value{}".format(self.nodeId, key, value))


def update_others_eventual(other_nodes, key, value):
        pass