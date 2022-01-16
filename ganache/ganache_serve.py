import json
from web3 import Web3

# class to deploy contract and serve it as API 
class SmartContact():
    def __init__(self, abi_file, bytecode_file):
        self.abi = ""
        self.bytecode = "" 
        self.fetch_file(abi_file, bytecode_file)

        # Set up web3 connection with Ganache
        self.ganache_url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.ganache_url))

        # account setup
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]

        # deploy contract 
        self.contract = self.create_contract()


    
    def fetch_file(self, abi_file, bytecode_file):
        """
        Fetch json files and make objects 
        """
        with open(abi_file) as f:
            self.abi = json.load(f)

        with open(bytecode_file) as f:
            self.bytecode = json.load(f)['object']

    
    def create_contract(self):
        """
        contact deployment over blockchain
        """
        contract_setup = self.web3.eth.contract(abi=self.abi, bytecode=self.bytecode)

        # # Submit the transaction that deploys the contract
        tx_hash = contract_setup.constructor().transact()

        # # Wait for the transaction to be mined, and get the transaction receipt
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)

        contract = self.web3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=self.abi
            )
        
        return contract

    # 
    # 
    #
    # python methods for calling & transacting contract
    def addUser(self, id, bool):
        tx_hash = self.contract.functions.addDoc(id, bool).transact()
        self.web3.eth.waitForTransactionReceipt(tx_hash)

    def getUser(self, id):
        return self.contract.functions.getDoc(id).call()
    
contract = SmartContact(abi_file='./ganache/contract_abi.json', bytecode_file='./ganache/contract_bytecode.json')

if __name__ == '__main__':
    # 
    contract.addUser(1, True)
    contract.addUser(2, True)
    contract.addUser(3, True)
    print(
        'user 0', contract.getUser(0), '\n',
        'user 1', contract.getUser(1), '\n',
        'user 2', contract.getUser(2), '\n',
        'user 3', contract.getUser(3), '\n',
    )