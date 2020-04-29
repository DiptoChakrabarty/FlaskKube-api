FROM python
RUN  mkdir app
WORKDIR  /app
COPY  .  .
RUN "pip install -r requirements.txt"
EXPOSE  5000
CMD  ["python","app.py"]