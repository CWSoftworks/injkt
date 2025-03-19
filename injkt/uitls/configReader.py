from injkt.values.configFile import ConfigFile
from injkt.values.rawConfig import RawConfig

class ConfigReader:
    def __init__(self,File: ConfigFile):
        self.File = File
        self.FileLocation = self.File.Location
        self.Config: RawConfig

    def Read(self):
        try:
            with open(self.FileLocation,"r") as File:
                self.Config.RawConfig = File.read()
                File.close()
            self.Config.ToDict()
            return self.Config
        except Exception as Error:
            return False