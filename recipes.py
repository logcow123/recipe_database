from display_recipe import displayRecipe, getAllRecipes
from insert_recipe import insertRecipe, userMakeRecipe
import os

def main():
    continue_program = True
    while continue_program:
        os.system("clear")
        menu()
        user_input = input()
        match (user_input):
            case "1":
                case1()
            case "2":
                print("Case 2")
            case "3":
                print("Case 3")
            case "4":
                print("Case 4")
            case "5":
                print("Case 5")
                continue_program = False

def menu():
    print("Welcome to the Recipe Database! Choose an option")
    print("[1] Display Recipe")
    print("[2] Create Recipe")
    print("[3] Update recipe")
    print("[4] Delete recipe")
    print("[5] Quit")

def case1():
    recipes = getAllRecipes()
    os.system("clear")
    print("Type in the ID of the recipe you want")
    for recipe in recipes:
        title = recipe[1].title()
        print(f" - {title:<20}ID: {recipe[0]}")
    valid_input = False
    while valid_input == False:
        rec_id = input()
        try:
            int(rec_id)
            valid_input = True
        except:
            print("Please enter a valid Number!")
    os.system("clear")
    displayRecipe(int(rec_id))
    input()
    

if __name__ =="__main__":
    main()