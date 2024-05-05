import peewee as pw
from main import db


class Museum(pw.Model):
    title = pw.CharField(max_length=100)
    description = pw.TextField()
    image = pw.BlobField()

    class Meta:
        database = db


db.create_tables([Museum])
