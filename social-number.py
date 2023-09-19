import requests
from randommer import Randommer

randommer = Randommer()
class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        self.api_key = api_key
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        pass
        base_urel = randommer.base_url
        url = base_urel + "SocialNumber"
        headers = {
            "X-Api-Key":self.api_key
        }
        r = requests.get(url , headers=headers)
        return r.json()
key="f1ab06cd2da14928a4f4299e85162d76"
social=SocialNumber(key)
print(social.get_SocialNumber())
