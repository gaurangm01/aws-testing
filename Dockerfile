FROM python:3.11.1-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirement.txt /code
RUN pip3 install --upgrade pip
RUN pip3 install -r requirement.txt
COPY . /code
EXPOSE 8000
COPY scripts/entrypoint.sh /code
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]