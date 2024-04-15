import xmlrpc.client

import random
import time

import nodes_config
import clients_config


def eventual_consistency(clientId):
    print("Client {} started with eventual consistency".format(clientId))

    node1 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[0].get("address")
                                      + ":" + str(nodes_config.nodes[0].get("port")))

    node2 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[1].get("address")
                                      + ":" + str(nodes_config.nodes[1].get("port")))

    node3 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[2].get("address")
                                      + ":" + str(nodes_config.nodes[2].get("port")))

    input_data = {}
    with open(clients_config.clients[clientId].get("test_file"), "r") as f:
        for line in f:
            key, value = line.split(":")
            input_data[key] = value.strip("\n")

    time.sleep(1)


    for k, v in input_data.items():
        node1.put(str(k), str(v))
        print("Client {} Node 1 - PUT {}, {}".format(clientId, k, v))
        delay = random.uniform(0.5, 1.2)
        print("Client {} Delay: {} seconds".format(clientId, delay))
        time.sleep(delay)
        print("Client {} Node 1 - GET {} -> Result {} --> Expected {}".format(clientId, k, node1.get(k), v))
        print("Client {} Node 2 - GET {} -> Result {} --> Expected {}".format(clientId, k, node2.get(k), v))
        print("Client {} Node 3 - GET {} -> Result {} --> Expected {}\n".format(clientId, k, node3.get(k), v))

    for k, v in input_data.items():
        print("Client {} Node 1 - REMOVE {} -> Result {}".format(clientId, k, node1.remove(k)))
        delay = random.uniform(0.5, 1.2)
        print("Client {} Delay: {} seconds".format(clientId, delay))
        time.sleep(delay)
        print("Client {} Node 1 - GET {} -> Result {} --> Expected {}".format(clientId, k, node1.get(k), "NULL"))
        print("Client {} Node 2 - GET {} -> Result {} --> Expected {}".format(clientId, k, node2.get(k), "NULL"))
        print("Client {} Node 3 - GET {} -> Result {} --> Expected {}\n".format(clientId, k, node3.get(k), "NULL"))