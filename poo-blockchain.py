import hashlib
from datetime import datetime

class Block():
    
    
    def __init__(self, id_block, block_info, nonce, hash_prev, timestamp):
        self.id_block = id_block
        self.block_info = block_info #block_info viene desde main() que ejecuta mine_block() que contiene en su primer parametro block_information
        self.nonce = nonce
        self.hash_prev = hash_prev
        self.timestamp = timestamp
    def __str__(self):
        return "[Id: {0} ,Hash Info: {1}, Nonce: {2}, Hash Previo: {3}, Timestamp: {4}]".format(self.id_block,self.block_info,self.nonce, self.hash_prev, self.timestamp)

transacciones = []



def genesis_block(block):
    transacciones.append(block)

    
def mine_block(block):
    transacciones.append(block)

def print_transactions():
    for x in transacciones:
        print (x)


def main():
    #block_information = hashlib.sha256((input("Ingrese su informacion: ")).encode()).hexdigest()
    block_information = input("Ingrese sus datos a encryptar") 
    now = datetime.now()
    hash_previo = hashlib.sha256((f"{transacciones}").encode()).hexdigest()
    id_next = transacciones[-1].id_block + 1
    nonce = 0
    while True:
        hash_bloque = hashlib.sha256((block_information + hash_previo + str(transacciones[-1].nonce)).encode()).hexdigest()
        if hash_bloque.startswith("0000"): # Increase target to two leading zeros
            print("Has minado un bloque", hash_bloque)
            mine_block(Block(id_next,hash_bloque, nonce, hash_previo, now))
            print_transactions()
            main()
            return nonce, hash_bloque
        nonce += 1
        id_next = transacciones[-1].id_block + 1
        ########---------block info------nonce---previous_hash---time
        mine_block(Block(id_next,hash_bloque, nonce, hash_previo, now))
        
    
    

if __name__ == "__main__":
    now = datetime.now()
    genesis_block(Block(0, "Welcom to StreamChain, this is Block Genesis", 0, hashlib.sha256(("None").encode()).hexdigest(), now))
    main()
    