from enum import Enum

import numpy as np

from commons.model.exceptions.exceptions import InvalidModelTypeException
from commons.model.linear_regression import LinearRegression


class ModelType(Enum):
    LINEAR_REGRESSION = 1

    @classmethod
    def validate(cls, model_type):
        if not any(model_type == item.name for item in cls):
            raise InvalidModelTypeException(model_type)


class ModelFactory:

    @classmethod
    def get_model(cls, model_type):
        if ModelType[model_type] == ModelType.LINEAR_REGRESSION:
            return LinearRegression
        else:
            raise InvalidModelTypeException(model_type)

    @classmethod
    def load_model(cls, model_type, model_data):
        if ModelType[model_type] == ModelType.LINEAR_REGRESSION:
            return LinearRegression(X=np.asarray(model_data['x']), y=np.asarray(model_data['y']), model_type=model_type)
        else:
            raise InvalidModelTypeException(model_type)
