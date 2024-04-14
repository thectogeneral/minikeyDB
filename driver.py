# Import for argparse for command line arguments
import argparse
import time

from node import init_kv_node

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
    pass

def init_clients():
    pass

def kill_clients():
    pass

def kill_kv_nodes():
    pass