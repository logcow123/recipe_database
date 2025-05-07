import sqlalchemy as sa
import insert_statements
from recipe_database import engine, ingredient_table, recipe_ingredient, recipe_table, instruction_table

ID_INDEX = 0
INGR_NAME_INDEX= 1
INGR_ID_INDEX = 2
AMOUNT_INDEX = 3
INSTR_TECT_INDEX = 3

def main():
    displayRecipe("Grilled Cheese")



def displayRecipe(recipe):
    recipe_data = getRecipeData(recipe.lower())
    if recipe_data != None:
        recipe_id = recipe_data[0]
        recipe_title = recipe_data[1]

        ingr_dict = getIngredients(recipe_id)
        instruction = getInstructions(recipe_id)

        print(f"{recipe_title.title()}: \n")
        print("Ingredients: ")
        for ingr in ingr_dict:
            print(f"{ingr}: {ingr_dict[ingr]}")
        
        print()
        print("Instructions:")
        for i in range(len(instruction)):
            print(f"{i+1}: {instruction[i]}")
    else:
        print("Recipe Does Not Exist")



def getRecipeData(recipe):
    with engine.connect() as conn:
        # when getting results... dont forget to fetch them!!!
        stmt = sa.select(recipe_table).where(recipe_table.c.title == recipe)
        results = conn.execute(stmt).fetchone() # use fetchone() or fetchall()

        return results
    
def getIngredients(recipe_id):
    with engine.connect() as conn:

        stmt = sa.select(recipe_ingredient).where(recipe_ingredient.c.recipe_id == recipe_id)
        results1 = conn.execute(stmt).fetchall()

        ingredients = {}

        for r in results1:
            ingredient_id = r[INGR_ID_INDEX]
            ingr_amount = r[AMOUNT_INDEX]

            stmt = sa.select(ingredient_table).where(ingredient_table.c.id == ingredient_id)
            results2 = conn.execute(stmt).fetchone()

            ingr_name = results2[INGR_NAME_INDEX]

            ingredients[ingr_name] = ingr_amount

        return ingredients

def getInstructions(recipe_id):
    with engine.connect() as conn:
        instructions = []

        stmt = sa.select(instruction_table).where(instruction_table.c.recipe_id  == recipe_id).order_by(instruction_table.c.step)
        results = conn.execute(stmt).fetchall()

        for r in results:
            instructions.append(r[INSTR_TECT_INDEX])
        
        return instructions






if __name__ == "__main__":
    main()