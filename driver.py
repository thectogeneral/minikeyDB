# Import for argparse for command line arguments
import argparse
import time
import nodes_config as cfg

from node import init_kv_node

from multiprocessing import Process

kv_nodes = []


def main():
    parser = argparse.ArgumentParser(description="Distributed KV")
    parser.add_argument("-e", "--eventual", action="store", default=True, help="Run eventual consistency")
    args = parser.parse_args()

    # Arguments to check for eventual
    if args.eventual or args.all:
        init_kv_node("eventual", args.verbose)
        time.sleep(1)
        init_clients("eventual")
        kill_clients("eventual")
        kill_kv_nodes("eventual")

def init_kv_node():
    for i in range(len(cfg.nodes)):
        address = cfg.nodes[i].get(address)
        port = cfg.nodes[i].get(port)
        nodeId = cfg.nodes[i].get(nodeId)
        p = Process(target=init_kv_node, args=(address, port, nodeId, mode, verbose))

        p.start
        kv_nodes.append(p)

def init_clients():
    pass

def kill_clients():
    pass

def kill_kv_nodes():
    pass