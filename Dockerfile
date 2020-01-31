FROM python:3

WORKDIR /

COPY choc-o-latine.py requirements.txt /

RUN pip3 install -r /requirements.txt

CMD [ "python3", "-u", "/choc-o-latine.py" ]
