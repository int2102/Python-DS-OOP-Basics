import getpass

import pandas as pd
import pymysql

my_password = getpass.getpass("Write your password here:")
try:
    connection = pymysql.connect(
        host="localhost", user="root", password=my_password, database="meteo_history"
    )
    inter1 = """
    #Rank the hot temperatures 
    SELECT
    RANK() OVER(ORDER BY temperature DESC) AS Global_Rank, country,temperature
    FROM global_extremes
    WHERE event_type="Heatwave"
    """
    inter2 = """
    #Write some details of the records
    SELECT country, CONCAT(temperature,' (',city,')-',YEAR(event_date)) AS record_details
    FROM global_extremes
    """
    inter3 = """
    #Difference in years compared to the present
    SELECT 
    city,
    temperature,
    YEAR(event_date) AS Record_Year,
    MONTH(event_date) AS Record_Month,
    ROUND(DATEDIFF(CURRENT_DATE(), event_date) / 365, 0) AS Years_Ago
    FROM global_extremes
    ORDER BY Years_Ago DESC;
    """
    inter4 = """
    #SHOW how many events has every category of natural disasters
    SELECT event_type,COUNT(record_id) AS number_events
    FROM global_extremes
    GROUP BY event_type
    ORDER BY number_events DESC
    """
    inter5 = """
    #Filter the temperature values, pick only the records from the 20 years, after that we export them to an excel file
    WITH dates AS(
    SELECT 
    country,
    city,
    temperature,
    YEAR(event_date) AS Record_Year,
    MONTH(event_date) AS Record_Month,
    ROUND(DATEDIFF(CURRENT_DATE(), event_date) / 365, 0) AS Years_Ago
    FROM global_extremes
    ORDER BY Years_Ago DESC
    )
    SELECT country,temperature
    FROM dates
    WHERE Years_Ago <=20;
    """
    df = pd.read_sql(inter5, connection)
    df.to_excel(r"G:\My Drive\Python\Proiecte SQL", index=False)
except Exception as e:
    print(f"Error:{e}")
