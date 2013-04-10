from google.appengine.ext import db


class Asset(db.Model):
    symbol = db.StringProperty(required=True)
    isin = db.StringProperty(required=True)
    label = db.StringProperty(required=True)
    market = db.StringProperty(required=True) # bancal, mettre une enumeration
    currency = db.StringProperty(required=True) # bancal aussi
    type = db.StringProperty(required=True) # bancal aussi

class Quote(db.Model):
    value = db.FloatProperty(required=True)
    ts = db.DateTimeProperty(required=True)
    volume = db.FloatProperty(required=True)
    asset = db.ReferenceProperty(Asset, collection_name='quotes')
    
class Portfolio(db.Model):
    assets = db.ListProperty(required=True, item_type=db.Key)
    name = db.StringProperty(required=True)
    owner = db.StringProperty(required=True)
    
    def get_assets(self):
        res = []
        for a in self.assets:
            res.append(db.get(a))
        return res
    
