import redis
from flask import Flask, request
from rq import Queue


app = Flask(__name__)
r = redis.from_url("redis://127.0.0.1:6379")
q = Queue(connection=r)


# Get queue info
@app.route("/")
def jobs():
    queued_jobs = q.jobs
    scheduled_jobs = q.scheduled_job_registry.get_job_ids()
    started_jobs = q.started_job_registry.get_job_ids()
    deferred_jobs = q.deferred_job_registry.get_job_ids()
    canceled_jobs = q.canceled_job_registry.get_job_ids()
    finished_jobs = q.finished_job_registry.get_job_ids()
    failed_jobs = q.failed_job_registry.get_job_ids()

    html = '<center><br /><br />'
    html += f'{len(queued_jobs)} queued jobs:<br /><br />'
    for job in queued_jobs:
        html += f'<a href="job/{job.id}">{job.id}</a><br /><br />'
    html += f'{len(scheduled_jobs)} scheduled jobs:<br /><br />'
    for job in scheduled_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += f'{len(started_jobs)} started jobs:<br /><br />'
    for job in started_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += f'{len(deferred_jobs)} deferred jobs:<br /><br />'
    for job in deferred_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += f'{len(canceled_jobs)} canceled jobs:<br /><br />'
    for job in canceled_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += f'{len(finished_jobs)} finished jobs:<br /><br />'
    for job in finished_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += f'{len(failed_jobs)} failed jobs:<br /><br />'
    for job in failed_jobs:
        html += f'<a href="job/{job}">{job}</a><br /><br />'
    html += '</center>'
    return html


# Get a specific job info
@app.get('/job/<job_id>')
def get_job(job_id):
    res = q.fetch_job(job_id)
    if not res.result:
        return f'''<center><br /><br /><h3>The job is still pending</h3><br /><br />ID:{job_id}<br />
                Queued at: {res.enqueued_at}<br />Status: {res._status}</center>'''
    return f'''<center><br /><br /><h1>{res.result}</h1><br /><br />ID:{job_id}<br />
            Queued at: {res.enqueued_at}<br />Finished at: {res.ended_at}</center>'''


# Enqueue a job with args (if any)
@app.post('/job/<job_type>')
def post_job(job_type):
    args = request.args.to_dict()
    job = q.enqueue(f'jobs.{job_type}', args)
    return f'<center><br /><br /><a href="job/{job.id}">{job_type} with job id {job.id} enqueued</a><br /><br /></center>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

