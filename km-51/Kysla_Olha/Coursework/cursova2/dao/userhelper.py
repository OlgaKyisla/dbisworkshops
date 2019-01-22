import cx_Oracle
from dao.credentials import *


def is_user(u_email, u_pass):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select is_user(:u_email,:u_pass) FROM dual'
    cursor.execute(query, [u_email, u_pass])
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_users_makeup(user_email):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select * from table(users_makeup.get_users_makeup( :user_email))'
    cursor.execute(query, [user_email])

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def get_makeup_by_id(id):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select * from table(makeup_tbl.get_users_makeup) where makeup_id = :id'
    cursor.execute(query, [id])

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_makeup():

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select * from table(makeup_tbl.get_users_makeup)'
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def get_makeup_id():

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select makeup_id from table(makeup_tbl.get_users_makeup)'
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_user_email(user_email):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    user_id = cursor.callfunc("USER_AUTH.get_user_email", cx_Oracle.NCHAR, [user_email])

    cursor.close()
    connection.close()

    return user_id

def get_user_role(user_email):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    user_role = cursor.callfunc("USER_AUTH.get_user_role", cx_Oracle.NCHAR, [user_email])

    cursor.close()
    connection.close()

    return user_role


def insert_to_user_feature(feature_name, user_email, user_attribute):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("USERS_MAKEUP.insert_to_user_feature", [feature_name, user_email, user_attribute])

    cursor.close()
    connection.close()

    return True


def new_user(u_email, u_status, u_name, u_pass):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    user_id = cursor.var(cx_Oracle.STRING)
    status = cursor.var(cx_Oracle.STRING)

    cursor.callproc("USER_AUTH.new_user", [u_email, status, u_name, u_pass])
    cursor.close()
    connection.close()

    return user_id.getvalue(), status.getvalue()


def get_users():
    connection = cx_Oracle.connect(username, password, databaseName)

    cursor = connection.cursor()

    query = 'SELECT * FROM "User"'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result
def get_feature():
    connection = cx_Oracle.connect(username, password, databaseName)

    cursor = connection.cursor()

    query = 'SELECT * FROM FEATURE'
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def count_email(u_email):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    counter = cursor.callfunc("USER_AUTH.count_email", cx_Oracle.NATIVE_INT, [u_email])
    cursor.close()
    connection.close()

    return counter


def new_makeup(MAKEUP_NAME, MAKEUP_PRICE, MAKEUP_QUANTITY, MAKEUP_DESCRIPTION):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    id = cursor.callfunc("ADMIN_ACTIONS.new_makeup", cx_Oracle.NUMBER, [MAKEUP_NAME, MAKEUP_PRICE, MAKEUP_QUANTITY, MAKEUP_DESCRIPTION])
    cursor.close()
    connection.close()

    return id


def edit_makeup(MAKEUP_ID ,MAKEUP_NAME, MAKEUP_PRICE, MAKEUP_QUANTITY, MAKEUP_DESCRIPTION):

    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("ADMIN_ACTIONS.edit_makeup", [MAKEUP_ID, MAKEUP_NAME, MAKEUP_PRICE, MAKEUP_QUANTITY, MAKEUP_DESCRIPTION])
    cursor.close()
    connection.close()

    return True

def delete_makeup(id):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("admin_actions.delete_makeup", [id])

    cursor.close()
    connection.close()

    return True

# Run this module Ctrl+Shift+F10

if __name__ == "__main__":

    #print(get_users())
        #if is_user('olgakyi@gmail.com', '555') == [(1,)]:
        #    print('111')
    #print(get_users_makeup('olha@gmaill.com'))
    #print(get_user_email('olha@gmaill.com'))
    #[a,b]=new_user('newuser18@gmail.com', None, 'newname', 'olas1_pass#')
    #print([a,b])
    #new_user('newuser19@gmail.com', None, 'newname', 'olas1_pass#')
    #res_list = [x[0] for x in get_feature()]
    #print(res_list)

    #for i,j in get_feature.items():
     #   print(i,j)
    #insert_to_user_feature('face type', 'newuser15@gmail.com', 'ovale');
    #insert_to_user_feature('color', 'newuser15@gmail.com', 'ovale');
    #a= get_user_role('olha@ukr.net')
    #print(a)
    #u_bool = is_user("dima@gmail.com","dima")
    #print(new_makeup('lipstick_6D', '100', '55', 'read cosmetic applied to the lips'))
    #delete_makeup('11')
    #a = get_makeup_by_id('8')
    #list = [x[1] for x in a]
    #print(list[0])
    print(get_makeup_id())
    #edit_makeup('10','55','22','33','55')