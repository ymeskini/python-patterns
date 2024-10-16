from dataclasses import dataclass
import os
import sqlite3
from datetime import datetime
from typing import Any
from pydantic import BaseModel
from logging import Logger

logger = Logger(__name__)


CURRENT_DIRECTORY = os.path.dirname(__file__)
DATABASE_FILEPATH = os.path.join(CURRENT_DIRECTORY, './application.db')

@dataclass
class SQLiteConnectionManager:
    file_path: str
    conn: sqlite3.Connection | None = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.file_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type: str, value: Any, traceback: Any):
        logger.info("Closing the connection")
        if self.conn:
            self.conn.close()


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
    with SQLiteConnectionManager(file_path=DATABASE_FILEPATH) as cursor:
        cursor.execute("SELECT * FROM blogs where id=?", [blog_id])
        result: tuple[Any] | None = cursor.fetchone()

        if result is None:
            raise NotFoundError(blog_id)

        blog_attrs = dict(result)

        blog = Blog(**blog_attrs)

        if not blog.public:
            raise NotAuthorizedError(blog_id)

    return blog


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
