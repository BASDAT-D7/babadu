from django.db import connection

def query_add(query):
  with connection.cursor() as cursor:
    cursor.execute(query)

def query_result(query):
  with connection.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def parse(result):
    data = result[0][0]
    return data

