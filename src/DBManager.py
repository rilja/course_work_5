import psycopg2


class DBManager:
    def __init__(self, db_name, params):
        self.db_name = db_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        with psycopg2.connect(dbname=self.db_name, **self.params) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(""""SELECT name, open_vacancies FROM employees""")
            conn.commit()

    def get_all_vacancies(self):
        with psycopg2.connect(dbname=self.db_name, **self.params) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(""""SELECT name, open_vacancies FROM employees""")
            conn.commit()

    def get_avg_salary(self):
        with psycopg2.connect(dbname=self.db_name, **self.params) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(""""SELECT name, open_vacancies FROM employees""")
            conn.commit()

    def get_vacancies_with_higher_salary(self):
        with psycopg2.connect(dbname=self.db_name, **self.params) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(""""SELECT name, open_vacancies FROM employees""")
            conn.commit()

    def get_vacancies_with_keyword(self):
        with psycopg2.connect(dbname=self.db_name, **self.params) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                cur.execute(""""SELECT name, open_vacancies FROM employees""")
            conn.commit()
