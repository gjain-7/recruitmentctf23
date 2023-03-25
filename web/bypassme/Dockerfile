FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    ucspi-tcp \
    mysql-server \
    libmysqlclient-dev 

WORKDIR /ctf

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
COPY .env .env


EXPOSE 5000

RUN mkdir /nonexistent
CMD ["service", "mysql", "start"]
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]