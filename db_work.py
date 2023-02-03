import pymysql

from configs.db_config import *


def connect_to_db():
    try:
        connection = pymysql.connect(
            host=db_host,
            port=3306,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor)
        print('zaebis')
        print('#' * 20)
        return connection
    except Exception as ex:
        print('Connection pizdec')
        print(ex)


def new_user_db(chat_id, username):
    connection = connect_to_db()
    if not check_user_db(chat_id):
        try:
            with connection.cursor() as cursor:
                insert_query = 'INSERT INTO `bot_users` (chat_id, username, start_time) VALUES' \
                       f'( \'{chat_id}\', \'{username}\', NOW());'
                cursor.execute(insert_query)
                connection.commit()
        finally:
            connection.close()
            return True
    else:
        return False


def check_user_db(ch_id):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            check_query1 = f'SELECT username FROM `bot_users` WHERE chat_id = \'{ch_id}\';'
            cursor.execute(check_query1)
            data = cursor.fetchall()
    finally:
        # data = cursor.fetchall()
        connection.close()
        if data:
            print('NASHEL')
            return True
    print('NE_NASHEL')
    return False
