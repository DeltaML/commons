from commons.model.delta_model import DeltaModel
from commons.model.prediction import Prediction
from commons.operations_utils.functions import pred_diff


class LinearRegression(DeltaModel):
    """Runs linear regression with local data or by gradient steps,
    where gradient can be passed in.

    """
    def __init__(self, X=None, y=None, requirements=None, weights=None):
        self.type = "LINEAR_REGRESSION"
        super().__init__(X, y, self.type, requirements, weights)

    def fit(self, n_iter, eta=0.01):
        """Linear regression for n_iter"""
        for _ in range(n_iter):
            gradient = self.compute_gradient()
            self.gradient_step(gradient, eta)

    def gradient_step(self, gradient, eta=0.01):
        """Update the model with the given gradient"""
        self.weights = self.weights - (eta * gradient)

    def compute_gradient(self):
        """Compute the gradient of the current model using the training set
        """
        prediction = self.predict(self.X)
        delta = prediction.values - self.y
        return delta.dot(self.X) / len(self.X)

    def predict(self, X, y_test=None):
        """Score test data"""
        values = X.dot(self.weights)
        diff = None
        if y_test is not None:
            diff = pred_diff(values, y_test)
        return Prediction(values=values, diff=diff)
