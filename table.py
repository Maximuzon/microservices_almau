import time
import random
from sql_queries import create_table, insert_liquid
from liquid import Liquid

if __name__ == '__main__':
    while True:
        create_table()
        print("created")