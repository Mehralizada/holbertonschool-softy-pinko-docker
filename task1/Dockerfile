# Use the official Ubuntu image as a parent image
FROM ubuntu:latest

# Update and install necessary packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip

# Remove the EXTERNALLY-MANAGED flag if it exists
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Install Flask using pip3
RUN pip3 install flask

# Set the working directory in the container
WORKDIR /app

# Copy the local python file to the container
COPY api.py /app/api.py

# Command to run the Flask app
CMD ["python3", "api.py"]
.
