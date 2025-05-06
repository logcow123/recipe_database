import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import List, Optional


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

print("BEFORE CREATION")
# allows for metadata to be created
meta_data_obj = sa.MetaData()

# creating a table in an Object Orientated way
user_table = sa.Table(
    "user_account",
    meta_data_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(30)),
    sa.Column("fullname", sa.String)
)

# Using a Foriegn key in another table
address_table = sa.Table(
    "address",
    meta_data_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.ForeignKey("user_account.id"), nullable=False),
    sa.Column("email_address", sa.String, nullable=False),
)

#after declareing the objects, the meta_data_obj can create the tables for us
meta_data_obj.create_all(engine)



# ORM version of creating tables

# creates a delcarative base that allows use of the meta-data collection
class Base(so.DeclarativeBase):
    pass

# example table
class User(Base):
    __tablename__ = "user_account"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(30))
    fullname: so.Mapped[Optional[str]]

    addresses: so.Mapped[List["Address"]] = so.relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
class Address(Base):
    __tablename__ = "address"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    email_address: so.Mapped[str]
    user_id = so.mapped_column(sa.ForeignKey("user_account.id"))

    user: so.Mapped[User] = so.relationship(back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)



# using .insert() to make an insert statment
stmt = sa.insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
print(stmt)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit
    print(result.inserted_primary_key)

print(sa.insert(user_table))
