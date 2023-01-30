# python-blockchain

Make sure you turn on ENV mode

- `python3 -m venv venv`
- `source venv/bin/activate`
- check that it's on with `pip -V`

- When using a virtualenv, you must source the `venv/bin/activate` script each time you start a new shell, otherwise the installed Python packages will not be available
- If using a Debian based Linux distro, and the _venv_ Python library is not found or if there is an error about missing _ensurepip_, you will have to apt install `python3-venv` first

Install the python-blockchain package from the current directory\
`pip install .`

This code is a simple implementation of a blockchain in Python. The code consists of two files: `flaskapi.py` and `blockchain.py`.

The `flaskapi.py` file creates a Flask API that serves as the interface for interacting with the blockchain. The API has three routes:

`/mine:` This endpoint implements the proof of work algorithm, creates a new block and adds it to the chain.
`/transactions/new:` This endpoint creates a new transaction to be added to the next mined block.
`/chain:` This endpoint returns the full chain.
The blockchain.py file implements the Blockchain class. The class has several methods that allow adding a new block, new transactions, and registering new nodes. It also includes methods for checking if a chain is valid, resolving conflicts among chains, and implementing the proof of work algorithm.

# Testing the API using Postman

1. Install the Postman app on your computer.
2. Open the app and select the New button to create a new request.
3. For testing the /mine endpoint, select the GET method, and enter the endpoint url http://0.0.0.0:5005/mine. Click the Send button to get the response.
4. For testing the /transactions/new endpoint, select the POST method, and enter the endpoint url http://0.0.0.0:5005/transactions/new. Add a JSON body with the transaction data. Such as:

```json
{
  "sender": "Sender1",
  "recipient": "Recipient1",
  "amount": 10
}
```

5. Click the Send button to get the response.
6. For testing the /chain endpoint, select the GET method, and enter the endpoint url http://0.0.0.0:5005/chain. Click the Send button to get the response.
