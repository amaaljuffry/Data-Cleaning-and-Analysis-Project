import pandas as pd 
df = pd.read_csv('netflix_titles.csv')

#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine(r'mssql://AMA\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn = engine.connect()

df.to_sql('netflix_raw', con=conn , index=False, if_exists = 'append')
conn.close()

df.head()
df[df.show_id=='s5023']
max(df.description.dropna().str.len())
df.isna().sum()


drop TABLE [dbo].[netflix_raw](
[show_id] [varchar] (10) NULL,
[type] [varchar ] (10) NULL,
[title] [nvarchar] (200) NULL,
[director] [varchar] (250) NULL,
[cast] [varchar] (1000) NULL,
[country] [varchar] (150) NULL,
[date_added] [varchar] (20) NULL,
[release_year] [bigint] NULL,
[rating] [varchar] (10) NULL
[duration] [varchar] (10) NULL,
[listed_in] [varchar](100) NULL,
[description] [varchar] (500) NULL

)
GO