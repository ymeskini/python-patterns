from dataclasses import dataclass
import sqlite3
from datetime import datetime
from typing import Any
from pydantic import BaseModel


class AccessError(Exception):
    pass


@dataclass
class NotFoundError(Exception):
    id: str


@dataclass
class NotAuthorizedError(AccessError):
    id: str


@dataclass
class NotAuthenticatedError(AccessError):
    id: str


class Blog(BaseModel):
    id: str
    date: datetime
    title: str
    content: str
    public: bool


def fetch_blog(blog_id: str) -> Blog | None:
    conn = sqlite3.connect("./using_exception_classes/application.db")
    conn.row_factory = sqlite3.Row

    try:
        curr = conn.cursor()

        curr.execute("SELECT * FROM blogs where id=?", [blog_id])
        result: tuple[Any] = curr.fetchone()

        blog_attrs = dict(result)

        blog = Blog(**blog_attrs)

        if not blog.public:
            raise NotAuthorizedError(blog_id)

        conn.close()

    except AccessError as _e:
        print("Access denied")
        return None

    return blog


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
