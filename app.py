from flask import Flask,render_template
import pandas as pd
from ydata_profiling import ProfileReport
import logging,sys

app = Flask('__name__',template_folder='template')
@app.route('/')
def home():
   
    data = pd.read_csv("IRIS.csv")
    profile = ProfileReport(data)
    profile.to_file("Profiling_Report_Results.html")
    return render_template("Profiling_Report_Results.html")

if(__name__=='__main__'):
    log = logging.getLogger('werkzeug')
    log.disabled = True
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None
    app.run(debug=True,host="0.0.0.0",port=5000)
