import mapCreation
import total_calories
import insec_households

# Show map 
def main() -> None:

    # Data-fetching code
    totalCals = total_calories.getTotalCalories()
    insecHouses = insec_households.getInsecHouseholds()

    mapCreation.createMap('total_calories', totalCals)
    mapCreation.createMap('esti_insec_households', insecHouses)
    mapCreation.createMap('per_insec_households', insecHouses)

if __name__ == "__main__":
    main()