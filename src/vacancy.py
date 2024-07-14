from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Abstract class for creating vacancies from API"""
    @abstractmethod
    def __init__(self, identification, name, url, salary, description):
        self.id = identification
        self.name = name
        self.url = url
        self.salary = salary if salary else 0
        self.description = description

    @classmethod
    def cast_to_object_list(cls, data):
        pass


class Vacancy(BaseVacancy):
    def __init__(self, identification, name, url, salary, description):
        super().__init__(identification, name, url, salary, description)

    @classmethod
    def cast_to_object_list(cls, data):
        """"convert json data in list of class Vacancy objects"""

        vacancies = []
        for i in data:
            vacancy = cls(i.get('id'),
                          i.get('name'),
                          i.get('alternate_url'),
                          i.get('salary'),
                          i.get('description'))
            vacancies.append(vacancy)

        return vacancies
