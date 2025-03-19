from injkt.uitls.configReader import ConfigReader
from injkt.values.configFile import ConfigFile
from injkt.values.rawConfig import RawConfig
from injkt.values.defaultConfigFiles import DEFAULT_CONFIG_FILES

class Configure:
    def __init__(self):
        self.DefaultConfigs = DEFAULT_CONFIG_FILES
        # damn
        self.TopLevelConfig: dict = ConfigReader(ConfigFile(self.DefaultConfigs["toplevel"])).Read().Config
        print(self.TopLevelConfig)