
class PhantomException(Exception):
    pass


class PhantomParameterException(PhantomException):
    pass


class PhantomHTTPException(PhantomException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
