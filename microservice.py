import os
import time
import datetime
from flask import Flask, jsonify


app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /determineTime/42/determineTime/yyyy
#   "yyyy" is passed as the value of the input parameter.
#
@app.route('/determineTime/<remainderOfUrl>')
def determineTime(remainderOfUrl):
    #validate url
    try:
        intUrl = int(remainderOfUrl)
    except ValueError:
        return 'error'
    if (intUrl < -23 or intUrl > 23):
        return 'error'
    
    #calculate time in hhmm format
    date_time = str(datetime.datetime.utcnow());
    hh = date_time[11:13]
    hh = int(hh) + int(remainderOfUrl)
    if (hh > 23):
        hh = hh - 24
    if (hh < 0):
        hh = hh + 24
    mm = date_time[14:16]
    hhmm = str(hh) + mm
    if (len(hhmm) == 3):
        hhmm = '0' + hhmm
    return hhmm 

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

