FROM python:3.11.5-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-warn-script-location -r requirements.txt

COPY src ./src

CMD ["src/manage.py", "runserver". "0.0.0.0:8000"]
