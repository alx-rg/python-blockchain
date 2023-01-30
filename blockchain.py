# create a blockchain class
import hashlib
import json
import time


class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.new_block(previous_hash=1, proof=100) # genesis block

  def new_block(self, proof, previous_hash=None):
    # create a new block and add it to the chain
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'proof': proof,
      previous_hash: previous_hash or self.hash(self.chain[-1]),
    }
    self.current_transactions = []
    self.chain.append(block)
    return block
  

  def new_transaction(self):
    # adds a new transaction to the list of transactions
    # create new transaction, send to the next block. 
    # transaction contains var. sender, recipient and amount
    self.current_transactions.append(
      {
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
      }
    )
    return self.last_block['index'] + 1

  def register_node(self):
    # add a new node to the list of nodes
    # add it to the network
    pass
 
  def valid_proof(self):
    # determine if submitted block to the chain solves the problem
    pass

  def valid_chain(self):
    # determine if a given blockchain is valid
    pass

  @staticmethod

  def hash(block):
    # hashes a block
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

  @property

  def last_block(self):
    # returns the last block in the chain 
    return self.chain[-1]

  def proof_of_work(self, last_proof):
    # method where concensus algorithm implemented
    #takes two parameters, self & last proof 
    proof = 0
    while self.valid_proof(last_proof, proof) is False:
      proof += 1
    return proof
  
  @staticmethod
  def valid_proof(last_proof, proof):
    # validate the proof:
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"
  