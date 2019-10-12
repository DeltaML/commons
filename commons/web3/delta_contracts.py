class DeltaContract:
    """
    Base Wrapper to DeltaML smart contract

    """
    def __init__(self, contract, address=None):
        self._contract = contract
        self.address = address

    def get_functions(self):
        return self._contract.functions.all_functions()

    def exec(self):
        self._contract.functions.all_functions()

    def set_data_owner(self, address):
        self._contract.functions.setDataOwner(address).transact({'from': address})

    def set_federated_aggregator(self, address):
        self._contract.functions.setFederatedAggregator(address).transact({'from': address})

    def set_model_buyer(self, address):
        self._contract.functions.setModelBuyer(address).transact({'from': address})

    def get_improvement(self):
        return self._contract.functions.getImprovement()

    def calculate_fixed_payment(self, model_id, take, payees_count):
        return self._contract.functions.calculateFixedPayment(model_id, take, payees_count)

    def calculate_payment_for_validation(self, model_id):
        return self._contract.functions.calculatePaymentForValidation(model_id)

    def calculate_payment_for_orchestration(self, model_id):
        return self._contract.functions.calculatePaymentForOrchestration(model_id)


class FederatedAggregatorContract(DeltaContract):
    """
    Wrapper to Federated Aggregator contract functions
    """

    def __init__(self, contract, address):
        super().__init__(contract=contract, address=address)

    def new_model(self, model_id, validators, trainers, model_buyer):
        self._contract.functions.newModel(model_id, validators, trainers, model_buyer).transact({'from': self.address})

    def save_mse(self, model_id, mse, iter):
        self._contract.functions.saveMse(model_id, mse, iter).transact({'from': self.address})

    def save_partial_mse(self, model_id, mse, trainer, iter):
        self._contract.functions.savePartialMse(model_id, mse, trainer, iter).transact({'from': self.address})

    def calculate_contributions(self, model_id):
        self._contract.functions.calculateContributions(model_id).transact({'from': self.address})

    def pay_for_orchestration(self, model_id):
        self._contract.functions.payForOrchestration(model_id).transact({'from': self.address})


class ModelBuyerContract(DeltaContract):
    """
    Wrapper to Model Buyer contract functions
    """

    def __init__(self, contract, address):
        super().__init__(contract=contract, address=address)

    def pay_for_model(self, model_id, pay):
        self._contract.functions.payForModel(model_id, pay).transact({'from': self.address, 'value': pay})

    def finish_model_training(self, model_id):
        self._contract.functions.finishModelTraining(model_id).transact({'from': self.address})

    def check_mse_for_iter(self, model_id, iter, mse):
        return self._contract.functions.checkMseForIter(model_id, iter, mse).transact({'from': self.address})

    def check_partial_mse_for_iter(self, model_id, trainer, iter, mse):
        return self._contract.functions.checkPartialMseForIter(model_id, trainer, iter, mse).transact({'from': self.address})

    def generate_training_payments(self, model_id):
        self._contract.functions.generateTrainingPayments(model_id).transact({'from': self.address})


class DataOwnerContract(DeltaContract):
    """
    Wrapper to Data Owner contract functions
    """
    def __init__(self, contract, address):
        super().__init__(contract=contract, address=address)

    def get_do_contribution(self, model_id, data_owner_id):
        self._contract.functions.getDOContribution(model_id, data_owner_id).transact({'from': self.address})

    def calculate_payment_for_contribution(self, model_id, data_owner):
        return self._contract.functions.calculatePaymentForContribution(model_id, data_owner).transact({'from': self.address})

    def pay_for_contribution(self, model_id):
        self._contract.functions.payForContribution(model_id).transact({'from': self.address})

    def pay_for_validation(self, model_id):
        self._contract.functions.payForValidation(model_id).transact({'from': self.address})
