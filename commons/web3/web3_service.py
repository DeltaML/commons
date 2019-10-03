import json
from web3 import Web3

from commons.web3.exceptions import InvalidAbiFormatException


class Web3Service:

    def __init__(self, url):
        self.http_provider = Web3.HTTPProvider(url)
        self.w3 = Web3(self.http_provider).eth

    @staticmethod
    def _load_abi(abi_path):
        with open(abi_path) as f:
            info_json = json.load(f)

        if not "abi" in info_json:
            raise InvalidAbiFormatException(abi_path)
        return info_json["abi"]

    def build_contract(self, abi_path, address):
        abi = self._load_abi(abi_path)
        return self.w3.contract(address=address, abi=abi)

    def get_accounts(self):
        return self.w3.accounts
