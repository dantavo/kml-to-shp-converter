FROM osgeo/gdal:ubuntu-small-3.4.1

LABEL maintainer="Daniele Tavolaro"

RUN mkdir /app
RUN mkdir /app/dat
RUN mkdir /app/out

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY dat/*.kml app/dat/

WORKDIR /app

ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install --no-install-recommends -y ca-certificates vim curl autoconf libtool automake build-essential gcc python3-dev python3-pip python3-setuptools python3-virtualenv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]