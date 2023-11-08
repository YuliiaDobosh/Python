from consolemenu import *
from consolemenu.items import *

from rich import print as rprint
from rich.console import Console
from rich.table import Table

from datetime import datetime

import requests
from image import DrawImage

class API:
    url = 'https://dog.ceo/api/breeds/image/random'
    def __init__(self) -> None:
        self.menu = ConsoleMenu("Random Dog API")
        
        self.menu.append_item(FunctionItem("Get image of random dog", self.get_weather))
        self.menu.append_item(FunctionItem("History", self.history))
        self.menu.append_item(FunctionItem("Get image from index of history", self.get_image))
        self.histories = []

    def get_weather(self):
        pu = PromptUtils(Screen())

        response = requests.get(f"{API.url}", headers={'Accept': 'application/json'})
        json_data = response.json()
        self.histories.append((datetime.now(), json_data['message']))

        image = DrawImage.from_url(json_data['message'])
        image.draw_image()

        pu.enter_to_continue()

    def history(self):
        pu = PromptUtils(Screen())
        console = Console()
        
        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("Index", style="dim", width=6)
        table.add_column("Timestamp", justify="right")
        table.add_column("Message (URL)")

        for index, (timestamp, message) in enumerate(self.histories):
            table.add_row(str(index), timestamp.strftime('%Y-%m-%d %H:%M:%S'), message)

        console.print(table)
        pu.enter_to_continue()

    def get_image(self):
        pu = PromptUtils(Screen())

        index = int(pu.input("Enter index of history")[0])

        image = DrawImage.from_url(self.histories[index][1])
        image.draw_image()

        pu.enter_to_continue()

    def run(self):
        self.menu.show()