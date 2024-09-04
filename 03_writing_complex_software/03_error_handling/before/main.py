import sqlite3
from datetime import datetime
from typing import Any
from pydantic import BaseModel


class Blog(BaseModel):
    id: str
    date: datetime
    title: str
    content: str
    public: bool


def fetch_blog(blog_id: str) -> Blog | None:
    conn = sqlite3.connect("./before/application.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM blogs where id=?", [blog_id])
    result: tuple[Any] = cursor.fetchone()

    blog_attrs = dict(result)

    blog = Blog(**blog_attrs)

    conn.close()

    return blog


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
