import sqlite3

def init_authorization():
    conn=sqlite3.connect("./cloud_computing_project/data/user_info.db")
    cursor = conn.cursor()
    cursor.execute('create table if not exists user (id int primary key,'
                   'first_name varchar(20) not null,'
                   'last_name varchar(20) not null,'
                   'password varchar(20) not null)')
    # cursor.execute('insert into user (id,first_name,last_name,password) values (1,"Michael","hello","asdasd")')
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

init_authorization()
