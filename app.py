import time
import random

from selenium import webdriver

from utils import send_message


CONTACTS = [
    'Larissa (Vik)',
    'Lucas Artes',
    'Gustavo [IFPI]',
    'Luiz [NTHE]',
    'Sthayllon',
    'Iana',
    'Igor Max (Vik)',
    'Hayssa Campelo',
    'Felipe (IFPI)',
    'Bárbara (Vik)',
    'Washington Jr',
    'Anna IFPI',
    'Gisele (Vik)',
    'Raianne',
    'Rômulo',
    'Valclides',
]

print('Abrindo o webdriver')
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print('Esperando a leitura do QRCode')
time.sleep(15)

for contact_name in CONTACTS:
    image_number = random.randint(1, 43)
    send_message(driver, contact_name, image_number)
