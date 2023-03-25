FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    ucspi-tcp

WORKDIR /ctf

COPY . .

EXPOSE 5000

CMD ["tcpserver", "0.0.0.0", "5000", "python3", "chal.py"]