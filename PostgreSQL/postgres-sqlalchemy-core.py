from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgres://postgres:password@localhost/red30')

with engine.connect() as connection:
    meta  = MetaData(engine)
    sales_table = Table('sales', meta, autoload = True, autoload_with = engine)

    insert_statement = sales_table.insert().values(
        order_num = 'Retail',
        cust_name = 'Syman Mapstone',
        prod_number ='EB521',
        prod_name = 'Understanding Atificial intelligence',
        quantity = 3,
        price = 19.5,
        discount = 0,
        order_total = 58.5
    )

    connection.execute(insert_statement)

    #read
    select_statement = sales_table.select().limit(10)
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)
    
    #update 
    update_statement = sales_table.select().where(sales_table.c.order_num == 110596).values(quantity=2, order_total = 39)
    updated_set = connection.execute(update_statement)
    #confirm update: Read
    reselect_statement = sales_table.select().where(sales_table.c.order_num == 110596).values(quantity=2, order_total = 39)
    updated_set = connection.execute(reselect_statement)
    for u in updated_set:
        print(u)

    #delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num == 110596)
    connection.execute(delete_statement)

    #confirm delete: Read
    not_found_set = connection.execute(reselect_statement)
    print(not_found_set.rowcount)




    