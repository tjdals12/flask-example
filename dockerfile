FROM python:3.8.1

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 4000

CMD ["python", "app/app.py"]