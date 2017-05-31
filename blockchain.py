from hashlib import sha256

class NotMinedError(Exception):
    pass

class BlockChainPacket:
    def __init__(self,previous_hash: str = '', blockchain_hash_prefix: str = 'bd0f'):
        self._blockchain_hash_prefix = blockchain_hash_prefix
        self.order = 0
        self.payload : str = ''
        self.flood = 0
        self.previous_hash = previous_hash
        self.current_hash = ''
        
    def next(self):
        if not self.isCorrect():
            self.mine()
            
        new = BlockChainPacket(self.current_hash)
        new.order += 1
        return new

    def isMined(self) -> bool:
        return True if self.current_hash.startswith(self._blockchain_hash_prefix) else False
        
    def isCorrect(self) -> bool:
        return True if self.current_hash == sha256(str(self).encode()).hexdigest() and self.isMined() else False

    def __str__(self):
        return f'xo:{self.order} xph:{self.previous_hash} xf:{self.flood} xp:{self.payload}'

    def writeToOut(self):
        print(f'{"OK  " if self.isCorrect() else "FAIL"}\t{self.current_hash} -> {str(self)}')

    def mine(self):
        self.flood = 0
        while not (self.isCorrect()):
            self.flood += 1
            m = sha256(str(self).encode())
            self.current_hash = m.hexdigest()
            correct = self.isCorrect()
            mined = self.isMined()