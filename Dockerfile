# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /text_to_speech

# Copy the application files into the working directory
COPY . /text_to_speech

# Install the application dependencies
RUN pip install -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
