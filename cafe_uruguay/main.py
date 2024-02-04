from datetime import date

import praw
import prawcore
from praw.models import Subreddit

from cafe_uruguay.config import AuthConfig, BasicConfig


def _main(debug: bool = False):
    title = f"{BasicConfig.title} {date.today()}"
    body = BasicConfig.body

    reddit_client = praw.Reddit(
        client_id=AuthConfig.client_id,
        client_secret=AuthConfig.client_secret,
        password=AuthConfig.password,
        username=AuthConfig.username,
        user_agent="script for /u/random_daily_subject",
    )

    subreddit = reddit_client.subreddit(BasicConfig.subreddit)

    try:
        flair_id = get_flair_id(subreddit, BasicConfig.flair_text)
    except prawcore.exceptions.Forbidden:
        flair_id = None

    _ = subreddit.submit(title, selftext=body, flair_id=flair_id)


def get_flair_id(subreddit: Subreddit, text: str) -> str | None:
    return next(
        (
            t["id"]
            for t in subreddit.flair.link_templates
            if t["type"] == "richtext"
            and any(chunk.get("t") == text for chunk in t["richtext"])
        ),
        None,
    )


if __name__ == "__main__":
    _main()
