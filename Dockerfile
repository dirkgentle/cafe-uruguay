FROM python:3.11-alpine

ENV TZ=America/Montevideo

RUN apk add build-base gcc musl-dev python3-dev libffi-dev openssl-dev cargo pkgconfig
RUN pip install poetry

WORKDIR /cafe_uruguay
COPY pyproject.toml .
COPY poetry.lock .
COPY cafe_uruguay ./cafe_uruguay
COPY README.md .

RUN poetry install --without=dev

CMD ["poetry", "run", "python", "cafe_uruguay/main.py"]
