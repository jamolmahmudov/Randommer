import requests
from randommer import Randommer
randommer = Randommer()
class Finance(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key = api_key
    def get_crypto_address_types(self) -> list:

        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        pass
        base_url=randommer.base_url
        url=base_url+"Finance/CryptoAddress/Types"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url,headers=heardes)

        return r.json()

    def get_crypto_address(self, crypto_type: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        pass
        base_url=randommer.base_url
        url=base_url+"Finance/CryptoAddress"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "cryptoType":crypto_type
        }
        r=requests.get(url,params=payload, headers=heardes)
        return r.json()

    def get_countries(self) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        pass
        base_url=randommer.base_url
        url=base_url+"Finance/Countries"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url,headers=heardes)
        return r.json()

    def get_iban_by_country_code(self, country_code: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        pass
        base_url=randommer.base_url
        url=base_url+f"Finance/Iban/{country_code}"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "countryCode ":country_code
        }

        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
key="f1ab06cd2da14928a4f4299e85162d76"
finace=Finance(key)
print(finace.get_iban_by_country_code("SA"))