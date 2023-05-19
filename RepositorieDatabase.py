import sqlite3


class RepoDatabase:
    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            create table if not exists repositories (
                id integer primary key,
                title text,
                desc text,
                language text 
            )
        """)

    def add_repos(self, repo):
        self.cursor.execute("""
            insert into repositories (title, desc, language)
            values (?,?,?)
        """, (repo.title, repo.desc, repo.language))
        self.conn.commit()
