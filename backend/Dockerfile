FROM python:3.12.0-bullseye
#RUN apt update -y && apt upgrade -y
COPY ./web/. /home/edu/.
WORKDIR /home/edu/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /home/edu/req.txt