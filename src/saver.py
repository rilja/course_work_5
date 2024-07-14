from abc import ABC, abstractmethod
import psycopg2


class Saver(ABC):
    """Abstract class for saving data"""
    @abstractmethod
    def __init__(self):
        self.is_added = False
        pass

    @abstractmethod
    def add_cell(self, identification):
        pass

    @abstractmethod
    def delete_cell(self, identification):
        pass