"Requester module"

from typing import Dict
import requests
class HttpRequester:
    """initial requester class"""
    def __init__(self):
        self.__url = """https://ic.unicamp.br/"""

    def request_from_page(self) -> Dict:
        """Initial requester from page"""
        response = requests.get(self.__url, timeout=100)
        print(response.text)
        print(response.status_code)
        return {
            "status_code": response.status_code,
            "html": response.text,
        }
