# MinikeyDB: Distributed Key-Value Store

MinikeyDB is a simple distributed key-value store system designed for educational purposes and experimentation with eventual consistency. It allows users to store and retrieve key-value pairs across multiple nodes in a distributed system.

## Features

- **Distributed Architecture**: MinikeyDB utilizes a distributed architecture where key-value pairs are stored across multiple nodes.
- **Eventual Consistency**: The system employs eventual consistency, ensuring that all updates are eventually propagated to all nodes in the system.
- **Client-Server Model**: Clients interact with the key-value store system through simple client scripts.
- **Simple Configuration**: Configuration files are provided for easy setup and customization of nodes and clients.

## Components

MinikeyDB consists of the following components:

1. **Node**: Each node represents a server in the distributed system. Nodes store key-value pairs and communicate with each other to maintain eventual consistency.
2. **Client**: Clients interact with the key-value store system by performing operations such as putting, getting, and removing key-value pairs.

## Running MinikeyDB

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup

1. Clone the MinikeyDB repository to your local machine:

```sh
git clone https://github.com/itz-salemm/minikeyDB.git
```

2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

### Configuration

1. Configure the nodes in the `nodes_config.py` file. Specify the address, port, and node ID for each node in the system.
2. Configure the clients in the `clients_config.py` file. Specify the test file path for each client.

### Running Nodes

To start the nodes in the distributed system, run the following command:

```sh
python driver.py -e
```

The `-e` flag specifies eventual consistency mode. You can also use the `-v` flag for verbose logging.

This command initializes clients and performs operations such as putting, getting, and removing key-value pairs. Adjust the configuration in `clients_config.py` to specify test files and customize client behavior.

### Monitoring

You can monitor the system by observing the console output for nodes and clients. Verbose logging can be enabled for detailed information.
