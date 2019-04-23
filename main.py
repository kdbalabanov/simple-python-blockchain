from block import Block
from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()
    num_blocks = 10

    for i in range(num_blocks):
        blockchain.mine(Block('Block: ' + str(i + 1)))