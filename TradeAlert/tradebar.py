from dataclasses import dataclass
from datetime import datetime
import enum
from . import resolution
# This class represents the HLOC data across a defined period (the 'resolution).



@dataclass
class TradeBar():
    
    def __init__(self):
        self.epic       :str
        self.timestamp  :datetime
        self.resolution :str
        self.high       :int
        self.low        :int
        self.open       :int
        self.close      :int



