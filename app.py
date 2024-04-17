from vetiver import VetiverModel
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins
# From Chapter 4
import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

load_dotenv(find_dotenv())

# This stuff loaded in from chapter 6
b = pins.board_folder('data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240306T195822Z-a6f9b')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app

vetiver_api.run(port = 8080)

# if i want to run shiny app, I have to type py app.py in the terminal and then run 
# my app.R to get the prediction thing. 
