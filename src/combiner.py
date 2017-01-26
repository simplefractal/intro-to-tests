from .apis import (
    NameAPI,
    CategorizationAPI,
    GeolocationAPI
)

class Combiner(object):
    def __init__(self, tx):
        self.tx = tx

    def get_name(self):
        return NameAPI(self.tx).process()

    def get_category(self):
        return CategorizationAPI(self.tx).process()

    def get_geo(self):
        return GeolocationAPI(self.tx).process()

    def combine(self):
        name = self.get_name()
        if name["confidence"] < .65:
            return None
        else:
            geo = self.get_geo()
            data = {
                "name": name,
                "category": self.get_category()
            }
            if geo["confidence"] > .8:
                data["geo"] = geo

            return data