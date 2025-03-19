from injkt.values.repoProvider import RepoProvider

class Repo:
    def __init__(self,Provider: RepoProvider,Name: str = "",Owner: str = ""):
        self.Name = Name
        self.Owner = Owner
        self.Provider = Provider