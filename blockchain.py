import datetime
import hashlib
import random
import urllib.request
from time import sleep
baseURL1 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field1='
baseURL2 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field2='
baseURL3 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field3='
baseURL4 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field4='
baseURL5 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field5='
baseURL6 = 'https://api.thingspeak.com/update?api_key=OBCSL71VM27907ZL&field6='

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def _init_(self, data):
        self.data = data

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

    def _str_(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
class Sensors:

    def sendData(self):
        n=0  
        while n<10:
            spo2 = random.randint(60, 110)
            bp_dystolic = random.randint(110,150)
            temp = random.uniform(95.0,104.0)
            ecg = random. randint(120,200)
            eeg = random.uniform(0.5,30.0)
            bp_systolic = random.randint(80,89)
            f1 = urllib.request.urlopen(baseURL1 + str(bp_systolic))
            sleep(15)
            f2 = urllib.request.urlopen(baseURL2 + str(bp_dystolic))
            sleep(15)
            f3 = urllib.request.urlopen(baseURL3 + str(spo2))
            sleep(15)
            f4 = urllib.request.urlopen(baseURL4 + str(temp))
            sleep(15)
            f5 = urllib.request.urlopen(baseURL5 + str(ecg))
            sleep(15)
            f6 = urllib.request.urlopen(baseURL6 + str(eeg))
            sleep(15)
            n=n+1
            x=str(bp_systolic)
            blockchain.mine(Block("bp_systolic "+x))
            x=str(bp_dystolic)
            blockchain.mine(Block("bp_dystolic "+x))
            x=str(spo2)
            blockchain.mine(Block("spo2 "+x))
            x=str(temp)
            blockchain.mine(Block("temp "+x))
            x=str(ecg)
            blockchain.mine(Block("ecg "+x))
            x=str(eeg)
            blockchain.mine(Block("eeg "+x))
            f1.read()
            f1.close()
            f2.read()
            f2.close()
            f3.read()
            f3.close()
            f4.read()
            f4.close()
            f5.read()
            f5.close()
            f6.read()
            f6.close()
metrics = Sensors()
metrics.sendData()

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
