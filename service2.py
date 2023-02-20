import time
from sql_queries import create_table, check_for_storage

create_table()

if __name__ == '__main__':
    while True:
        check_for_storage()
        print("checked")
        time.sleep(20)