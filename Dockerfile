# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY text_to_speech /app/text_to_speech
COPY requirements.txt /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Define the entry point for the container
CMD ["python", "-m", "text_to_speech.app"]