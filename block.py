import datetime
import hashlib


class Block:
    """ The Block data structure which is the building block (pun intended) of the blockchain

    Attributes:
        block_num:  The number of the block.
        data:       The data of the block.
        next:       Pointer to the next block.
        hash:       A hash is a function that converts data into a number within a certain range.
        nonce:      A nonce is a number that is used once.
        prev_hash:  The hash of the previous block.
        timestamp:  The timestamp of the block when it was created.
    """
    block_num = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prev_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def compute_hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_num).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.compute_hash()) + "\nPrevious Hash: " + str(self.prev_hash) + "\nBlockNo: " + \
               str(self.block_num) + "\nBlock Data: " + str(self.data) + "\nHashes: " + \
               str(self.nonce) + "\n--------------"
