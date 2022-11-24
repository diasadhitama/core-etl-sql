"""
    author: diasadhitama3@gmail.com
"""

import pandas as pd, os #type: ignore
from sqlalchemy import create_engine #type: ignore
from . conn import ConnectionDatabase



class ReadData:


    def read(self):


        # inisiasi connection
        con_database        = ConnectionDatabase.conn(self)

        # read database       

        dataframe_sql       = pd.read_sql("""
                                                SELECT status."UserId", status."StatusId", titlestatus."Title"\
                                                FROM status inner join titlestatus \
                                                on status."StatusId" = titlestatus."StatusId"\
                                                where status."StatusId" = 1\
                                                and status."UserId" is not null\
                                                order by status."UserId"
        """, con_database)


        print(dataframe_sql)
        
                