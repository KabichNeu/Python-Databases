import psycopg2

def insert_sale(conn, order_num, order_type, cust_name, prod_number,
    prod_name, quantity, price, discount):

    order_total = quantity*price
    if discount != 0:
        order_total = order_total * discount
    
    sale_data = (order_num, order_type, cust_name, prod_number, prod_name,
        quantity, price, discount, order_total)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO sales(
        ORDER_NUM,
        ORDER_TYPE,
        CUST_NAME,
        PROD_NUMBER,
        PROD_NAME,
        QUANTITY,
        PRICE,
        DISCOUNT,
        ORDER_TOTAL) VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ''', sale_data)
    conn.commit()
    cur.execute("SELECT CUST_NAME, ORDER_TOTAL FROM sales WHERE ORDER_NUM=%s;", (order_total,) )
    rows = cur.fetchall()
    for row in rows:
        print("CUST_NAME=", row[0])
        print("ORDER_TOTAL", row[1], "\n")

if _name__ == "__main__":


    con =  psycopg2.connect(
                database="red30",
                user="postgres",
                password="password",
                host="localhost",
                port = "5432"
            )

    cursor = con.cursor()

    cursor.execute('''CREATE TABLE Sales
        (ORDER_NUM INT PRIMARY KEY,
        ORDER_TYPE TEXT,
        CUST_NAME TEXT,
        PROD_NUMBER TEXT,
        PROD_NAME TEXT,
        QUANTITY INT,
        PRICE REAL,
        DISCOUNT REAL,
        ORDER_TOTAL REAL);
    ''')

    con.commit()

    order_num = int(input("What is the order number\n"))
    order_type = input("What is the orfer type:\n")
    cust_name = input("What is the cust name:\n")
    prod_number = int(input("What is the product number:\n"))
    prod_name = input("What is the product name:\n")
    quantity = float(input("What is the quantity:\n"))
    price = float(input("What is the price:\n"))
    discount = float(input("What is the discount:\n"))

    insert_sale(con, order_num,order_type,cust_name,prod_number,prod_name,quantity,price,discount)
    cur = conn.cursor()
    # cursor.execute("SELECT * FROM sales LIMIT 10")
    # print(cursor.fetchall())
    cursor.execute('''
        INSERT INTO sales(
            ORDER_NUM,
            ORDER_TYPE,
            CUST_NAME,
            PROD_NUMBER,
            PROD_NAME,
            QUANTITY,
            PRICE,
            DISCOUNT,
            ORDER_TOTAL) VALUES
            (1105910, 'Retail', 'Syam Mapstone', 'EB521', 'Understanding Artificial Intelligence', 3, 19.5, 0,58.5)
    ''')
    con.commit()
    cursor.execute("SELECT CUST_NAME, ORDER_TOTAL FROM sales WHERE ORDER_NUM=1105910")
    rows = cur.fetchall()
    for row in rows:
        print("CUST_NAME = ", row[0])
        print("ORDER_TOTAL=",, row[1], "\n")
    con.close()



