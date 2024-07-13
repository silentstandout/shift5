#install the 'pandas' library with 'pip install pandas'

import pandas as pd
import sqlite3

# Create connection to SQLite db
conn = sqlite3.connect('shift5.db')

# Load CSV files into pandas DataFrames with low_memory=False. Adjust paths.
df1 = pd.read_csv('/path/to/acas.csv', low_memory=False)
df2 = pd.read_csv('/path/to/hires_traces.csv', low_memory=False)
df3 = pd.read_csv('/path/to/readsb_hist.csv', low_memory=False)
df4 = pd.read_csv('/path/to/traces.csv', low_memory=False)
# Load others if needed

# Store the DataFrames as tables in the SQLite database
df1.to_sql('acas', conn, index=False, if_exists='replace')
df2.to_sql('hirestraces', conn, index=False, if_exists='replace')
df3.to_sql('readsb', conn, index=False, if_exists='replace')
df4.to_sql('traces', conn, index=False, if_exists='replace')
# Store more DataFrames if needed

# Close the db connection
conn.close()



