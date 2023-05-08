from django.db import connection

def query_result(query):
  with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    return result