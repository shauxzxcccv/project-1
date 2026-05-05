countries = []

while True:

    main = input("\nDo you want to know about a country add it or exit? (add/view/exit): \n")

    if main == "exit":
        print("\nThank you for using the country information system.\n")
        print("\n Exiting...\n")
        break

    elif main == "add":

        while True:
            name = input("\nEnter the name of the country: \n")
            code = input("\nEnter the country code: \n")
            population = input("\nEnter the population: \n")
            location = input("\nEnter the location: \n")
            president = input("\nEnter the name of the president: \n")

            country = {
                "name": name,
                "code": code,
                "population": population,
                "location": location,
                "president": president
            }

            countries.append(country)
            print("\nCountry added successfully!\n")
            break

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
                choice = input("\nWhich country do you want to know about? (Enter the name of the country): \n")
                if choice in [country["name"] for country in countries]:
                    selected_country = next(country for country in countries if country["name"] == choice)
                    
                    while True:
    
                        info = input("\nEnter the information you want to know (code/population/location/president): \n")
    
                        if info in selected_country:
                            print("\n" + "Answer: " + str(selected_country[info]) + "\n")
                            break
                        
                        else:
                            print("\nInvalid information. Please enter one of the following: (code, population, location, president).\n")
                            continue


#while True:
#    if main == "view":
#        choice = input("\nWhich country do you want to know about? (Enter the name of the country): \n")
#        if choice in [country["name"] for country in countries]:
#            selected_country = next(country for country in countries if country["name"] == choice)
#            info = input("\nEnter the information you want to know (code/population/location/president): \n")
#            if info in selected_country:
#                print("\n" + "Answer: " + str(selected_country[info]) + "\n")
#                break
#            else:
#                print("\nInvalid information. Please enter one of the following: (code, population, location, president).\n")
#                continue