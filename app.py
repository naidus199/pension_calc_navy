import pickle
#lr = pickle.load(open("lr_c35.pkl","rb"))

import numpy as np
from flask import Flask,request,render_template
app =Flask(__name__)


@app.route("/")
def homepage():
	return render_template("index.html")
	

# @app.route("/predict",methods=['POST'])
# def predict():
#     pre_sal = lr.predict([[int(x) for x in request.form.values()]])
#     return render_template("index.html",prediction_text = "your Salary is "+str(pre_sal[0]))
    
#@app.route("/app.py", methods = ["GET",  "POST"])
@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        basic = int(request.form.get('basic'))
        msp = int(request.form.get('msp'))
        da = int(request.form.get('da'))
        tot_service = int(request.form.get('tot_service'))
        leave_days = int(request.form.get('leave_days'))
        pf = int(request.form.get('pf'))
        commutaion = int(request.form.get('commutaion') )
        ngis = int(request.form.get('ngis'))
        age_at_retirement = int(request.form.get('age_at_retirement'))
        graduity_months = 10

        graduity = ((((basic + msp)* da)/100) + basic + msp) * graduity_months
        leave_amount = (((basic*da)/100)+basic) * (leave_days/30)
        full_pension = (basic+msp)/2
        da_on_pension = (full_pension*da)/100
        age_factors = {30:9.173, 31:9.169, 32:9.164, 33:9.159, 34:9.152, 35:9.145, 36:9.136, 
        37:9.126, 38:9.116, 39:9.103, 40:9.09, 41:9.075, 42:9.059, 43:9.04, 44:9.019,
        45:8.996, 46:8.971, 47:8.943, 48:8.913, 49:8.881, 50:8.846, 51:8.808, 52:8.768,
        53:8.724, 54:8.678, 55:8.627, 56:8.572, 57:8.512}
        age_factor = age_factors[age_at_retirement]
        commutaion_amount = ((full_pension*commutaion)/100)*12*age_factor
        commutation_emi = (full_pension*commutaion)/100
        tot_comm_repay = commutation_emi*12*15
        commuted_pesnion = full_pension+da_on_pension-tot_comm_repay
        total_in_hand = graduity+leave_amount+pf+commutaion_amount+ngis
    return render_template("index.html",prediction_text = "The amount in your hand is "+str(total_in_hand))
    
    
    
if __name__ == "__main__":
    app.run(port=5000,debug=True)