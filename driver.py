# Import for argparse for command line arguments
import argparse
import time

import nodes_config as cfg
import clients_config
import client
from node import node_init as init_kv_node

from multiprocessing import Process

kv_nodes = []
clients = []

def main():
    parser = argparse.ArgumentParser(description="MiniKeyDB")
    parser.add_argument("-e", "--eventual", action="store_true", default=True, help="Run eventual consistency")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose logging option")
    args = parser.parse_args()

    # Arguments to check for eventual
    if args.eventual or args.all:
        init_kv_nodes("eventual", args.verbose)
        time.sleep(1)
        init_clients("eventual")
        kill_clients("eventual")
        kill_kv_nodes("eventual")

def init_kv_nodes(mode, verbose):
    for i in range(len(cfg.nodes)):
        address = cfg.nodes[i].get("address")
        port = cfg.nodes[i].get("port")
        nodeId = cfg.nodes[i].get("nodeId")
        p = Process(target=init_kv_node, args=(address, port, nodeId, mode, verbose,))
        p.start()
        kv_nodes.append(p)

def init_clients(mode):
    for i in range(len(clients_config.clients)):
        if mode == "eventual":
            p = Process(target=client.eventual_consistency, args=(i,))
            p.start()
            clients.append(p)
    for c in clients:
        c.join()


def kill_clients(mode):
    count = 1
    while clients:
        p = clients.pop()
        p.terminate()
        print("Killed Client {} with consistency".format(count, mode))
        count += 1

def kill_kv_nodes(mode):
    count = 1
    while kv_nodes:
        p = kv_nodes.pop()
        p.terminate()
        print("Killed KV Node {} with {} consistency...".format(count, mode))
        count += 1

if __name__ == "__main__":
    main()