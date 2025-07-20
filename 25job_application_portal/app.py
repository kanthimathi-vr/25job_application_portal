from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Machine Learning Engineer',
        'company': 'OpenAI',
        'logo': 'logos/openai.png',
        'department': 'AI Research',
        'description': 'Work on cutting-edge AI models and systems.'
    },
    {
        'id': 2,
        'title': 'Frontend Developer',
        'company': 'Google',
        'logo': 'logos/google.png',
        'department': 'Web',
        'description': 'Develop responsive and beautiful web apps.'
    },
    {
        'id': 3,
        'title': 'Cloud Solutions Architect',
        'company': 'Amazon',
        'logo': 'logos/amazon.png',
        'department': 'Cloud',
        'description': 'Design scalable cloud architectures on AWS.'
    }
]

@app.route('/')
def home():
    dept = request.args.get('dept')
    departments = sorted(set(job['department'] for job in jobs))
    filtered_jobs = [job for job in jobs if job['department'] == dept] if dept else jobs
    return render_template('home.html', jobs=filtered_jobs, departments=departments, selected_dept=dept)

@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
def job_detail(job_id):
    job = next((j for j in jobs if j['id'] == job_id), None)
    if not job:
        return "Job not found", 404

    if request.method == 'POST':
        # You could save application info here
        return redirect(url_for('success'))

    return render_template('job_detail.html', job=job)

@app.route('/success')
def success():
    return render_template('success.html')


if __name__=='__main__':
    app.run(debug=True)