FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start Gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
