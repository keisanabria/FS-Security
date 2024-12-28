from pathlib import Path
import censusAPI

# Verify if the data to be used is already a CSV file
def verifyFile(fileName, function_name):
    file_path = Path(fileName)

    # Check if the file exists
    if not file_path.exists():
        print(f"{fileName} does not exist. Calling {function_name} to create it.")
        
        # Dynamically call the function in censusAPI with the same name as the file
        if hasattr(censusAPI, function_name):  # Check if the function exists in the module
            func = getattr(censusAPI, function_name)
            func()  # Call the function
        else:
            print(f"Function {function_name} does not exist in censusAPI.")

    # Return True only if the file exists
    return file_path.exists()