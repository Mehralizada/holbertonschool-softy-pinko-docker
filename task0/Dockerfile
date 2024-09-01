# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Update APT and upgrade installed packages
RUN apt-get update && \
    apt-get upgrade -y

# Create a script that echoes "Hello, World!" and make it executable
RUN echo 'echo "Hello, World!"' > /hello.sh && chmod +x /hello.sh

# Specify the command to run when the container starts
CMD ["/hello.sh"]
