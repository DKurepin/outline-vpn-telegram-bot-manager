FROM python:3.12
WORKDIR /app
COPY . /app

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
CMD ["python", "src/main.py"]