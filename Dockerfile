FROM python:3.7-slim

WORKDIR .

COPY blog/requirements.txt blog/requirements.txt

RUN pip3 install -r blog/requirements.txt

COPY . .

CMD [ "python3", "run.py" ] 
