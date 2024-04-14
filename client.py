# Import xml rpc client
import xmlrpc.client

# Import XML RPC client to connect to kv nodes and test
import random


# Import the configurations for the kv nodes
import nodes_config

# Import the configuration for the clients
import clients_config

# Create artificial delays
import time

def eventual_consistency(clientId):
    print("Client {} started with eventual consistency".format(clientId))

    # Create a connection to node 1
    node1 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[0].get("address")
                                      + ":" + str(nodes_config.nodes[0].get("port")))

    # Create a connection to node 2
    node2 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[1].get("address")
                                      + ":" + str(nodes_config.nodes[1].get("port")))
    # Create a connection to node 3
    node3 = xmlrpc.client.ServerProxy("http://" + nodes_config.nodes[2].get("address")
                                      + ":" + str(nodes_config.nodes[2].get("port")))
    # Create a dictionary to put test data into
    input_data = {}
    # Open the file with the tests
    with open(clients_config.clients[clientId].get("test_file"), "r") as f:
        # For each line
        for line in f:
            # Get a key, value by splitting at the :
            key, value = line.split(":")
            # Set the dictionary value and strip off the \n at the end of the line
            input_data[key] = value.strip("\n")

    time.sleep(1)

    # Loop though the items in the dictionary for puts
    for k, v in input_data.items():
        # Put the key/value into the first node
        node1.put(str(k), str(v))
        # Print out the statement confirming
        print("Client {} Node 1 - PUT {}, {}".format(clientId, k, v))
        # Create a random delay
        delay = random.uniform(0.5, 1.2)
        # Print out specified delay
        print("Client {} Delay: {} seconds".format(clientId, delay))
        # Sleep delay time
        time.sleep(delay)
        # Do get values for each of the three nodes with key and value then confirm with expected value
        print("Client {} Node 1 - GET {} -> Result {} --> Expected {}".format(clientId, k, node1.get(k), v))
        print("Client {} Node 2 - GET {} -> Result {} --> Expected {}".format(clientId, k, node2.get(k), v))
        print("Client {} Node 3 - GET {} -> Result {} --> Expected {}\n".format(clientId, k, node3.get(k), v))

    # Loop through some items in the dictionary for removes
    for k, v in input_data.items():
        # Put the key/value into the first node
        print("Client {} Node 1 - REMOVE {} -> Result {}".format(clientId, k, node1.remove(k)))
        # Create delay for waiting
        delay = random.uniform(0.5, 1.2)
        # Print out delay to show
        print("Client {} Delay: {} seconds".format(clientId, delay))
        # Sleep for desired delay
        time.sleep(delay)
        # Print out more get statements that should show that values were removed
        print("Client {} Node 1 - GET {} -> Result {} --> Expected {}".format(clientId, k, node1.get(k), "NULL"))
        print("Client {} Node 2 - GET {} -> Result {} --> Expected {}".format(clientId, k, node2.get(k), "NULL"))
        print("Client {} Node 3 - GET {} -> Result {} --> Expected {}\n".format(clientId, k, node3.get(k), "NULL"))