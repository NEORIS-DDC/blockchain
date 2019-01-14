import datetime
import hashlib


class Block:
    blockNo = 0
    next = None
    nonce = 0
    previous_hash = 0x0

    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now()

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + \
               "\nBlockNo: " + str(self.blockNo) + \
               "\nBlock Data: " + str(self.data) + \
               "\nNonce: " + str(self.nonce) +  \
               "\nTimeStamp: " + str(self.timestamp) + \
               "\n---------------------"
