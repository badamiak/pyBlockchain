from benchmark import Benchmark
from sys import stdout as out
from blockchain import BlockChainPacket

def test():
    
    p = BlockChainPacket()
    p.payload = "should OK"

    with Benchmark('p1 mine') as _:
        p.mine()

    p.writeToOut()
    out.flush()

    p2 = p.next()
    p2.payload = 'should OK'
    
    with Benchmark('p2 mine') as _:
        p2.mine()

    p2.writeToOut()
    out.flush()
    

    p2.payload = "should FAIL, not mined packet"
    p2.writeToOut()
    out.flush()
    

    p2.payload = 'should OK, remined'
    with Benchmark('p2 remine') as _:
        p2.mine()
    p2.writeToOut()
    out.flush()
    

    p3 = p2.next()
    p3.payload = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget gravida orci.
Etiam mattis, nibh ut scelerisque elementum, leo lorem dictum arcu, sit amet faucibus nunc augue at velit.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget fringilla arcu. Curabitur posuere nibh quam,
varius viverra felis porttitor non. Nullam sagittis et massa vel volutpat. Donec a dolor porta, fermentum lorem quis, posuere massa.'''

    with Benchmark('p3 mine') as _:
        p3.mine()
    p3.writeToOut()
    out.flush()
    

test()