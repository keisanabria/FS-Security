import mapCreation
import total_calories
import insec_households
import collapseData
import acs_year

# Show map 
def main() -> None:

    # Data-fetching code
    totalCals = total_calories.getTotalCalories()
    insecHouses = insec_households.getInsecHouseholds()

    mapCreation.createMap('total_calories', totalCals)
    mapCreation.createMap('esti_insec_households', insecHouses)
    mapCreation.createMap('per_insec_households', insecHouses)

    collapseData.add_sheet_with_dataframe(str(acs_year.getACS_year()), total_calories.getTotalCalories())

if __name__ == "__main__":
    main()