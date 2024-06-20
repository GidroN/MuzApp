from playhouse.migrate import *
my_db = SqliteDatabase('db.sqlite3')
migrator = SqliteMigrator(my_db)


migrate(
    migrator.add_column('museum', 'work_time',work_time),
)