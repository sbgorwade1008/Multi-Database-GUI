from flask import Flask, render_template_string
import pandas as pd

import cx_Oracle
from zmq import HELLO_MSG

def query(user,password,host,port,dsn):
    # Establish a connection to the database
    connection = cx_Oracle.connect(f"{user}/{password}@{host}:{port}/{dsn}")

    # Define the SQL query
    query = 'SELECT * FROM tab'

    # Execute the query and return the results as a DataFrame
    df = pd.read_sql(query, connection)

    # Close the database connection
    connection.close()

    # Print the DataFram

    html_table = df.to_html()

    # Render the HTML template with the table
    return html_table
