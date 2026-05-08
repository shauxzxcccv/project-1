countries = []

while True:

    main = input("\nDo you want to know about a country add it or exit? (add/view/exit): \n")

    if main == "exit":
        print("\nThank you for using the country information system.\n")
        print("\n Exiting...\n")
        break

    elif main == "add":
            
            name = input("\nEnter the name of the country: \n")
            code = input("\nEnter the country code: \n")
            population = input("\nEnter the population: \n")
            location = input("\nEnter the location: \n")
            president = input("\nEnter the name of the president: \n")

            country = {
                "name": name,
                "code": code,                                   # -- as "code" user can use numerical prefixes of the countries(+48, +49, +1) or three-letter abbreviations(POL, GER, USA)
                "population": population,
                "location": location,
                "president": president
            }

            countries.append(country)
            print("\nCountry added successfully!\n")
            continue

    elif main != "add" and main != "view" and main != "exit":
        print("\nInvalid input. Please enter 'add', 'view', or 'exit'.\n")
        continue

    elif main == "view":
        if not countries:
            print("\nNo countries added yet. Please add a country first.\n")
            continue

        elif main == "view":

            print("\nAvailable countries:")

            for country in countries:
                print("- " + country["name"])
                continue
    while True: 
        choice = input("\nType name of the country you want to view, or go back to the main menu: (Enter the name of country/main menu) \n")
        
        if choice in [country["name"] for country in countries]:
                
                selected_country = next(country for country in countries if country["name"] == choice)
                for key, value in selected_country.items():
                    print(f"{key:<10} | {value}")
                    continue

#                while True:                                                                                                                #
#                                                                                                                                           #
#                        info = input("\nEnter the information you want to know (code/population/location/president): \n")                  #
#                                                                                                                                           #
#                        if info in selected_country:                                                                                       #
#                            print("\n" + "Answer: " + str(selected_country[info]) + "\n")                                                  #           -- if you want to use special search via keys 
#                            break                                                                                                          #              to find more specific information
#                                                                                                                                           #
#                        else:                                                                                                              #
#                            print("\nInvalid information. Please enter one of the following: (code, population, location, president).\n")  #
#                            continue                                                                                                       #

        elif choice == "main menu":
             break
        
        else:
             print("\n Invalid answer. Please, try again.\n")
             continue


