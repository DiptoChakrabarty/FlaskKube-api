FROM python
RUN  mkdir app
WORKDIR  /app
COPY  .  .
RUN   apt-get update -y &&  apt-get upgrade -y &&  apt-get install python-mysqldb  -y && pip3 install -r requirements.txt
EXPOSE  5000
CMD  ["python3","app.py"]