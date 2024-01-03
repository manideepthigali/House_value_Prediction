from flask import Flask,render_template,request
from args import *
import pickle
import numpy as np



with open('Model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
    
    
    
app=Flask(__name__)
@app.route('/',methods=['Get','POST'])
def index():
    #print(request.method)
    #print(request.form)
    if request.method== 'POST':
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        Location = request.form['Location']
        Sqft = request.form['Sqft']
        Status = request.form['Status']
        Direction = request.form['Direction']
        Property_type = request.form['Property_type']
        
        inp_arr=np.array([[bedrooms,bathrooms,Location,Sqft,Status,Direction,Property_type]])
        
        input_df = scaler.transform(inp_arr)

        prediction =  model.predict(input_df)[0]
        
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               property_type_mapping=property_type_mapping,
                               direction_mapping=direction_mapping,prediction=prediction)
        
        
        
        
    else:
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               property_type_mapping=property_type_mapping,
                               direction_mapping=direction_mapping)
@app.route('/second')
def second():
    return 'I am in Second Page'
@app.route('/third')
def third():
    return 'I am in Third Page' 
#app.run(use_reloader=True,debug=True)


if __name__ == '__main__' :
    app.run()
    