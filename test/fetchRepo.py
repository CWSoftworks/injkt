from injkt.lib.fetchRepo import FetchRepo
from injkt.values.repo import Repo
from injkt.values.repoProvider import RepoProvider

if __name__ == "__main__":
    print("Starting")
    ProviderClass = RepoProvider()
    ProviderClass.ProviderName = "github"
    RepoClass = Repo(ProviderClass,"CWSoftworks","injkt")
    FetchRepo(RepoClass)
