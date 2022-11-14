# Flask - Reddis test

This is a simple test of Flask and Reddis using Docker Composer. It includes also rq-dashboard for monitoring the queue.

## How to run

1. Create Docker stack
```sh
docker-compose build
docker-compose -p flask_redis up --build -d
```

2. Check if project works:
[http://localhost:9999](http://localhost:9999)

3. Monitor rq-dashboard:
[http://localhost:9181](http://localhost:9181)

