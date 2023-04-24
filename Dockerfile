FROM python:3.9.1-buster

WORKDIR /app

COPY pyproject.toml .
COPY pdm.lock .
RUN pip install --no-cache-dir pdm && pdm export -f requirements -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY wsgi.py wsgi.py
COPY blog ./blog
COPY migrations ./migrations
COPY entrypoint.sh entrypoint.sh

RUN chmod u+x ./entrypoint.sh

EXPOSE 8080

CMD ["./entrypoint.sh"]

