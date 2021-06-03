FROM python:3.8-slim
RUN mkdir /app/
ADD . /app/
WORKDIR /app/

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python3", "/app/train/manage.py", "runserver", "0.0.0.0:8000"] 