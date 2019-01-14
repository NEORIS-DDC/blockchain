from block import Block
from blockchain import Blockchain


blockchain = Blockchain()
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))
