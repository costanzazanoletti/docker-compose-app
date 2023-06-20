FROM python:3.7.6-buster
COPY . /app
WORKDIR  /app
RUN pip3 install sqlalchemy==1.4
RUN pip3 install pymysql
RUN pip3 install cryptography
RUN pip install pandas
CMD ["python3", "app.py"]