from datetime import datetime
from hashlib import sha256

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce=0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self. timestamp = datetime.now()
    self.hash = self.generate_hash()

  def print_contents(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    print("previous hash:", self.previous_hash)
    
  def generate_hash(self):
    # hash the blocks contents
    block_contents = str(self.timestamp)+str(self.transactions)+str(self.nonce)+str(self.previous_hash)
    
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True

  def proof_of_work(self,block, difficulty=2):
    self.proof=block.generate_hash()
    while(self.proof[:2] != '0'*difficulty):
      block.nonce += 1
      self.proof= block.generate_hash() 
    block.nonce = 0
    return self.proof

if __name__ == '__main__':

  print(datetime.now())
  # text to hash
  text = 'I am excited to learn about blockchain!'

  # print result
  hash_result = sha256(text.encode())
  print(hash_result.hexdigest())

  transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
  transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
  transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
  transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
  transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
  transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

  mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

  # add your code below
  my_transaction = {
  'amount': '250',
  'sender': 'Jack',
  'receiver': 'Al'}

  mempool.append(my_transaction)

  print (mempool)

  block_transactions = [transaction1, transaction2, transaction3]

  print (block_transactions)
  
  #test all the methods
  block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
  block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
  block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
  fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

  local_blockchain = Blockchain()

  local_blockchain.print_blocks()

  local_blockchain.add_block(block_one_transactions)
  local_blockchain.add_block(block_two_transactions)
  local_blockchain.add_block(block_three_transactions)

  local_blockchain.print_blocks()

  local_blockchain.chain[2].transactions=fake_transactions

  local_blockchain.validate_chain()