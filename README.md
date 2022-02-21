* Before run application (in local):

```
$ sudo apt update.
$ sudo apt install libpq-dev gdal-bin libgdal-dev
$ python3 -m venv venv
$ pip install -r requirements.txt
$ python3 main.py
```

* Run application:

```
$ python3 main.py
```

* Run application in docker container:

```
$ docker build -t kml-to-shp-converter:latest .
$ docker run -t kml-to-shp-converter:latest
```

* Run application in docker container into the shell:

```
$ docker run -t kml-to-shp-converter:latest /bin/bash
```

* Useful docker command:

```
$ docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -f "dangling=true" -q)
```