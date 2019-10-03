class ExceptionMessageConstants:
    INVALID_ABI_FORMAT = "Abi {} haven't valid format"


class GenericException(Exception):
    def __init__(self, msg, status_code=400):
        # Call the base class constructor with the parameters it needs
        super().__init__(msg)

        # Now for your custom code...
        self.status_code = status_code


class InvalidAbiFormatException(GenericException):
    def __init__(self, abi):
        super().__init__(ExceptionMessageConstants.INVALID_ABI_FORMAT.format(abi))
