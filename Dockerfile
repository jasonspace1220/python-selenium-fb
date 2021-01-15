FROM joyzoursky/python-chromedriver:latest

WORKDIR /usr/workspace

COPY FB ./FB

RUN pip install PyMySQL && pip install selenium && pip install beautifulsoup4

CMD python FB/getMessage.py