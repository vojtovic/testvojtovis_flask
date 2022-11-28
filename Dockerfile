FROM python:3.10
WORKDIR /code
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["python", "run.py"]
