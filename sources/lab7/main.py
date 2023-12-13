import requests
from .api import API

def main():
    """Main function to run the Random Dog API interaction."""
    # Create an instance of the API class
    api = API()

    # Run the API interaction and user interface
    api.run()

if __name__ == '__main__':
    # Execute the main function if the script is run as the main program
    main()
