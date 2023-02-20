import psycopg2
from sql_queries import create_table
import time
conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)

if __name__ == '__main__':
    while True:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM liquid")
        liquid = cursor.fetchall()
        print(liquid)
        time.sleep(10)


