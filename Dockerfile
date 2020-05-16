FROM alpine:3.5
RUN apk add --update python3 py-pip
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY server /src/server
COPY run.sh /src/run.sh
CMD ./src/run.sh