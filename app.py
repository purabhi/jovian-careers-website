from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'Title': 'Data Analyst',
    'Location': 'Benglaru, India',
    'Salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'Title': 'Data Scientist',
    'Location': 'Delhi, India',
    'Salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'Title': 'Frontend Engineer',
    'Location': 'Remote',
    'Salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'Title': 'Backend Engineer',
    'Location': 'San Francisco, USA',
    'Salary': 'Rs. 15,00,000'
  },
]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)


app.run(host='0.0.0.0', debug=True)
