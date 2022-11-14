FROM python:3.10-alpine
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["python", "app.py"]