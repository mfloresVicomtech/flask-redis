# Flask - Reddis example

This is a simple example of Flask and Reddis with a worker with some job types. It includes also rq-dashboard and/or redisinsight for monitoring the queue.

It consists of a *queue* service based on a micro api on Flask and an integrated Redis both running together, and a *worker* service that's just a base Python with *rq* as a dependency and a *jobs.py* script with just a collection of task that it can run.

## How to run

1. Run the thing:
    ```sh
    docker compose -p flask_redis up -d
    ```

2. Check if project works:
[flask-redis](http://localhost:5000)

3. Test it posting some jobs:
    - `curl -X POST 'localhost:5000/job/long_task?delay=5'`
    - `curl -X POST 'localhost:5000/job/io_task?amount=100000000'`
    - `curl -X POST 'localhost:5000/job/cpu_task?power=8'`

4. Monitor :
    - [rq-dashboard](http://localhost:9181)
    - [redisinsight](http://localhost:3000)

