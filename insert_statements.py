import sqlalchemy as sa
from recipe_database import engine, ingredient_table, recipe_ingredient, recipe_table, instruction_table

INGR_GRILL_CHEESE = {"Cheddar Cheese": "2 slices",
                      "White Bread": "2 slices",
                      "Butter": "1 Tbsp"}
                      
INSTR_GRILL_CHEESE = ["Put a frying pan on the stove top and set the tempurature to Medium", 
                      "Get 2 slices of White Bread and place 2 slices of Cheddar Cheese In between them",
                      "Butter both sides of the sandwich then place onto the frying pan",
                      "Cook the sandwich until it is golden brown on one side then flip it",
                      "Cook until the other side is golden brown",
                      "Remove the sandwich from the pan and enjoy"]

INGR_HARD_EGG = {"Egg": "1-6",
                 "Salt": "1 tsp"}

INSTR_HARD_EGG = ["Bring a pot of water to a boil",
                  "Carefully insert the eggs into the water",
                  "Let them boil for 9-14 minutes",
                  "Remove the eggs from the water and let sit until cool",
                  "Peel the eggs and enjoy with salt"]

RECIPES = ["Grilled Cheese", "Hard Boiled Eggs"]



def main():
    with engine.connect() as conn:  
        results = conn.execute(sa.text("SELECT * FROM recipe_ingredient"))
        for r in results:
            print(r)



# This section Inserts the Recipes Into the Database
def insertIngredients(ingredients):
    with engine.connect() as conn:
        for ingr in ingredients.keys():
            ingr_text = sa.insert(ingredient_table).values(name=ingr)
            conn.execute(ingr_text)
        conn.commit()

def insertRecipes(recipes):
    with engine.connect() as conn:
        for rec in recipes:
            rec_text = sa.insert(recipe_table).values(title=rec.lower())
            conn.execute(rec_text)
        conn.commit()

def insertInstructions(instructuions, recipe_id_param):
    with engine.connect() as conn:
        step = 1
        for inst in instructuions:
            instr_text = sa.insert(instruction_table).values(recipe_id=recipe_id_param, step=step, text=inst)
            conn.execute(instr_text)
            step = step + 1
        conn.commit()

def insertIngrRec(ingredients, recipe_id_param):
     with engine.connect() as conn:
        for ingr in ingredients:
            # This returns a tuple!!!! dont forget you need to access items inside it
            result = conn.execute(sa.select(ingredient_table.c.id).where(ingredient_table.c.name == ingr)).fetchone()
            ingr_id = result[0]
            # This creates and executes the insert statement
            stmt = sa.insert(recipe_ingredient).values(recipe_id=recipe_id_param, ingredient_id=ingr_id, amount=ingredients[ingr])
            conn.execute(stmt)
        conn.commit()


insertIngredients(INGR_GRILL_CHEESE)
insertIngredients(INGR_HARD_EGG)

insertRecipes(RECIPES)


insertInstructions(INSTR_GRILL_CHEESE, 1)
insertInstructions(INSTR_HARD_EGG, 2)

insertIngrRec(INGR_GRILL_CHEESE, 1)
insertIngrRec(INGR_HARD_EGG, 2)

if __name__ == "__main__":
    main()
