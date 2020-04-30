FROM python
RUN  mkdir app
WORKDIR  /app
COPY  .  .
RUN      pip3 install -r requirements.txt
EXPOSE  5000
CMD  ["python3","app.py"]