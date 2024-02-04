import os

from dotenv import load_dotenv

load_dotenv()


class AuthConfig:
    password = os.getenv("REDDIT_PWD")
    username = os.getenv("REDDIT_USERNAME")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")


class BasicConfig:
    debug_mode = bool(os.getenv("REDDIT_DEBUG"))
    subreddit = os.getenv("REDDIT_SUBREDDIT", "Uruguay" if not debug_mode else "test")

    title = "Café Uruguay"

    body = (
        "Bienvenidos y bienvenidas al café de /r/Uruguay, un espacio semanal"
        " para relajarse y charlar. Vayan tomando asiento, en un momento les"
        " llevamos la orden."
        "\n\n*****\n\n"
        " *En estos posts no aplica la regla de contenido relacionado con Uruguay.*"
        " Pueden hablar de lo que quieran,"
        " mientras no rompa ninguna otra regla de Reddit o del sub."
        " Prohibido salivar y hablar con el conductor."
        " \n\n*****\n\n"
        " *Bot by \\/u/DirkGentle.*"
        " [Source.](https://github.com/dirkgentle/cafe-uruguay)"
    )

    flair_text = os.getenv("REDDIT_FLAIR", "AskUruguay 🧉")
