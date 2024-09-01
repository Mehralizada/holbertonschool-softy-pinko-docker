FROM ubuntu:latest

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get install -y python3 python3-pip

# Remove EXTERNALLY-MANAGED file if present to avoid pip install issues
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

RUN pip3 install flask

RUN pip3 install flask-cors

WORKDIR /app

COPY ./api.py /app/api.py

CMD [ "python3", "api.py" ]

#First terminal building/running the backend:
#docker build -f ./back-end/Dockerfile -t softy-pinko-back-end:task3 ./back-end
#docker run -p 5252:5252 -it --rm --name softy-pinko-back-end-task3 softy-pinko-back-end:task3

#Second terminal building/running the front-end:
#docker build -f ./front-end/Dockerfile -t softy-pinko-front-end:task3 ./front-end
#docker run -p 9000:9000 -it --rm --name softy-pinko-front-end-task3 softy-pinko-front-end:task3