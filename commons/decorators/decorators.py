from commons.operations_utils.functions import deserialize, serialize


def optimized_collection_parameter(optimization, active=False):
    def wrap(f):
        def wrapped_optimized_collection_parameter(*args):
            collection = optimization(args[2]) if active else args[2]
            params = list(args)
            params[2] = collection
            return f(*params)
        return wrapped_optimized_collection_parameter
    return wrap


def optimized_collection_response(optimization, active=False):
    def wrap(f):
        def wrapped_optimized_collection_response(*args):
            result = f(*args)
            return optimization(result) if active else result
        return wrapped_optimized_collection_response
    return wrap


def optimized_dict_collection_response(optimization, active=False):
    def wrap(f):
        def wrapped_optimized_collection_response(*args):
            result = f(*args)
            updates = list(map(lambda x: x['update'], result))
            owners = list(map(lambda x: x['data_owner_id'], result))  # TODO: Add model_id
            updates = optimization(updates) if active else updates
            return updates, owners
        return wrapped_optimized_collection_response
    return wrap


def normalize_optimized_collection_argument(active=False):
    def wrap(f):
        def wrapped_normalize_optimized_collection(*args):
            # TODO: Refactor!!!
            data = args[2].tolist() if active else args[2]
            params = list(args)
            params[2] = data
            return f(*params)
        return wrapped_normalize_optimized_collection
    return wrap


def normalize_optimized_response(active=True):
    def wrap(f):
        def wrapped_normalize_optimized_response(*args):
            result = f(*args)
            result['model']['weights'] = result['model']['weights'].tolist() if active else result['model']['weights']
            return result
        return wrapped_normalize_optimized_response
    return wrap


def data_owner_computation():
    def wrap(f):
        def wrapped_data_owner_computation(*args):
            encryption_service = args[0].encryption_service
            collection = args[2]
            public_key = args[3]
            collection = deserialize(collection, encryption_service, public_key)
            params = list(args)
            params[2] = collection
            result = f(*params)
            return serialize(result, encryption_service, public_key)
        return wrapped_data_owner_computation
    return wrap
