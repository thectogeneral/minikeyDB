# Import XML RPC server to receive data
from xmlrpc.server import SimpleXMLRPCServer

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
    pass