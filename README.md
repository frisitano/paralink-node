![](https://paralink.network/images/logo-sm-home.png)

Paralink Node is responsible for executing ETL pipelines and PQL queries. The results are relayed to
all supported chains via callbacks. Paralink Node is also a dependency to the on-chain [runtime](https://github.com/paralink-network/paralink-substrate).

## Configure
Before running the node, please setup your `.env`. Copy the `.env.template` file to `.env` and modify the variables.

Migrate the DB with:

```
pipenv run alembic upgrade head
```

## Run

We suggest using Docker to run the image:

```
docker build -t paralink-node .
docker run -it -p 7424:7424 paralink-node ./paralink-node node start --host 0.0.0.0
```

Otherwise you can build the node yourself:

```
pipenv sync
./paralink-node
```

The node will by default listen on port `7424`.

The node exposes two JSON RPC methods, which will execute PQL depending on the location:
 - `execute_pql(pql_json)`: submit PQL JSON in the JSON RPC request (see [simple_get_request.py](examples/simple_get_request.py))
 - `execute_ipfs(ipfs_address, ipfs_hash)`: submit IPFS node address and IPFS hash where your PQL JSON is located (see [examples/ipfs_request.py](examples/ipfs_request.py))

Furthermore see [examples](examples) folder for additional examples on how to use the node.

## Web UI

A Web UI is accessible on [localhost:7424](http://localhost:7424). It lists all your local IPFS files as well as allows you to create your own PQL definitions, test them and save them to IPFS.

## Docs

We use Sphinx to generate docs. To auto generate docs, use:

```
pipenv run sphinx-apidoc -f -o docs/source paranode
cd docs/
pipenv run make html
```

the files will be available under `docs/build/html`.


## Tests

You can run tests with:

```
pipenv run pytest
```

