from recipe_database import *
import sqlalchemy as sa

def main():
    pass

def deleteRecipe(rec_id):
    with engine.connect() as conn:
        stmt = sa.delete(instruction_table).where(instruction_table.c.recipe_id==rec_id)
        conn.execute(stmt)

        stmt = sa.delete(recipe_ingredient).where(recipe_ingredient.c.recipe_id==rec_id)
        conn.execute(stmt)

        stmt = sa.delete(recipe_table).where(recipe_table.c.id==rec_id)
        conn.execute(stmt)

        conn.commit()




if __name__ =="__main__":
    main()