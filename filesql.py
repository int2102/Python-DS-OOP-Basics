import pandas as pd
import pymysql

# Acestea sunt datele tale locale
HOST = "localhost"
USER = "root"
PASSWORD = ""  # Înlocuiește cu parola setată la instalare

try:
    # Ne conectăm la motorul MySQL de pe laptopul tău
    conexiune = pymysql.connect(host=HOST, user=USER, password=PASSWORD)

    print("Succes! Python a comunicat cu MySQL-ul tău local!")

    # Hai să vedem ce baze de date ai deja pe server (sunt câteva default)
    df = pd.read_sql("SHOW DATABASES;", conexiune)
    print("\nBazele de date existente pe serverul tău:")
    print(df)

except Exception as e:
    print(f"Eroare: {e}")
