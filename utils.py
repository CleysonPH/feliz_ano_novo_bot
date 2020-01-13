import time

from selenium import webdriver


ATTACHMENT_XPATH = '//*[@id="main"]/header/div[3]/div/div[2]/div'
INPUT_XPATH = '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'


def send_message(driver, contact_name='Sarah', image_number=1):
    print('Procurando contato')
    search_box = driver.find_element_by_class_name('_2zCfw')
    search_box.send_keys(contact_name)
    time.sleep(2)
    contact = driver.find_element_by_xpath(
        f'//span[@title = "{contact_name}" and @class="_19RFN _1ovWX _F7Vk"]')
    contact.click()
    time.sleep(2)

    attach_button = driver.find_element_by_xpath(ATTACHMENT_XPATH)
    attach_button.click()
    time.sleep(1)
    input_button = driver.find_element_by_xpath(INPUT_XPATH)
    input_button.send_keys(
        f'/home/cleysonph/workspaces/python/feliz_ano_novo/img/{image_number}.jpg')
    time.sleep(1)
    attach_message = driver.find_element_by_class_name('_3FeAD')
    attach_message.send_keys('Feliz Ano Novo')
    time.sleep(1)
    send_attach_button = driver.find_element_by_class_name('_1g8sv')
    send_attach_button.click()
    time.sleep(2)
