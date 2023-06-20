from flask import Flask, render_template, request, redirect,url_for
import pickle
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SairamSQL@2022'
app.config['MYSQL_DB'] = 'internshipwebsitedb'

mysql = MySQL(app)


@app.route('/',methods =['Get','POST'])
def landing():
    return render_template("LandingPage.html")


@app.route('/PredictionPage.html',methods =['Get','POST'])
def Predict():
    if request.method == "POST":
        internetval = request.form.get('intval')
        anxietyval = request.form.get('anxval')
        depressionval = request.form.get('depval')

        if internetval == "Normal":
            internetval = 0
        elif internetval == "Mild":
            internetval = 1
        elif internetval == "Moderate":
            internetval = 2
        elif internetval == "Severe":
            internetval = 3

        if depressionval == "Normal":
            depressionval = 0
        elif depressionval == "Mild":
            depressionval = 1
        elif depressionval == "Moderate":
            depressionval = 2
        elif depressionval == "Severe":
            depressionval = 3 

        if anxietyval == "Normal":
            anxietyval = 0
        elif anxietyval == "Mild":
            anxietyval = 1
        elif anxietyval == "Moderate":
            anxietyval = 2
        elif anxietyval == "Severe":
            anxietyval = 3 


        if 'AnxbuttonClicked' in request.form and request.form['AnxbuttonClicked'] == 'true':
            with open('AnxietyModel','rb') as f:
                ANX_model = pickle.load(f)
                anx_res = ANX_model.predict([[internetval,depressionval]])
                anx_result = anx_res.round()

            if anx_result == 0:
                anx_result = "Normal"
            elif anx_result == 1:
                anx_result = "Mild"
            elif anx_result == 2:
                anx_result = "Moderate"
            elif anx_result == 3:
                anx_result = "Severe" 

            return render_template("PredictionPage.html",disease = "Anxiety",predict = anx_result)

            

        else:
            with open('DepressionModel','rb') as f:
                DEP_model = pickle.load(f)
                dep_res = DEP_model.predict([[internetval,anxietyval]])
                dep_result = dep_res.round()

            if dep_result == 0:
                dep_result = "Normal"
            elif dep_result == 1:
                dep_result = "Mild"
            elif dep_result == 2:
                dep_result = "Moderate"
            elif dep_result == 3:
                dep_result = "Severe" 

            return render_template("PredictionPage.html",disease = "Depression",predict = dep_result)

    return render_template("PredictionPage.html")


@app.route('/AccurateFormPage.html',methods =['Get','POST'])
def Form():
    if request.method == "POST":
        i1 = int(request.form.get('i1'))
        i2 = int(request.form.get('i2'))
        i3 = int(request.form.get('i3'))
        i4 = int(request.form.get('i4'))
        i5 = int(request.form.get('i5'))
        i6 = int(request.form.get('i6'))
        i7 = int(request.form.get('i7'))
        i8 = int(request.form.get('i8'))
        i9 = int(request.form.get('i9'))
        i10 = int(request.form.get('i10'))
        i11 = int(request.form.get('i11'))
        i12 = int(request.form.get('i12'))
        i13 = int(request.form.get('i13'))
        i14 = int(request.form.get('i14'))
        i15 = int(request.form.get('i15'))
        i16 = int(request.form.get('i16'))
        i17 = int(request.form.get('i17'))
        i18 = int(request.form.get('i18'))
        i19 = int(request.form.get('i19'))
        i20 = int(request.form.get('i20'))

        d1 = int(request.form.get('d1'))
        d2 = int(request.form.get('d2'))
        d3 = int(request.form.get('d3'))
        d4 = int(request.form.get('d4'))
        d5 = int(request.form.get('d5'))
        d6 = int(request.form.get('d6'))
        d7 = int(request.form.get('d7'))
        d8 = int(request.form.get('d8'))


        a1 = int(request.form.get('a1'))
        a2 = int(request.form.get('a2'))
        a3 = int(request.form.get('a3'))
        a4 = int(request.form.get('a4'))
        a5 = int(request.form.get('a5'))
        a6 = int(request.form.get('a6'))
        a7 = int(request.form.get('a7'))

        name = request.form.get('name')
        email = request.form.get('email')
        gender = request.form.get('gender')

        InternetTotalScore = i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15+i16+i17+i18+i19+i20
        DepressionTotalScore = d1+d2+d3+d4+d5+d6+d7+d8
        AnxietyTotalScore = a1+a2+a3+a4+a5+a6+a7

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(''' INSERT INTO user_details VALUES(%s,%s,%s,%s,%s,%s)''',(name,gender,email,InternetTotalScore,DepressionTotalScore,AnxietyTotalScore))
        mysql.connection.commit()
        cursor.close()



        return redirect(url_for('FormResult', InternetTotalScore=InternetTotalScore,DepressionTotalScore=DepressionTotalScore,AnxietyTotalScore=AnxietyTotalScore,name=name))
    return render_template("AccurateFormPage.html")


@app.route('/FormResult.html',methods =['Get','POST'])
def FormResult():
    InternetTotalScore = request.args.get('InternetTotalScore')
    DepressionTotalScore = request.args.get('DepressionTotalScore')
    AnxietyTotalScore = request.args.get('AnxietyTotalScore')
    name = request.args.get('name')
    return render_template("FormResult.html", InternetTotalScore=InternetTotalScore,DepressionTotalScore=DepressionTotalScore,AnxietyTotalScore=AnxietyTotalScore,name=name)



if __name__ == '__main__':
    app.run(port = 3000, debug = True)
