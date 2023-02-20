import psycopg2

from liquid import Liquid

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    Create TABLE IF NOT EXISTS Liquid(
        id SERIAL PRIMARY KEY,
        flavour VARCHAR(255) NOT NULL,
        retail_price INTEGER NOT NULL,
        base_price INTEGER NOT NULL,
        quantity INTEGER NOT NULL, 
        volume_ml INTEGER NOT NULL,
        status INTEGER NOT NULL,
        buying_method VARCHAR(255) NOT NULL,
        created DATE DEFAULT NOW()
        )
    """
    print("table created")

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_liquid(liquid: Liquid):
    query = """
    INSERT INTO liquid (flavour, retail_price,base_price, quantity, volume_ml,status,buying_method)
    VALUES (%s, %s, %s, %s,%s,%s,%s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (liquid.flavour, liquid.retail_price, liquid.base_price, liquid.quantity, liquid.volume_ml,liquid.status,liquid.buying_method))
    conn.commit()

def check_for_storage():
    cursor = conn.cursor()
    print("list of available flavours: 1. strawberry 2.tobacco 3. iced guava 4. orange")
    z= input("Type in the liquid flavour to check availability:")
    cursor.execute("""
    SELECT
        SUM(CASE WHEN flavour = %s AND STATUS = 0 THEN quantity ELSE 0 END) AS total_ml_plus,
        SUM(CASE WHEN flavour = %s AND STATUS = 1 THEN quantity ELSE 0 END) AS total_ml_minus
    FROM liquid
    """,(z, z))
    row = cursor.fetchone()
    if row:
        print(row[0], row[1])
        leftovers = row[0] - row[1]
        if row[0] - row[1] > 2:
            print("Enough orange flavoured liquid. Right now it is ", leftovers, "available")
        else:
            print("Buy orange flavoured liquid asap!")
    else:
        print("No results found.")
    cursor.execute(z)
    conn.commit()

def profit():
    cursor = conn.cursor()
    print("list of available flavours: 1. strawberry 2.tobacco 3. iced guava 4. orange")
    x = input("Amount of profit earned, type in the flavour:")
    cursor.execute("""
    SELECT
        SUM(CASE WHEN flavour = %s THEN retail_price ELSE 0 END) AS total_profit,
        SUM(CASE WHEN flavour = %s THEN base_price else 0 end) as total_spendings
    FROM liquid
    """,(x,x))
    row = cursor.fetchone()
    print("Total estimated profit from sales of the",x,"liquid is:",row[0]-row[1])
    cursor.execute(x)
    conn.commit()

def statistics():
    cursor = conn.cursor()
    print("list of available flavours: 1. strawberry 2.tobacco 3. iced guava 4. orange")
    c = input("Type in for which buying method you want to get statistics:")
    cursor.execute("""
    Select
        SUM(CASE WHEN buying_method =%s and status = 0 or status=1 then quantity else 0 end) as total_amount_bought,
        SUM(CASE WHEN buying_method =%s and status = 0 then quantity else 0 end) as total_amount_present,
        SUM(CASE WHEN buying_method = %s and status = 0 then volume_ml else 0 end) as total_amount_present_ml, 
        MAX(case when flavour = %s and status = 1 then created else 0 end) as last_purchase_date,
        AVG(CASE when flavour = %s and status =1 then retail_price else 0 end) as average_selling_value
    from liquid
    """,(c,c,c,c,c))
    row = cursor.fetchone()
    print("Statistic for the",c,"flavoured liquid \n Total amount bought:",row[0],"\n Total amount present:",row[1],"\n Total amount present in ml:",row[2], "\n Last purchase data:",row[3],"\n Average selling price",row[4])
    cursor.execute(c)
    conn.commit()