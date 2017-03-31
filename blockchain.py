from hashlib import sha256

class NotMinedError(Exception):
    pass

class BlockChainPacket:
    def __init__(self,previous_hash: str = '', blockchain_hash_prefix: str = 'bd0f'):
        self._blockchain_hash_prefix = blockchain_hash_prefix
        self.order = 0
        self.message = ''
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
        return f'xo:{self.order} xp:{self.previous_hash} xf:{self.flood} xm:{self.message}'

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

def test():
    from benchmark import Benchmark
    from sys import stdout as out
    
    p = BlockChainPacket()
    p.message = "should OK"

    with Benchmark('p1 mine') as _:
        p.mine()

    p.writeToOut()
    out.flush()

    p2 = p.next()
    p2.message = 'should OK'
    
    with Benchmark('p2 mine') as _:
        p2.mine()

    p2.writeToOut()
    out.flush()
    

    p2.message = "should FAIL, not mined packet"
    p2.writeToOut()
    out.flush()
    

    p2.message = 'should OK, remined'
    with Benchmark('p2 remine') as _:
        p2.mine()
    p2.writeToOut()
    out.flush()
    

    p3 = p2.next()
    p3.message = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget gravida orci.
Etiam mattis, nibh ut scelerisque elementum, leo lorem dictum arcu, sit amet faucibus nunc augue at velit.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget fringilla arcu. Curabitur posuere nibh quam,
varius viverra felis porttitor non. Nullam sagittis et massa vel volutpat. Donec a dolor porta, fermentum lorem quis, posuere massa.'''

    with Benchmark('p3 mine') as _:
        p3.mine()
    p3.writeToOut()
    out.flush()
    

test()