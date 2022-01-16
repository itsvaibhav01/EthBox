import json
from web3 import Web3

# secret
with open('./infura/secret.json') as f:
    SECRET = json.load(f)

class SmartContract():
    def __init__(self, abi_file, wallet_file):
        self.fetch_file(abi_file, wallet_file)

        # setup web3 from infura
        self.infura = SECRET['url']
        self.web3 = web3 = Web3(Web3.HTTPProvider(self.infura))

        # account setup
        self.private_key = web3.eth.account.decrypt(self.keystore, SECRET['pass']) 
        self.account = web3.eth.account.privateKeyToAccount(self.private_key)
        self.web3.eth.defaultAccount = self.account

        # contract 
        self.contract = web3.eth.contract(address=SECRET['contract_address'], abi=self.abi)


    def fetch_file(self, abi_file, wallet_file):
        """
        Fetch json files and make objects 
        """
        with open(abi_file) as f:
            self.abi = json.load(f)

        with open(wallet_file) as f:
            self.keystore = json.load(f)

    
    # contract methods 
    def getUser(self, id):
        "get bool at ID"
        return self.contract.functions.getDoc(id).call({'from':self.account.address})
    
    def addUser(self, id, bool):
        "add/update object in contract"
       
        _txn = self.contract.functions.addDoc(id, bool).buildTransaction(
            {
            'from': self.account.address,
            'nonce': self.web3.eth.getTransactionCount(self.account.address),
            'gas': 1728712,
            'gasPrice': self.web3.toWei('25', 'gwei')
            }
        )

        signed = self.account.signTransaction(_txn)
        self.web3.eth.sendRawTransaction(signed.rawTransaction)

        # # WAIT FOR CONFIRMATION
        # _txn_receipt = self.web3.eth.waitForTransactionReceipt(signed.hash)
        # return _txn_receipt['transactionHash']

        # # transaction hash
        return signed.hash.hex()  


contract = SmartContract(abi_file='./infura/contract_abi.json', wallet_file='./infura/wallet.json')

if __name__ == '__main__':
    # 
    contract.addUser(1, True)
    contract.addUser(2, True)
    print(
        'user 0', contract.getUser(0), '\n',
        'user 1', contract.getUser(1), '\n',
        'user 2', contract.getUser(2), '\n',
    )