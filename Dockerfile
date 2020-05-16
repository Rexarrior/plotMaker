FROM ubuntu
ADD . /src
WORKDIR /src

COPY ./server /root/plotMaker/server
COPY ./frontend/plot-maker/static /var/www/plotMaker/static

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -V
RUN pip3 install -r ./requirements.txt
RUN chmod 777 ./run.sh

RUN apt-get install nginx
RUN apt-get install ufw
RUN ufw "Nginx Full"
COPY plotMaker.conf /etc/nginx/sites-available/plotMaker.conf
RUN rm /etc/nginx/sites-enabled/default
RUN li -s /etc/nginx/sites-available/plotMaker.conf /etc/nginx/sites-enabled/plotMaker.conf
RUN nginx -t
RUN systemctl restart nginx

RUN apt-get install gunicorn3
COPY gunicorn.service /etc/systemd/system/gunicorn.service
RUN systemctl daemon-reload
RUN systemctl start gunicorn
