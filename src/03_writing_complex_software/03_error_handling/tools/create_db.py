import sqlite3

PATH = "application.db"  # Change this to the path where you want to create the database


def main() -> None:
    conn = sqlite3.connect(PATH)

    curr = conn.cursor()

    # Create table
    curr.execute(
        """CREATE TABLE blogs
        (id text not null primary key, date text, title text, content text, public integer)"""
    )

    # Insert a few rows of data
    curr.execute(
        """INSERT INTO blogs VALUES
        ('first-blog', '2021-03-07', 'My first blog' ,'Some content', 1)"""
    )
    curr.execute(
        """INSERT INTO blogs VALUES
        ('private-blog', '2021-03-07', 'Secret blog' ,'This is a secret', 0)"""
    )

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


if __name__ == "__main__":
    main()
