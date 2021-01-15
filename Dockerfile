FROM joyzoursky/python-chromedriver:latest

WORKDIR /usr/workspace

COPY FB ./FB

RUN pip install PyMySQL && pip install selenium && pip install beautifulsoup4

ENV fb_message_id 1

CMD python FB/getMessage.py ${fb_message_id}