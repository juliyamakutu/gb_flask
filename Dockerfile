FROM python:3.9.1-buster

WORKDIR /app

COPY pyproject.toml .
COPY pdm.lock .
RUN pip install --no-cache-dir pdm && pdm export -f requirements -o requirements.txt \
    && pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

CMD ["python", "wsgi.py"]

