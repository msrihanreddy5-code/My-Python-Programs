import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hashlib.sha256((data+prev_hash).encode()).hexdigest()

b1 = Block("Genesis", "0")
b2 = Block("Transaction", b1.hash)
print(b1.hash, b2.hash)
