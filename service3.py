import time
from sql_queries import create_table, profit

create_table()

if __name__ == '__main__':
    while True:
        profit()
        print("calculated")
        time.sleep(20)