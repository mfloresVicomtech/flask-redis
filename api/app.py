import random
from time import sleep
from flask import Flask
import redis
from rq import Queue
from utils.helpers import do_long_task

app = Flask(__name__)
r = redis.from_url("redis://redis:6379")
q = Queue(connection=r)


@app.route("/")
def hello():
    task = q.enqueue(do_long_task, 5)
    n = len(q.jobs)

    html = '<center><br /><br />'
    for job in q.jobs:
        html += f'<a href="job/{job.id}">{job.id}</a><br /><br />'
    html += f'Total {n} Jobs in queue </center>'
    return f"{html}"

@app.get('/job/<job_id>')
def get_job(job_id):

    res = q.fetch_job(job_id)

    if not res.result:
        return f'<center><br /><br /><h3>The job is still pending</h3><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Status: {res._status}</center>'

    return f'<center><br /><br /><h1>{res.result}</h1><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Finished at: {res.ended_at}</center>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
