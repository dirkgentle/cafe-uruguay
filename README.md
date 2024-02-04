# Café Uruguay

Bot que hace un post semanal de conversación en [r/uruguay](https://www.reddit.com/r/uruguay/).

## Requisitos

- Python 3.11
- [Python Poetry](https://python-poetry.org/docs/)

## Instalación

- Para desarrollo: `poetry install`
- Para producción: `poetry install --without=dev`

## Correr

- `poetry run python cafe_uruguay/main.py`

Opcionalmente, también hay una imagen de [docker](https://www.docker.com/) que se puede construir con `./build_img.sh` y luego correr con `./run_container.sh`.
