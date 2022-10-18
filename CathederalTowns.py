class Town:
    def __init__(self, name, pop, county):
        self.name = name
        self.pop = pop
        self.county = county
        
def main():
    towns = []
    
    while True:
        name = input("enter the name of a town (or 'END' to end) > ")
        if name.lower() == "end":
            break
        population = input(f"enter the population of town {name} > ")
        county = input(f"enter the county that {name} is located in > ")
        town = Town(name, population, county)
        towns.append(town)

    while True:
        county = input("enter a county to search for > ")
        if county.lower() == "end":
            break
            
        print(f"cathederal towns found in {county}:")
        for town in towns:
            if town.county == county:
                print(f"{town.name} | population: {town.pop}")
                


main()
