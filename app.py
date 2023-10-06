from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'London',
    'salary': '£50k'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Manchester',
  },
  {
    'id': 3,
    'title': 'Team Leader',
    'location': 'London',
    'salary': '£100k'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='R9')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)