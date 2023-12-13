import logging
from datetime import datetime
import requests
from consolemenu import *
from consolemenu.items import *
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from requests.exceptions import RequestException
from image import DrawImage

class API:
    """Class for interacting with the Random Dog API and managing user interface."""

    url = 'https://dog.ceo/api/breeds/image/random'

    def __init__(self) -> None:
        """Initialize the API object."""
        self.menu = ConsoleMenu("Random Dog API")

        # Add menu items
        self.menu.append_item(FunctionItem("Get image of random dog", self.get_weather))
        self.menu.append_item(FunctionItem("History", self.history))
        self.menu.append_item(FunctionItem("Get image from index of history", self.get_image))
        self.histories = []

    def get_weather(self):
        """Function to get the image of a random dog from the API."""
        pu = PromptUtils(Screen())

        try:
            # Make a request to the API
            response = requests.get(f"{API.url}", headers={'Accept': 'application/json'})
            response.raise_for_status()  # Raise an exception on error response
            json_data = response.json()
            self.histories.append((datetime.now(), json_data['message']))

            # Display the image using DrawImage
            image = DrawImage.from_url(json_data['message'])
            image.draw_image()
            logging.info(f"Image received: {json_data['message']}")
        except RequestException as e:
            logging.error(f"Error while accessing the API: {e}")
            print("Failed to retrieve data from the API")

        pu.enter_to_continue()

    def history(self):
        """Function to display the history of images fetched from the API."""
        pu = PromptUtils(Screen())
        console = Console()

        # Create a table for displaying the history
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Index", style="dim", width=6)
        table.add_column("Timestamp", justify="right")
        table.add_column("Message (URL)")

        # Populate the table with history data
        for index, (timestamp, message) in enumerate(self.histories):
            table.add_row(str(index), timestamp.strftime('%Y-%m-%d %H:%M:%S'), message)

        console.print(table)
        pu.enter_to_continue()

    def get_image(self):
        """Function to get an image from the history based on user input."""
        pu = PromptUtils(Screen())

        try:
            # Get the index from the user and display the corresponding image
            index = int(pu.input("Enter index of history")[0])
            image = DrawImage.from_url(self.histories[index][1])
            image.draw_image()
            logging.info(f"Image from index {index} received")
        except (IndexError, ValueError):
            logging.warning("Invalid index")
            print("Invalid index entered")

        pu.enter_to_continue()

    def run(self):
        """Function to start the API interaction and user interface."""
        self.menu.show()
