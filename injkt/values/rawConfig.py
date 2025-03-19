import json

class RawConfig:
    def __init__(self):
        self.RawConfig: str
        self.Config: dict
    
    def ToDict(self):
        self.Config = json.loads(self.RawConfig)