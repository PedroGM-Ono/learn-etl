"Requester module"

import requests
class HttpRequester:
    """initial requester class"""
    def __init__(self):
        self.__url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'

    def request_from_page(self):
        """Initial requester from page"""
        response = requests.get(self.__url, timeout=10)
        print(response)
