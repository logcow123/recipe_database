from display_recipe import displayRecipe, getAllRecipes
from insert_recipe import insertRecipe, userMakeRecipe
from update_recipe import *
import os

def main():
    continue_program = True
    while continue_program:
        os.system("clear")
        menu()
        user_input = input()
        match (user_input):
            case "1":
                os.system("clear")
                case1()
                input()
            case "2":
                case2()
            case "3":
                case3()
            case "4":
                print("Case 4")
            case "5":
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


def case2():
    os.system("clear")
    userMakeRecipe()

def case3():
    os.system("clear")
    print("What recipe would you like to update?")

    recipes = getAllRecipes()
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
    rec_id = int(rec_id)
    os.system("clear")
    print("What would you like to update?")
    print("[1] Title\n"
          "[2] Ingredient\n"
          "[3] Instruction")
    user_input = input()
    os.system("clear")
    match user_input:
        case "1":
            new_title = input("What is the new title?\n")
            updateRecTitle(rec_id, new_title)
            print("Completed")
        case "2":
            userUpdateIngr(rec_id)
        case "3":
            userUpdateInstr(rec_id)


    

if __name__ =="__main__":
    main()