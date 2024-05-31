from flask import Flask, render_template, jsonify 

app = Flask(__name__)

# List of job dictionaries
JOBS = [
  {
    'id': 1,
    'title': 'Manager',
    'location': 'Albuquerque, NM',
    'salary': '$64,000'
  },
  {
    'id': 2,
    'title': 'Admin Assistant',
    'location': 'Remote',
    'salary': '$60,000'
  },
  {
    'id': 3,
    'title': 'Supervisor',
    'location': 'Albuquerque, NM',
    'salary': '$55,000'
  },
  {
    'id': 4,
    'title': 'AM-Driver',
    'location': 'Albuquerque, NM',
    'salary': '$35,000'
  },
  {
    'id': 5,
    'title': 'PM-Driver',
    'location': 'Albuquerque, NM',
    'salary': '$35,000'
  }
]


@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS, company_name='UNM SHUTTLE SERVICES')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

# Ensure the script runs only if executed directly
if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 8080,  debug=True)
