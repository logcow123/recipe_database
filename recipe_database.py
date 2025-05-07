import sqlalchemy as sa


# I will use memory for now until I have everything sorted
engine = sa.create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata_obj = sa.MetaData()

#This section creates all the Tables
recipe_table = sa.Table(
    "recipe",
    metadata_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(30))
)

ingredient_table = sa.Table(
    "ingredient",
    metadata_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(30))
)

instruction_table = sa.Table(
    "instruction",
    metadata_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("recipe_id", sa.ForeignKey("recipe.id"), nullable=False),
    sa.Column("step", sa.Integer),
    sa.Column("text", sa.String)
)

recipe_ingredient = sa.Table(
    "recipe_ingredient",
    metadata_obj,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("recipe_id", sa.ForeignKey("recipe.id"), nullable=False),
    sa.Column("ingredient_id", sa.ForeignKey("ingredient.id"), nullable=False),
    sa.Column("amount", sa.String)
)
# This Commits the tables
metadata_obj.create_all(engine)



    