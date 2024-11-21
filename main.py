import hashlib

class YuvrajCoinBlock:
    def __init__(self, prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-" .join(transaction_list) + "-" + prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Jamal sends 5.2 YuvrajCoin to Sarki"

b1 = YuvrajCoinBlock("Initial Block",t1)
print(b1.block_hash)

t2 = " Sarki sends 0.6 YuvrajCoin to Vedant"

b2 = YuvrajCoinBlock(b1.block_hash, t2)
print(b2.block_hash)