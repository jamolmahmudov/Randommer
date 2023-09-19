import requests
from randommer import Randommer

randommer = Randommer()
class Name(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key = api_key
    def get_name(self, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        pass
        base_url=randommer.base_url      
        url=base_url+"Name"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "nameType":nameType,
            "quantity":quantity
        }
        r=requests.get(url,params=payload, headers=heardes)
        return r.json()
    
    def get_name_suggestions(self, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        pass
        base_url=randommer.base_url      
        url=base_url+"Name/Suggestions"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "startingWords":startingWords
        }
        r=requests.get(url,params=payload, headers=heardes)
        return r.json()
    
    def get_name_cultures(self) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        pass
        base_url=randommer.base_url      
        url=base_url+"Name/Cultures"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url, headers=heardes)
        return r.json()
key="f1ab06cd2da14928a4f4299e85162d76"
name=Name(key)
print(name.get_name_cultures())