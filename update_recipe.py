import sqlalchemy as sa
from recipe_database import *
from display_recipe import displayRecipe
import os
from insert_statements import insertIngredient

INGR_INDEX = 2

def main():
    os.system("clear")
    displayRecipe(1)
    updateInstr(1, "Updated instrucion One")
    displayRecipe(1)

def updateRecTitle(rec_id, new_title):
    with engine.connect() as conn:
        stmt = sa.update(recipe_table).where(recipe_table.c.id==rec_id).values(title=new_title)
        conn.execute(stmt)
        conn.commit()

def updateRecIngr(rec_ingr_id, new_ingr, new_amount):
    new_ingr_id = insertIngredient(new_ingr)
    with engine.connect() as conn:
        stmt = sa.update(recipe_ingredient).where(recipe_ingredient.c.id==rec_ingr_id).values(ingredient_id=new_ingr_id, amount=new_amount)
        conn.execute(stmt)
        conn.commit()

def updateInstr(instr_id, new_instr):
    with engine.connect() as conn:
        stmt = sa.update(instruction_table).where(instruction_table.c.id==instr_id).values(text=new_instr)
        conn.execute(stmt)
        conn.commit()

def userUpdateInstr(rec_id):
    with engine.connect() as conn:
        stmt = sa.select(instruction_table).where(instruction_table.c.recipe_id==rec_id)
        results = conn.execute(stmt).fetchall()

        for instr in results:
            print(f"ID: {instr[0]:<3} {instr[3]}")
        print()
        print("Which instruction would you like to update (Enter the ID)")
        valid_input = False
        while valid_input == False:
            instr_id = input()
            try:
                int(instr_id)
                valid_input = True
            except:
                print("Enter A Valid Input!")
        instr_id = int(instr_id)
        os.system("clear")
        print("What do you want the new instruction to be?")
        new_instr = input()
        updateInstr(instr_id, new_instr)

def userUpdateIngr(rec_id):
    with engine.connect() as conn:
        stmt = sa.select(recipe_ingredient).where(recipe_ingredient.c.recipe_id==rec_id)
        results = conn.execute(stmt).fetchall()
        ingredients = {}
        for result in results:
            ingr_id = result[INGR_INDEX]
            stmt = sa.select(ingredient_table.c.name).where(ingredient_table.c.id==ingr_id)
            ingr = conn.execute(stmt).fetchone()
            ingredients[ingr_id] = ingr

        print()
        print("Which ingredient would you like to update?")

        for ingr in results:
            ingredient = ingredients[ingr[INGR_INDEX]]
            print(f"ID: {ingr[0]:<3} {ingredient[0]:<20}, {ingr[3]}")
        print()
        print("Which ingredient would you like to update (Enter the ID)")
        valid_input = False
        while valid_input == False:
            ingr_id = input()
            try:
                int(ingr_id)
                valid_input = True
            except:
                print("Enter A Valid Input!")
        ingr_id = int(ingr_id)
        os.system("clear")
        print("What do you want the new Ingredient to be?")
        new_ingr = input()
        print("How much?")
        new_amount = input()
        updateRecIngr(ingr_id, new_ingr, new_amount)


if __name__ == "__main__":
    main()