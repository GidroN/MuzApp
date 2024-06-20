from playhouse.migrate import *
from peewee import SqliteDatabase, ForeignKeyField
from models import MapCoordinates

# Initialize the database
my_db = SqliteDatabase('db.sqlite3')
migrator = SqliteMigrator(my_db)

# Define the ForeignKeyField with the correct field reference
coordinates = ForeignKeyField(MapCoordinates, field=MapCoordinates.id, backref='museum', default=1)

# Perform the migration to add the new column
migrate(
    migrator.add_column('museum', 'coordinates_id', coordinates)
)

