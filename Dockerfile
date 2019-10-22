FROM python:3

WORKDIR /

COPY crypteur.py requirements.txt /

RUN pip3 install -r /requirements.txt

CMD [ "python3", "-u", "/crypteur.py" ]