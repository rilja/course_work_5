from src.employer import Employer
from src.parser import HH
from src.vacancy import Vacancy
from src.utils import create_database, save_data_to_database
from src.config import config

if __name__ == '__main__':
    hh_parser = HH()
    employers_list_from_hh = hh_parser.load_employers(10)
    employers_list = Employer.cast_to_object_list(employers_list_from_hh)
    vacancy_list_from_hh = employers_list[0].get_vacancies(employers_list[0].vacancies_url)
    vacancy_list = Vacancy.cast_to_object_list(vacancy_list_from_hh)
    params = config()
    create_database('CW5', params)
    # data = [vacancy_list, employers_list]
    # save_data_to_database(data, 'CW5', params)
