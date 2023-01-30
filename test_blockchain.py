from blockchain import Blockchain

blockchain = Blockchain()

# Add transactions
blockchain.new_transaction("John", "Jane", 100)
blockchain.new_transaction("Jane", "John", 50)
blockchain.new_transaction("Jane", "Alice", 75)

# Add a block to the chain
proof = blockchain.proof_of_work(blockchain.last_block["proof"])
blockchain.new_block(proof)

# Check the current chain
print(blockchain.chain)

# Check the validity of the chain
print(blockchain.valid_chain(blockchain.chain))