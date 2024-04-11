from flask import Flask,render_template
app=Flask(__name__)
jobs=[
  {
    "id":1,
    "title":"Data Analyst",
    "location":"Bengaluru,India",
    "Salary":"Rs. 10,00,000"
  },
  {
    "id":2,
      "title":"Job Analyst",
      "location":"Remote",
      "Salary":"Rs. 15,00,000"
    },
{
  "id":3,
    "title":"Data Engineer",
    "location":"Udupi,India",
    "Salary":"Rs. 10,00,000"
  }

]
@app.route("/")
def hello():
 return render_template("home.html",jobs=jobs,company_name="JOVIAN")
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
  
