FROM ubuntu
ADD . /src
WORKDIR /src

COPY ./server /root/plotMaker/server
COPY ./frontend/plot-maker/static /var/www/plotMaker/static

RUN apt-get update
RUN apt-get  install -y python3
RUN apt-get install -y python3-pip
RUN python3 -V
RUN pip3 install -r ./requirements.txt
RUN chmod 777 ./run.sh


RUN export DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get install -y nginx
RUN apt-get install -y ufw
RUN ufw allow 'Nginx Full'
COPY plotMaker.conf /etc/nginx/sites-available/plotMaker.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/plotMaker.conf /etc/nginx/sites-enabled/plotMaker.conf
RUN nginx -t
RUN apt-get install -y systemd
# RUN nginx &

RUN python3 -m pip install gunicorn
# COPY gunicorn.service /etc/systemd/system/gunicorn.service
CMD gunicorn server.server.wsgi:application --bind 0.0.0.0:$PORT


