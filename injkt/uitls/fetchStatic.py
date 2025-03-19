import requests

class FetchStatic:
    def __init__(self,FileUrl: str = "") -> None:
        self.FileUrl = FileUrl
    
    def Fetch(self) -> any:
        try:
            self.Request = requests.get(self.FileUrl)
            return self.Request.text
        except Exception as Error:
            return False