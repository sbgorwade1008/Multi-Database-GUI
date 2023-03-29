from flask import Flask, render_template_string
import pandas as pd
import oracle_db
import cx_Oracle

app = Flask(__name__)

# Define a route to display the HTML table
@app.route('/')
def display_table():
    # Render the HTML template with the table
    return render_template_string('<html><body>{{ table|safe }}</body></html>', table=oracle_db.query("sanmeet",1008,"localhost",1521,"XE"))

if __name__ == '__main__':
    app.run(debug=True)
