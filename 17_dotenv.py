from dotenv import load_dotenv
load_dotenv()
import os
key = os.getenv('METOFFICE_KEY')

print(key)
