from recipe_database import engine, ingredient_table, recipe_ingredient, recipe_table, instruction_table
import insert_statements as instmt
from display_recipe import getRecipeData, displayRecipe
import sqlalchemy as sa

def main():
        userMakeRecipe()
        displayRecipe("ramen")
        
                 
def userMakeRecipe():
    title = input("What is the Title of your Recipe?\n").lower()
    ingredients = {}
    instructions = []
    while True:
        ingr_name = input("What ingedient is requireed? (Enter nothing when done)\n - ")
        if ingr_name.strip() != "":
             ingr_amount = input("How much?\n - ")
             ingredients[ingr_name] = ingr_amount
        else:
            break
    print("Type in the instrucitons for your recipe (Enter nothing when Finished):")
    while True:
        instruction = input(" - ")
        if instruction.strip() != "":
             instructions.append(instruction)
        else:
             break
            
    insertRecipe(title, ingredients, instructions)
        

def insertRecipe(r_title, r_ingredients, r_instructions):

    instmt.insertIngredients(r_ingredients)
    instmt.insertRecipes([r_title])

    results = getRecipeData(r_title)
    print("+++++++++++++++++++++++++")
    print(results)
    r_id = results[0]

    instmt.insertInstructions(r_instructions, r_id)
    instmt.insertIngrRec(r_ingredients, r_id)



if __name__ == "__main__":
    main()