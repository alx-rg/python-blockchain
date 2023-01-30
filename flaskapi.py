from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

# Initializing blockchain
blockchain = Blockchain()

# Creating the app node
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-','')


@app.route('/mine', methods=['GET'])
def mine():
  return "Mining a new Block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
  value = request.get_json()
  required = ['sender', 'recipient', 'amount']
  if not all(k in value for k in required):
    return 'Missing values', 400

  #creating a new transaction
  index = blockchain.new_transaction(value['sender'], value['recipient'], value['amount'])
  response = {'message': f'Transaction will be added to Block {index}'}
  return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
  response = {
    'chain' : blockchain.chain,
    'length' : len(blockchain.chain)
  }
  return jsonify(response), 200

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)