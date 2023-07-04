FROM redis:7-alpine

# Install python/pip
RUN apk add --no-cache python3 py3-pip

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 5000 6379

CMD [ "honcho", "start" ]
