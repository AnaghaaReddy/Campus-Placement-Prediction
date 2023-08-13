import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('placed.pkl', 'rb'))
scaler=pickle.load(open('preprocess.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    a = request.form["gender"]
    b = request.form["ssc"]
    c = request.form["hse"]
    d = request.form["hsep"] 
    e = request.form["dp"]
    f = request.form["df"]
    g = request.form["we"]
    h = request.form["etp"]
    i = request.form["mbasp"]
    j = request.form["mbap"]

    if a == "f":
        a = 0
    else:
        a = 1

    if d == "comm":
        d = 1
    elif d == "scie":
        d = 2
    else:
        d = 0

    if f == "commMang":
        f = 0
    elif f == "sciTech":
        f = 2
    else:
        f = 1

    if i == "mktHr":
        i = 1
    else:
        i = 0

    t = [[int(a), float(b), float(c), int(d), float(e), int(f), float(g), float(h), int(i), float(j)]]

    #x=[[ 1,67,91.00,1,58.00,2,0,55.0,1,58.80]]

    output = model.predict(t)
    print(output)
    #print("AAAA")
    if output[0] == 1:
        output = "Placed"
        models_1=pickle.load(open('model.pkl', 'rb'))
        x = [[int(a), int(d), int(f), float(h), float(j)]]
        scaled_t = scaler.transform(x)
        output2 = models_1.predict(scaled_t)

        return render_template('index.html', y="The verdict is: " + output+" and salary is "+str(np.round(output2[0])))
    else:
        output = "Not Placed"
        output2="Need to work Hard!!"

        return render_template('index.html', y="The verdict is: " + output+" and "+output2)

if __name__ == '__main__':
    app.run(debug=True)


    
        