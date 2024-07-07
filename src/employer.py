from abc import ABC, abstractmethod

import requests


class BaseEmployer(ABC):
    """Abstract class for creating Employer from API"""
    @abstractmethod
    def __init__(self, identification, name, url, vacancies_url, open_vacancies):
        self.id = identification
        self.name = name
        self.url = url
        self.vacancies_url = vacancies_url
        self.open_vacancies = open_vacancies

    @classmethod
    def cast_to_object_list(cls, data):
        pass


class Employer(BaseEmployer):
    def __init__(self, identification, name, url, vacancies_url, open_vacancies):
        super().__init__(identification, name, url, vacancies_url, open_vacancies)

    @classmethod
    def cast_to_object_list(cls, data):
        """"convert response data in list of class Employer objects"""

        employers_list = []
        for i in data:
            employer = cls(i.get('id'),
                           i.get('name'),
                           i.get('url'),
                           i.get('vacancies_url'),
                           i.get('open_vacancies'))
            employers_list.append(employer)

        return employers_list

    @staticmethod
    def get_vacancies(vacancies_url):
        response = requests.get(vacancies_url).json()
        print(response)
