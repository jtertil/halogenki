import psycopg2


class Database:
    """Postgres database connections class."""
    def __init__(self, db_conf):
        self.db_conf = db_conf

    def select_one(self, query):
        """Executes SELECT query and return first row."""
        with psycopg2.connect(**self.db_conf) as conn:
            conn.set_session(readonly=True)
            with conn.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
            cursor.close()
        conn.close()
        return row

    def select_all(self, query):
        """Executes SELECT query and return list of rows."""
        with psycopg2.connect(**self.db_conf) as conn:
            conn.set_session(readonly=True)
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
            cursor.close()
        conn.close()
        return rows

    def execute(self, query):
        """Executes a query and return count of affected rows."""
        with psycopg2.connect(**self.db_conf) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            cursor.close()
        conn.close()
        return cursor.rowcount
