from django.db import connection
import psycopg2

# Ini adalah fungsi untuk membuka koneksi ke database
def babadu_d7_db():
    connection = psycopg2.connect(
        host="localhost",
        port="5433",
        database="babadu",
        user="postgres",
        password="Mario13052002",
    ).cursor()

    connection.autocommit = True

    connection = connection.cursor()
    connection.execute("SET search_path to BADADU_D7;")

    return connection