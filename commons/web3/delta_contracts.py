class DeltaContract:
    """
    Base Wrapper to DeltaML smart contract

    """
    def __init__(self, contract):
        self._contract = contract

    def get_functions(self):
        return self._contract.all_functions()

    def exec(self):
        self._contract.all_functions()

    def set_data_owner(self, address):
        self._contract.functions.setDataOwner(address)

    def set_federated_aggregator(self, address):
        self._contract.functions.setFederatedAggregator(address)

    def set_model_buyer(self, address):
        self._contract.functions.setModelBuyer(address)

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
    def new_model(self, model_id, validators, trainers, model_buyer):
        self._contract.functions.newModel(model_id, validators, trainers, model_buyer)

    def save_mse(self, model_id, mse, iter):
        self._contract.functions.saveMse(model_id, mse, iter)

    def save_partial_mse(self, model_id, mse, trainer, iter):
        self._contract.functions.savePartialMse(model_id, mse, trainer, iter)

    def calculate_contributions(self, model_id):
        self._contract.functions.calculateContributions(model_id)

    def pay_for_orchestration(self, model_id):
        self._contract.functions.payForOrchestration(model_id)


class ModelBuyerContract(DeltaContract):
    """
    Wrapper to Model Buyer contract functions
    """
    def pay_for_model(self, model_id, pay):
        self._contract.functions.payForModel(model_id, pay)

    def finish_model_training(self, model_id):
        self._contract.functions.finishModelTraining(model_id)

    def check_mse_for_iter(self, model_id, iter, mse):
        return self._contract.functions.checkMseForIter(model_id, iter, mse)

    def check_partial_mse_for_iter(self, model_id, trainer, iter, mse):
        return self._contract.functions.checkPartialMseForIter(model_id, trainer, iter, mse)


class DataOwnerContract(DeltaContract):
    """
    Wrapper to Data Owner contract functions
    """
    def get_do_contribution(self, model_id, data_owner_id):
        self._contract.functions.getDOContribution(model_id, data_owner_id)

    def calculate_payment_for_contribution(self, model_id, data_owner):
        return self._contract.functions.calculatePaymentForContribution(model_id, data_owner)

    def pay_for_contribution(self, model_id):
        self._contract.functions.payForContribution(model_id)

    def pay_for_validation(self, model_id):
        self._contract.functions.payForValidation(model_id)
