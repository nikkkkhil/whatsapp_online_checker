from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pygame
import os
from datetime import datetime
import requests
class WhatsappOnline:
    status = None
    search_bar_selector = '#side > div._2HS9r > div > label > input'
    message_input_selector = """#main > footer > div._2i7Ej.copyable-area > \
        div._13mgZ > div > div._3u328.copyable-text.selectable-text"""
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./media/person_online_notification.mp3')
        self.browser = webdriver.Firefox(executable_path = './bin/geckodriver', log_path = './bin/geckodriver.log')
        self.browser.get('https://web.whatsapp.com')
        print("\nWelcome to the whatsapp bot\n")

    def telegram_bot(self,bot_token,bot_chatID,bot_message):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

    def online_check(self,name):
        search_bar = self.browser.find_element_by_css_selector(
            self.search_bar_selector)
        search_bar.clear()
        search_bar.click()
        search_bar.send_keys(name)
        # press enter to search the person.
        search_bar.send_keys(u'\ue007')
        count= 0
        while(1):
            _status = self.browser.find_element_by_css_selector('#main > header')
            status = _status.text

            if status.find('online') != -1:
                count +=1
                self.status = 'online'
                if count ==1:
                    get_time = datetime.now().strftime("%H:%M:%S:%D")
                    msg = name + " is online at time "+ get_time
                    self.telegram_bot(<telegramAPI>,<telegramchannelID>,msg)
                    print(get_time)
                    pygame.mixer.music.play()
            else:
                self.status = None
                count = 0

            if status:
                print("{} is {}".format(
                    name,
                    'Online' if self.status else 'Offline'
                    )
                )

if __name__ == "__main__":
    user1 = WhatsappOnline()
    name = input("\nEnter the name of the person: ")
    user1.online_check(name)

