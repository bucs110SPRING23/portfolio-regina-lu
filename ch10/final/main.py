import meal, margarita

def main():
    dishoftheday = meal.mealAPI()
    dish = dishoftheday.get()
    marg = margarita.margaritaAPI()
    drink = marg.get()

    for data in dish:
        currentdish = data['strMeal']
        foodinstructions = data['strInstructions']
        youtubevideo = data['strYoutube']
        
    print("Today's menu is: " + currentdish)

    while True:
        tutorial = input('Do you want to learn how to make it? ("yes" or "no") ')
        if tutorial == "yes":
            print(foodinstructions)    
            video = input('Would you like to watch a video tutorial? ("yes" or "no") ')
            if video == "yes":
                print(youtubevideo)
                print("Hope that was helpful! \nNow lets move on to today's drink")
            else:
                print("Let's move on to the drinks")
            
            for data in drink:
                drinkinstructions_eng = data['strInstructions']
                drinkinstructions_it = data['strInstructionsIT']
            
            print("Today's drink menu is: Margarita")
            language = input('See instructions in: "English" or "Italian"? ')
            if language == "Italian" or language == "italian":
                print(drinkinstructions_it)
            else:
                print(drinkinstructions_eng)
            return False
        else:
            dishoftheday.change_meal()
            newmeal = dishoftheday.get()
            for data in newmeal:
                dish_new = data['strMeal']
                foodinstructions = data['strInstructions']
                youtubevideo = data['strYoutube']
            print(dish_new)

main()