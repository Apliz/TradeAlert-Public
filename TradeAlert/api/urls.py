from enum import Enum

class Url(Enum):
    ACCOUNT = 'https://demo-api.ig.com/gateway/deal/accounts'
    HISTORY = 'https://demo-api.ig.com/gateway/deal/history'
    SESSION = 'https://demo-api.ig.com/gateway/deal/session'
    PRICES = 'https://demo-api.ig.com/gateway/deal/prices'

