import sqlalchemy as sa
import sqlalchemy.orm as so

#   create engine || what database || What DBAPI || Location [echo means that it will log all the SQL the engine emtis]
engine = sa.create_engine("sqlite+pysqlite:///:memory:", echo=True)

# This establishes a connection with the DB with the context manager(like opening a file)
with engine.connect() as conn:
    # the sa.text() can run sqlite code directly but is not the main feature of sqlalchemy
    result = conn.execute(sa.text("SELECT 'Hello World'"))
    print(result.all())

# commiting changes to the engine (commit as you go method)
with engine.connect() as conn:
    conn.execute(sa.text("CREATE TABLE example (x int, y int)"))
    conn.execute(
        sa.text("INSERT INTO example (x, y) VALUES (:x, :y)"), 
        [{"x": 1, "y": 2}, {"x": 2, "y": 4}])
    conn.commit()

# another way to commit (begin once method **PREFERED**)
#  the 'engine.begin()' function will auto commit the block of code or will rollback if there was an exception
with engine.begin() as conn:
    conn.execute(
        sa.text("INSERT INTO example (x, y) VALUES (:x, :y)"), 
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}])

# fetching results   
with engine.connect() as conn:
    # reslut contains a list of tuples
    result = conn.execute(sa.text("SELECT x, y FROM example"))
    for row in result:
        # row in this context is a named tuple
        print(f"x: {row.x}  y: {row.y}")

with engine.connect() as conn:
    conn.execute(
        sa.text("INSERT INTO example (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
    )
    conn.commit()

# using the ORM version of connection (Session) 
stmt = sa.text("SELECT x, y FROM example WHERE y > :y ORDER BY x, y")
with so.Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

with so.Session(engine) as session:
    result = session.execute(
        sa.text("UPDATE example SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()