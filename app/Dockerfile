FROM python:3.9

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]