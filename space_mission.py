import getpass

import pandas as pd
import pymysql

my_password = getpass.getpass("Write your password here:")
try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password=my_password,
        database="space_exploration",
    )
    inter1 = """
    #Group companies by the cost of expeditions
    WITH group_cost AS(
    SELECT 
    company, 
    rocket_name,
    COALESCE(cost_millions, 0) AS Cost_Info
    FROM space_missions)
    SELECT company, sum(Cost_Info) AS sum_cost
    FROM group_cost
    GROUP BY company
    HAVING sum_cost >0
    ORDER BY sum_cost ASC
    """
    inter2 = """
    #Date difference between present and launch date
    SELECT mission_id,rocket_name,CONCAT(YEAR(CURRENT_DATE())-YEAR(launch_date)," Years Ago") AS Marginoftime
    FROM space_missions
    """
    inter3 = """
    #Show how many missions were a success
    SELECT COUNT(rocket_name)
    FROM space_missions
    WHERE mission_status="Success"
    """
    inter4 = """
    WITH analyse_cost AS(
    SELECT company, rocket_name, mission_status,
    CASE
       WHEN cost_millions>2000 THEN 'Expensive'
       WHEN cost_millions BETWEEN 300 AND 2000 THEN 'Medium costs'
       ELSE 'Low costs'
    END AS 'Category_costs'
    FROM space_missions
    WHERE cost_millions IS NOT NULL
    )
    SELECT Category_costs, COUNT(rocket_name) AS number_missions
    FROM analyse_cost
    GROUP BY Category_costs
    ORDER BY number_missions DESC
    """
    inter5 = """
    #Show whose agencies have an average cost per launch that is higher than the global average
    WITH GlobalAverage AS (
    SELECT AVG(cost_millions) AS avg_global_cost
    FROM space_missions
    ),
    CompanyAverage AS (
    SELECT company, AVG(cost_millions) AS avg_company_cost
    FROM space_missions
    GROUP BY company
    )
    SELECT c.company, c.avg_company_cost, g.avg_global_cost
    FROM CompanyAverage c
    CROSS JOIN GlobalAverage g
    WHERE c.avg_company_cost > g.avg_global_cost;
    """
    df = pd.read_sql(inter1, connection)
    print(df)
except Exception as e:
    print(f"Error:{e}")
