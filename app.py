from crypt import methods
from doctest import master
from flask import Flask, render_template, request, url_for ,redirect
from datetime import datetime,timedelta
import time

app = Flask(__name__)

master_list = [{
    "id": 3,
    "text": "3",
    "date": "21/05/2022"
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
        if request.form['submit'] == 'Create':
            empty_dict = {}
            empty_dict["id"]  = len(master_list)+1 #Add id entry
            empty_dict["text"] = request.form['announcement_text'] #Add text entry
            empty_dict["date"] = datetime.now().strftime('%d/%m/%Y') #Add date entry 
            
            master_list.insert(0,empty_dict) #Insert new entry into first index position of the master list
            return redirect(url_for('index'))

        elif request.form['submit'] == 'all-button':
            return render_template('index.html',data = master_list,text="all")
        
        elif request.form['submit'] == 'today-button':
            todays_list = [x for x in master_list if x['date'] == datetime.now().strftime('%d/%m/%Y')]
            return render_template('index.html',data= todays_list ,text="todays")

        elif request.form['submit'] == 'seve-day-button':
            start_date = datetime.now() - timedelta(days=7) #Get start date
            end_date = datetime.now() #Get ending date
            #Filter master list according to last seven days
            seven_list = [x for x in master_list if datetime.strptime(start_date.strftime('%d/%m/%Y'),'%d/%m/%Y') <= datetime.strptime(x['date'],'%d/%m/%Y') <= datetime.strptime(end_date.strftime('%d/%m/%Y'),'%d/%m/%Y') ]
            return render_template('index.html',data=seven_list,text="last seven days")

        elif request.form['submit'] == 'thirty-day-button':
            start_date = datetime.now() - timedelta(days=30) #Get start date
            end_date = datetime.now() #Get ending date
            #Filter master list according to last thirty days
            thirty_list = [x for x in master_list if datetime.strptime(start_date.strftime('%d/%m/%Y'),'%d/%m/%Y') <= datetime.strptime(x['date'],'%d/%m/%Y') <= datetime.strptime(end_date.strftime('%d/%m/%Y'),'%d/%m/%Y') ]
            return render_template('index.html',data = thirty_list,text="last thirty days")
    
    return render_template("index.html", data=master_list, text="all")

@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    #Find post in master_list with the given id
    for index, post in enumerate(master_list):
        if post['id'] == id:
            del master_list[index] #Delete post from master list 
    return render_template('index.html',data=master_list)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="localhost", port=5000, debug=True)