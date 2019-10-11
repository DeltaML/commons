import unittest

from commons.web3.delta_contracts import DeltaContract, FederatedAggregatorContract, ModelBuyerContract
from commons.web3.web3_service import Web3Service


class Web3ServiceTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true(self):
        self.assertEqual(True, True)


class W3ServiceIntegrationTest:
    ETH_URL = "http://127.0.0.1:7545"
    CONTRACT_ADDRESS = '0x5F7e7122f24b9C3EbD13F521921bde2c7D1CB1AF'

    if __name__ == '__main__':

        w3_service = Web3Service(ETH_URL)
        FA_ADDRESS = w3_service.get_accounts()[0]
        available_accounts = [account for account in w3_service.get_accounts() if account != FA_ADDRESS]
        mb_account = available_accounts.pop()
        do_accounts = [available_accounts.pop() for _ in range(5)]
        contract = DeltaContract(contract=w3_service.build_contract(address=CONTRACT_ADDRESS))
        contract.set_federated_aggregator(w3_service.eth_api.accounts[9])
        contract.set_model_buyer(mb_account)
        [contract.set_data_owner(do) for do in do_accounts]
        fa_contract = FederatedAggregatorContract(contract=w3_service.build_contract(address=CONTRACT_ADDRESS),
                                                  address=FA_ADDRESS)
        fa_contract.new_model(model_id="model_1", validators=do_accounts[1:3], trainers=do_accounts[3:],
                              model_buyer=mb_account)

        mb_contract = ModelBuyerContract(contract=w3_service.build_contract(address=CONTRACT_ADDRESS),
                                         address=mb_account)
        mb_contract.pay_for_model("model_1", 10)
