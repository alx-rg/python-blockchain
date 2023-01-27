# create a blockchain class
class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # create a new block and add it to the chain
    pass
    
  def new_transaction(self):
    # adds a new transaction to the list of transactions
    pass

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
    pass

  @property

  def last_block(self):
    # returns the last block in the chain
    pass
  