import time
from sql_queries import create_table, statistics

create_table()

if __name__ == '__main__':
    while True:
        statistics()
        print("calculated")
