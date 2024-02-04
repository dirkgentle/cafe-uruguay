FROM python:3.11.3

ENV TZ=America/Montevideo

RUN pip install poetry

WORKDIR /cafe_uruguay
COPY pyproject.toml .
COPY poetry.lock .
COPY cafe_uruguay ./cafe_uruguay

RUN poetry install --without=dev

CMD ["poetry", "run", "python", "cafe_uruguay/main.py"]
