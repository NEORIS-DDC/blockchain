from block import Block


class Blockchain:

    maxNonce = 2**32
    diff = 20
    target = 2**(256-diff)

    block = Block("Genesis")
    head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = block

    def mine(self, block):
        for _ in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
