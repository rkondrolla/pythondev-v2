from flask import Flask, render_template, jsonify
from DB import engine
from sqlalchemy import text

app = Flask(__name__)

# List of job dictionaries


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result:
            jobs.append({
                'id': row.id,
                'title': row.title,
                'location': row.location,
                'salary': row.salary
            })
        return jobs

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='UNM SHUTTLE SERVICES')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

