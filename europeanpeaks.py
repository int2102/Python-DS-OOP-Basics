import getpass

import pandas as pd
import pymysql

my_password = getpass.getpass("Please, write your password here:")
try:
    connection = pymysql.connect(
        host="localhost", user="root", password=my_password, database="peaks"
    )
    inter1 = """
    # Print the first table with the join of the columns from the second table
    SELECT c.Rank_europe,c.Country,c.Peak_name,c.Elevation,p.Proeminence,p.Mountain_range
    FROM countries_details c
    LEFT JOIN peak_details p
    ON p.Peak_name=c.Peak_name
    """
    inter2 = """
    #mountain_range=["Caucasus","Armenian Mounts","Alps","Pyrenees","Rila","Korab","Sar Mountains","Carpathians","Scandinavian Mountains"]
    # Show what countries have the highest peak from an important mountain range of Europe (note: Tatras Mountains are the western part of Carpathians, i have considered all Alps mountain ranges as "Alps")
    SELECT c.Rank_europe,c.Country,c.Peak_name,c.Elevation,p.Proeminence,p.Mountain_range,
    CASE
        WHEN p.Mountain_range in ("Caucasus","Armenian Mounts","Alps","Pyrenees","Rila","Korab","Sar Mountains","Carpathians","Scandinavian Mountains") then "1"
        ELSE "0"
    END AS "Important_range"
    FROM countries_details c
    LEFT JOIN peak_details p
    ON p.Peak_name=c.Peak_name
    """
    inter3 = """
    # Group by mountain range to see the mountain range with the most highest peaks
    SELECT COUNT(c.Peak_name) AS number_peaks,p.Mountain_range,
    CASE
        WHEN p.Mountain_range in ("Caucasus","Armenian Mounts","Alps","Pyrenees","Rila","Korab","Sar Mountains","Carpathians","Scandinavian Mountains") then "1"
        ELSE "0"
    END AS "Important_range"
    FROM countries_details c
    LEFT JOIN peak_details p
    ON c.Peak_name=p.Peak_name
    GROUP BY Mountain_range
    HAVING Important_range=1
    ORDER BY number_peaks DESC
    """
    inter4 = """
    #Group by mountain range to see the most highest mounts of Europe
    SELECT MAX(c.Elevation) AS max_altitude,p.Mountain_range
    FROM countries_details c
    LEFT JOIN peak_details p
    ON c.Peak_name=p.Peak_name
    WHERE p.Mountain_range in ("Caucasus","Armenian Mounts","Alps","Pyrenees","Rila","Korab","Sar Mountains","Carpathians","Scandinavian Mountains")
    GROUP BY Mountain_range
    ORDER BY max_altitude DESC
    """
    inter5 = """
    #Show the mean value of peaks elevation and which countries have their highest peaks over this value
    SELECT Country,Elevation
    FROM countries_details 
    WHERE Elevation>(
    SELECT AVG(Elevation) FROM countries_details)
    ORDER BY Elevation DESC
    """
    df = pd.read_sql(inter3, connection)
    print(df)
    df.to_excel(r"G:\My Drive\Python\Proiecte SQL\europeanpeaksgroup.xlsx", index=False)
except Exception as e:
    print(f"Error:{e}")
