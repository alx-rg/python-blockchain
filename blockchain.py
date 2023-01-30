# create a blockchain class
import hashlib
import json
import time


class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.nodes = set()
    self.new_block(previous_hash=1, proof=100) # genesis block

  def new_block(self, proof, previous_hash=None):
    # create a new block and add it to the chain
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }
    self.current_transactions = []
    self.chain.append(block)
    return block
  

  def new_transaction(self, sender, recipient, amount):
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

  def register_node(self, address):
    # add a new node to the list of nodes
    # add it to the network
    self.nodes.add(address)

  def valid_chain(self, chain):
    """Determine if a given blockchain is valid."""
    last_block = chain[0] # set the first block in the chain as the `last_block`
    current_index = 1 # start iterating from the second block
    
    # iterate through the rest of the blocks in the chain
    while current_index < len(chain):
      block = chain[current_index] # set the current block
      
      # check if the current block's `previous_hash` is equal to the hash of the `last_block`
      if block['previous_hash'] != self.hash(last_block):
        return False # if not, return False
      
      # check if the `proof` of the current block is valid
      if not self.valid_proof(last_block['proof'], block['proof']):
        return False # if not, return False
      
      last_block = block # set the current block as the `last_block` for the next iteration
      current_index += 1 # increment the index
      
    return True # if all checks pass, return True


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
  