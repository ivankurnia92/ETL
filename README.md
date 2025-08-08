# Simple ETL Pipeline


Problem
Sebuah toko ingin menganalisis tren penjualan untuk customer yang memiliki pembelian lebih dari 30.
Tim Data Analyst meminta bantuan ke Data Engineer untuk membuat ETL Pipeline agar mempermudah proses.
Sehingga cukup mengambil data yang terbaru di database.


ETL Pipeline Design:

Extract :
Generate Data
Understanding Data
Check Data Types
Read csv data

Transform :
data filter data name is not null
data market_area is not null
data location indonesia
Filter data number_of_sales > 30

Load :
Save the output to data_sales_idn_min_30 table on Postgres
Tools: Python, Pandas, dan PostgreSQL
