FROM python:3.11.1-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip3 install psycopg2==2.9.1
COPY . /code
EXPOSE 8000
COPY entrypoint.sh /code
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]