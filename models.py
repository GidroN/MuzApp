import peewee as pw

db = pw.SqliteDatabase('db.sqlite3')


class Museum(pw.Model):
    title = pw.CharField(max_length=100)
    description = pw.TextField()
    image = pw.CharField()

    class Meta:
        database = db

