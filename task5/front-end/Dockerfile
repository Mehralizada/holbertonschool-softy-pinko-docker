FROM nginx:latest

COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

COPY ./softy-pinko-front-end.conf  /etc/nginx/conf.d/default.conf

#docker build -f ./front-end/Dockerfile -t softy-pinko-front-end:task2 ./front-end
#docker run -p 9000:9000 -it --rm --name softy-pinko-front-end-task2 softy-pinko-front-end:task2