import psycopg2
from psycopg2.extras import RealDictCursor


class BaseModel:
    __connection_string = "host=localhost port=5432 user=postgres password=123 dbname=school"

    @classmethod
    def all(cls):
        table_name = cls.__name__.lower()

        with psycopg2.connect(cls.__connection_string) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"""
                    SELECT *
                    FROM {table_name}
                """)
                return [cls(**dict(i)) for i in cur.fetchall()]

    @classmethod
    def exec(cls, student_id):
        table_name = cls.__name__.lower()

        with psycopg2.connect(cls.__connection_string) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(f"""
                    SELECT * 
                    FROM {table_name}
                    WHERE id={student_id}
                """)
                return [dict(i) for i in cur.fetchall()]
