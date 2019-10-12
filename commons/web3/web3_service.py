import json
from web3 import Web3

from commons.web3.exceptions import InvalidAbiFormatException


class CurrencyService:

    def __init__(self, w3):
        self.w3 = w3

    def to_wei(self, value, currency):
        """
        Returns the value in the denomination specified by the currency argument converted to wei.
        :param value:
        :param currency:
        :return:
        """
        return self.w3.toWei(value, currency)

    def from_wei(self, value, currency):
        """
        Returns the value in wei converted to the given currency.
        The value is returned as a Decimal to ensure precision down to the wei.
        :param value:
        :param currency:
        :return:
        """
        return self.w3.fromWei(value, currency)


class Web3Service:
    DEFAULT_ABI_PATH = 'abi.json'

    def __init__(self, url):
        self.http_provider = Web3.HTTPProvider(url)
        self.w3 = Web3(self.http_provider)
        self.eth_api = self.w3.eth
        self.currency_service = CurrencyService(self.w3)

    @staticmethod
    def _load_abi(abi_path):
        with open(abi_path) as f:
            info_json = json.load(f)

        if not "abi" in info_json:
            raise InvalidAbiFormatException(abi_path)
        return info_json["abi"]

    def build_contract(self, address, abi_path=DEFAULT_ABI_PATH):
        """
        Build contract from api definition and locate in address param
        :param abi_path:
        :param address:
        :return:
        """
        abi = self._load_abi(abi_path)
        return self.eth_api.contract(address=address, abi=abi)

    def get_accounts(self):
        """
        Get all accounts
        :return:
        """
        return self.eth_api.accounts

    def transform_to_wei(self, value, currency):
        """
        Transform value to wei format using currency
        :param value:
        :param currency:
        :return:
        """
        return self.currency_service.to_wei(value, currency)
