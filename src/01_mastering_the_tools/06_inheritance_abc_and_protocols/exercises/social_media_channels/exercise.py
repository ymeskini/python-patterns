from dataclasses import dataclass
from time import time
from typing import Protocol


class SocialChannel(Protocol):
    followers: int

    def post(self, message: str) -> None: ...


@dataclass
class YoutubeChannel:
    followers: int

    def post(self, message: str) -> None:
        print(f"youtube channel: {message}")


@dataclass
class FacebookChannel:
    followers: int

    def post(self, message: str) -> None:
        print(f"facebook channel: {message}")


@dataclass
class TwitterChannel:
    followers: int

    def post(self, message: str) -> None:
        print(f"twitter channel: {message}")


@dataclass
class Post:
    message: str
    timestamp: int


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time():
                channel.post(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels: list[SocialChannel] = [
        YoutubeChannel(100),
        FacebookChannel(100),
        TwitterChannel(100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
