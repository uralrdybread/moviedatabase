
# coding: utf-8

# In[ ]:


films = {
    "Sponge Bob Returns":[3,4],
    "Samurai Duel":[18,5],
    "Boba Fett's Revenge":[18,3],
    "Black Panther 2":[15,5],    
    }

# Small film database

film_list = "Currently playing: Sponge Bob Returns, Samurai Duel, Boba Fett's Revenge and Black Panther 2."
print(film_list)
while True:
    choice = input("What film would you like to watch?: ").title()
    
    if choice in films:
        age = int(input("How old are you?: "))
        
        # age checker
        
        if age >= films[choice][0]:
            
            # seat checker
            
            num_seats = films[choice][1]
            
            #created a variable to help simplify the reservasion process
            
            if num_seats > 0:
                print("Thank you and enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, but this movie is sold out.")
        else:
            print("I'm very sorry but you're too young to watch this film")
    
    else:
        print("That film is currently not playing. Please select a film from the list provided")

