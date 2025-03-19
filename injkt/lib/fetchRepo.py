from injkt.values.repo import Repo
from injkt.values.repoProvider import RepoProvider
from injkt.values.config import Config

from injkt.uitls.fetchStatic import FetchStatic
from injkt.uitls.configReader import ConfigReader

from injkt.lib.configure import Configure

class FetchRepo:
    def __init__(self,RepoClass: Repo):
        self.RepoClass = Repo
        self.Configuration = Configure()