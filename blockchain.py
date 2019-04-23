from block import Block


class Blockchain:
    """ The Blockchain which is made up of block data structures.

    Attributes:
        difficulty: The mining difficulty of the blockchain.
        max_nonce:  The maximum number we can store in a 32-bit int.
        target:     Hash target which determines if a block is added to the blockchain during mining.
        block:      The initial/first block (commonly called the "Genesis" block.
        head:       Pointer which points to the head of our blockchain.
    """
    difficulty = 10
    max_nonce = 2 ** 32
    target = 2 ** (256 - difficulty)
    block = Block("Genesis")
    head = block

    def add(self, block):
        block.prev_hash = self.block.compute_hash()
        block.block_num = self.block.block_num + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.max_nonce):
            if int(block.compute_hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
