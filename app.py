from crypt import methods
from doctest import master
from flask import Flask, render_template, request, url_for ,redirect
from datetime import datetime,timedelta
import time

app = Flask(__name__)

master_list = [{
    "id": 3,
    "text": "3",
    "date": "18/05/2022"
  },{
    "id": 2,
    "text": "2",
    "date": "12/06/2020"
  },
  {
    "id":1,
    "text": "1",
    "date": "15/06/2022"
  }]
# master_list = []

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        empty_dict = {}
        empty_dict["id"]  = len(master_list)+1 #Add id entry
        empty_dict["text"] = request.form['announcement_text'] #Add text entry
        empty_dict["date"] = datetime.now().strftime('%d/%m/%Y') #Add date entry 
        
        master_list.insert(0,empty_dict) #Insert new entry into first index position of the master list
        
        return redirect(url_for('index'))

    return render_template("index.html", data=master_list)

@app.route("/all",methods=['POST'])
def all():
    return render_template('index.html',data = master_list)
    
@app.route("/today",methods=['POST'])
def today():
    #Filter master list according to today's date
    todays_list = [x for x in master_list if x['date'] == datetime.now().strftime('%d/%m/%Y')]
    return render_template('index.html',data= todays_list)

@app.route("/last_seven_days",methods=['POST'])
def last_seven_days():
    
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()

    #Filter master list according to last seven days
    seven_list = [x for x in master_list if datetime.strptime(start_date.strftime('%d/%m/%Y'),'%d/%m/%Y') <= datetime.strptime(x['date'],'%d/%m/%Y') <= datetime.strptime(end_date.strftime('%d/%m/%Y'),'%d/%m/%Y') ]
    return render_template('index.html',data=seven_list)

@app.route("/last_thirty_days",methods=['POST'])
def last_thirty_days():
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    #Filter master list according to last thirty days
    thirty_list = [x for x in master_list if datetime.strptime(start_date.strftime('%d/%m/%Y'),'%d/%m/%Y') <= datetime.strptime(x['date'],'%d/%m/%Y') <= datetime.strptime(end_date.strftime('%d/%m/%Y'),'%d/%m/%Y') ]
    return render_template('index.html',data = thirty_list)


@app.route("/delete/<int:id>", methods=['POST'])
def delete(id):

    #Find post in master_list with the given id
    for index, post in enumerate(master_list):
        if post['id'] == id:
            del master_list[index] #Delete post from master list 

    return render_template('index.html',data=master_list)

if __name__ == '__main__':
    app.run(debug=True)