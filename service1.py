import time
import random
from sql_queries import create_table, insert_liquid
from liquid import Liquid

create_table()

if __name__ == '__main__':
    while True:
        insert_liquid(
            Liquid(
                flavour=random.choice(["strawberry", "tobacco", "iced guava","orange"]),
                retail_price=random.choice([3900, 4500, 6000, 10000]),
                base_price=random.choice([400,600,500,1000]),
                quantity= 1,
                volume_ml=random.choice([5,10,30]),
                status=random.choice([0, 1]),
                buying_method=random.choice(["online","offline"]),
            )
        )
        print("Inserted")
        time.sleep(1)