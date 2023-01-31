# start by pulling the python image
FROM python:slim

# copy every content from the local file to the image
COPY . /app

# install the dependencies and packages in the requirements file
RUN pip install -r /app/requirements.txt

CMD sleep 20s && python /app/app.py