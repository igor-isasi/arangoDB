FROM python:3

ADD arangodb-client.py .

RUN pip install python-arango

CMD [ "python", "./arangodb-client.py" ]