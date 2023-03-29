from flask import Flask, render_template, request
from Write_dtl import Writer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Main.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    selected_db = request.form['database']
    a=Writer.readFile(1)
    if selected_db=="Oracle":
        return render_template('Oracle.html',server=a[0], port=int(a[1]), username=a[2], password=a[4], database=a[3])
    elif selected_db=="Oracle":

        return render_template("Query.html",)
    

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        # get the form data
        server = request.form['server']
        port = request.form['port']
        username = request.form['username']
        password = request.form['password']
        database = request.form['database']
        b=Writer(port=port,server=server,database=database,password=password,username=username)
        b.writeToFile()
        a=b.readFile()
        # pass the form data to the template
        return render_template('Oracle.html',server=a[0], port=int(a[1]), username=a[2], password=a[4], database=a[3])
    else:
        return render_template('Oracle.html')
'''   
@app.route('/submit', methods=['POST'])
def submit():
    input_value = request.form['query_in']
    # do something with the input value, e.g. query a database
    table = [['row1col1', 'row1col2'], ['row2col1', 'row2col2']]
    return render_template('Query.html', table=table)

'''
if __name__ == '__main__':
    app.run(debug=True)
