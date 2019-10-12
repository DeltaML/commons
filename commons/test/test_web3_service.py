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


class W3ServiceIntegrationTest(unittest.TestCase):
    ETH_URL = None
    CONTRACT_ADDRESS = None

    def setUp(self):
        self.ETH_URL = "http://127.0.0.1:7545"
        self.CONTRACT_ADDRESS = '0xb13931064070e3794079F36b667e2DAfDA40FfEC'
        self.model_id = "model_1"

    def test_true(self):
        w3_service = Web3Service(self.ETH_URL)
        all_accounts = w3_service.get_accounts()
        fa_address = all_accounts[0]
        mb_account = all_accounts[1]
        available_accounts = [account for account in all_accounts if account not in [fa_address, mb_account]]
        do_accounts = [available_accounts.pop() for _ in range(5)]
        contract = DeltaContract(contract=w3_service.build_contract(address=self.CONTRACT_ADDRESS))
        contract.set_federated_aggregator(fa_address)
        contract.set_model_buyer(mb_account)
        [contract.set_data_owner(do) for do in do_accounts]
        fa_contract = FederatedAggregatorContract(contract=w3_service.build_contract(address=self.CONTRACT_ADDRESS),
                                                  address=fa_address)
        fa_contract.new_model(model_id=self.model_id,
                              validators=do_accounts[1:3],
                              trainers=do_accounts[3:],
                              model_buyer=mb_account)

        mb_contract = ModelBuyerContract(contract=w3_service.build_contract(address=self.CONTRACT_ADDRESS),
                                         address=mb_account)
        mb_contract.pay_for_model(self.model_id, 10)
        fa_contract.save_mse(self.model_id, 10, 1)
        mb_contract.finish_model_training(self.model_id)
        mb_contract.generate_training_payments(self.model_id)

