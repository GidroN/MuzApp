import peewee as pw

db = pw.SqliteDatabase('db.sqlite3')


class Museum(pw.Model):
    title = pw.CharField(max_length=100)
    description = pw.TextField()
    image = pw.CharField()
    contacts = pw.TextField()
    website = pw.TextField()
    address = pw.TextField()
    work_time = pw.TextField()

    class Meta:
        database = db
