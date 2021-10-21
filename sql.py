from utils import *


def logs_query(start_date, end_date):
    logs_query_sql = ("""SELECT uscl.id,CONCAT(au.first_name,'',au.last_name) as name,au.email , au.last_login ,r.id ,r.name ,uscl.action_type ,uscl.message ,uscl.created_at 
                        FROM user_status_change_log uscl INNER JOIN auth_user au ON (uscl.user_id = au.id) LEFT OUTER JOIN
                        rider r ON (au.id = r.user_id) WHERE uscl.created_at BETWEEN '{}' AND '{}' 
                        ORDER BY uscl.created_at DESC limit 10""".format(start_date, end_date))

    query = """select"""
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(logs_query_sql)

    shifts = cursor.fetchall()
    return shifts
