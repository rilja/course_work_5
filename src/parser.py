from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """Abstract class for working with websites API"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_employers(self, count):
        pass


class HH(Parser):
    """class for working with HeadHunter API"""

    def __init__(self):
        self.area = 113  # Russia by default
        self.sort = 'by_vacancies_open'  # sort by top open vacancies
        self.url = 'https://api.hh.ru/employers'  # basic url
        self.employers = []
        self.params = {'area': self.area, 'sort_by': self.sort, 'per_page': 1}

    def load_employers(self, count=1):
        """returns list with employers"""
        self.params['per_page'] = count  # adding vacancies count to url
        response = requests.get(self.url, params=self.params).json()['items']
        return response
