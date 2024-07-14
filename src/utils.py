import psycopg2


def create_database(new_database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {new_database_name}")
        cur.execute(f"""CREATE DATABASE {new_database_name}
                        WITH OWNER "postgres"
                        ENCODING 'UTF8'
                        LC_COLLATE = 'ru_RU.UTF-8'
                        LC_CTYPE = 'ru_RU.UTF-8'
                        TEMPLATE = template0;""")

    conn.close()

    # вот при этой строке выдает ошибку
    with psycopg2.connect(dbname=new_database_name, **params) as conn:
        pass




    #     conn.autocommit = True
    #     conn.set_client_encoding('UTF8')
    #     with conn.cursor() as cur:
    #         cur.execute("""
    #             CREATE TABLE employees (
    #                 employee_id SERIAL PRIMARY KEY,
    #                 employee_HH_id INTEGER NOT NULL,
    #                 name VARCHAR(50),
    #                 url TEXT,
    #                 vacancies_url TEXT,
    #                 open_vacancies INTEGER
    #             )
    #         """)
    #
    #     with conn.cursor() as cur:
    #         cur.execute("""
    #             CREATE TABLE vacancies (
    #                 vacancy_id SERIAL PRIMARY KEY,
    #                 employee_id INT REFERENCES employees(employee_id),
    #                 vacancy_HH_id INTEGER NOT NULL,
    #                 name VARCHAR(50),
    #                 alternate_url TEXT,
    #                 salary_from INTEGER,
    #                 description TEXT
    #             )
    #         """)
    #
    #     conn.commit()


# def save_data_to_database(data: list, db_name: str, params: dict) -> None:
#     """Saving data to db"""
#
#     conn = psycopg2.connect(dbname=db_name, **params)
#
#     with conn.cursor() as cur:
#         for vacancy in data[0]:
#             cur.execute(
#                 """
#                 INSERT INTO vacancies (vacancy_HH_id, name, alternate_url, salary_from, description)
#                 VALUES (%s, %s, %s, %s, %s)
#                 RETURNING channel_id
#                 """,
#                 (vacancy.id, vacancy.name, vacancy.alternate_url, vacancy.salary[0], vacancy.description)
#             )
#
#         for employers in data[1]:
#             cur.execute(
#                 """
#                 INSERT INTO employees (employee_HH_id, name, url, vacancies_url, open_vacancies)
#                 VALUES (%s, %s, %s, %s, %s)
#                 """,
#                 (employers.id, employers.name, employers.url, employers.vacancies_url, employers.open_vacancies)
#             )
#
#     conn.commit()
#     conn.close()
