FROM joyzoursky/python-chromedriver:latest

WORKDIR /usr/workspace

COPY FB ./FB

RUN pip install PyMySQL && pip install selenium && pip install beautifulsoup4

ENV fb_message_id 1

ENV db_host 127.0.0.1

ENV db_user user

ENV db_password 123

ENV db_database adpost2021_v1_alpha

CMD python FB/getMessage_v2.py ${db_host} ${db_user} ${db_password} ${db_database}} ${fb_message_id}