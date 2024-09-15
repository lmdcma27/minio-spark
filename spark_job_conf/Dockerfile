FROM spark-kubernetes/spark-py:1.0.0

USER root

WORKDIR /app

COPY ../python-scripts/requirements.txt .

RUN pip install -r requirements.txt --break-system-packages

COPY ../python-scripts/spark_job.py .
COPY ../python-scripts/spark_job2.py .

