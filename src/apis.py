class BaseAPI(object):
    def __init__(self, tx):
        self.tx = tx

    def process(self):
        return

class NameAPI(BaseAPI):
    pass

class GeolocationAPI(BaseAPI):
    pass

class CategorizationAPI(BaseAPI):
    pass
