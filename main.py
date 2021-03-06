from flask import Flask, render_template,request,redirect
from scarrper import get_jobs
app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report") 
def report():
  word = request.args.get('word') ## word args 만
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs: 
      jobs = existingJobs
    else:
      jobs= get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html" ,
   searchingBy = word,
   resultsNumber=len(jobs),
   jobs =jobs 
   )

app.run(host="0.0.0.0") # 리펠환경에 있으니  서버 구축?


