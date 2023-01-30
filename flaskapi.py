from uuid import uuid4
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
  """Make proof of work algorithm"""
  last_block = blockchain.last_block
  last_proof = last_block['proof']
  proof = blockchain.proof_of_work(last_proof)

  # reward for finding the proof
  blockchain.new_transaction(
    sender="0",
    recipient=node_identifier,
    amount=1,
  )

  #create new block and add it to chain
  previous_hash = blockchain.hash(last_block)
  block = blockchain.new_block(proof, previous_hash)

  response = {
    'message': "New Block Forged",
    'index': block['index'],
    'transactions': block.get('transactions', []),
    'proof': block['proof'],
    'previous_hash' : block['previous_hash']
  }
  return jsonify(response), 200

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
  app.run(host="0.0.0.0", port=5005)