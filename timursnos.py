# -*- coding: utf-8 -*-
from colorama import init, Fore
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time 
import pystyle
from time import sleep
import platform
import os

#Поставь сюда свои почты, эти скорей всего уже разьебаны 
senders = {
    'lstefanick@hotmail.com1':'Luv2dance2','bchavez123@mail.com1':'aadrianachavez','lukejamesjones@mail.com1':'tinkerbell1','emahoney123@comcast.net1':'Shieknmme3#','mandy10.mcevoy@btinternet.com1':'Tr1plets3','jet747@cox.net1':'Sadie@1234','landsgascareservices@mail.com1':'Alisha25@','samantha224@mail.com1':'Madden098!@','kbhamil@wowway.com1':'Carol1940','email@bjasper.com1':'Lhsnh4us123!','biggsbrian@cox.net1':'Trains@2247Trains@2247','dzzeblnd@aol.com1':'Geosgal@1','jtrego@indy.rr.com1':'Jackwill14!','chrisphonte.rj@comcast.net1':'Junior@3311','tvwifiguy@comcast.net1':'Bill#0101','defenestrador@mail.com1':'m0rb1d8ss','glangley@gmx.com1':'ironhide','charlotte2850@hotmail.com1':'kelalu2850'
}

# Получатели
receivers = ['security@telegram.org', 'abuse@telegram.org', '']


def pidor():
    sleep(3)
    init()
    pidor = '''    
                        ╔═══════════════════════════════════════════════════════════════════════════════╗
                        ║                                                                               ║  
                        ║                 ▄████▄   ██░ ██  ▒█████   ▄████▄ ▓█████ ██▓███                ║   
                        ║                ▒██▀ ▀█ ▒▓██░ ██ ▒██▒  ██▒▒██▀ ▀█ ▓█   ▀▓██░  ██               ║  
                        ║                ▒▓█    ▄░▒██▀▀██ ▒██░  ██▒▒▓█    ▄▒███  ▓██░ ██▓▒              ║               
                        ║                ▒▓▓▄ ▄██ ░▓█ ░██ ▒██   ██░▒▓▓▄ ▄██▒▓█  ▄▒██▄█▓▒ ▒              ║                     
                        ║                ▒ ▓███▀  ░▓█▒░██▓░ ████▓▒░▒ ▓███▀ ░▒████▒██▒ ░  ░              ║               
                        ║                ░ ░▒ ▒    ▒ ░░▒░▒░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░ ▒▓▒░ ░  ░              ║              
                        ║                  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░   ░  ▒   ░ ░  ░▒ ░                   ║
                        ║                ░         ░  ░░ ░░ ░ ░ ▒  ░          ░  ░░                     ║
                        ║                ░ ░       ░  ░  ░    ░ ░  ░ ░        ░                         ║
                        ║                                                                               ║
                        ║                       tg @asuspay    &    @openport8080                       ║
                        ╚═══════════════════════════════════════════════════════════════════════════════╝ 
         
    '''
    print(pystyle.Colors.blue + pidor + Fore.RESET)
def print_menu():
    print(" ")
    print(pystyle.Colors.blue +" ")
    print("                                          ╔══════════════════════════════════════════════╗          ")
    print("                                          ║                                              ║          ")
    print("                                          ║                      Меню:                   ║          ")
    print("                                          ║                1. Снос аккаунта              ║          ")
    print("                                          ║                2. Снос канала                ║          ")
    print("                                          ║                3. Снос ботов                 ║          ")
    print("                                          ║                                              ║          ")
    print("                                          ╚══════════════════════════════════════════════╝          ")
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())

        time.sleep(3)
        server.quit()
        return True
    except Exception:
        return False


def handle_complaint(senders, receivers):
    sent_emails = 0  
    pidor()

    print_menu()
    sleep(2)
    choice = input('''
                        root@userTP-LINK:~# ''')

    if choice == "1":
        os.system('cls')
        sleep(2)
        print(" ")
        print(" ")
        print("                                          ╔══════════════════════════════════════════════╗          ")
        print("                                          ║                                              ║          ")
        print("                                          ║                Выберите тип жалобы:          ║          ")
        print("                                          ║                1.1 Обычный                   ║          ")
        print("                                          ║                1.2 Снос сессий               ║          ")
        print("                                          ║                1.3 Снос троллей              ║          ")
        print("                                          ║                                              ║          ")
        print("                                          ╚══════════════════════════════════════════════╝          ")
        
        sleep(1)
        complaint_choice = input('''
                        root@userTP-LINK:~# ''')

        if complaint_choice == "1.1":
            os.system('cls')
            sleep(2)
            print(" ")
            print(" ")
            print("                        ╔══════════════════════════════════════════════════════════════════════════════════════╗          ")
            print("                        ║                                                                                      ║          ") 
            print("                        ║  Введите причину, юзернейм, telegram ID, затем ссылки на канал/чат и на нарушение    ║          ")
            print("                        ║                                                                                      ║          ")
            print("                        ╚══════════════════════════════════════════════════════════════════════════════════════╝          ") 
            sleep(2)
            reason = input('''
                        root@userTP-LINK:~# Причина:  ''')
            sleep(1)
            username = input('''
                        root@userTP-LINK:~# Юзернейм:  ''')
            sleep(1)
            telegram_ID = input('''
                        root@userTP-LINK:~# Telegram ID:  ''')
            sleep(1)
            chat_link = input('''
                        root@userTP-LINK:~# Ссылка на чат:  ''')
            sleep(1)
            violation_chat_link = input('''
                        root@userTP-LINK:~# Ссылка на нарушение:  ''')
            
            print(" ")
            print(" ")
            

            complaint_texts = {
                "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
            }

            

            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    complaint_text = complaint_texts[complaint_choice]
                   
                    complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(), telegram_ID=telegram_ID.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip())
                    send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram аккаунт", complaint_body)
                    print(f"Отправлено на {receiver_email} от {sender_email}!")
                    sent_emails += 1

            print(" ")
            print(" ")
           
            

        elif complaint_choice == "1.2":
            account_username = input("Юзернейм: ")
            Telegram_account_ID = input("Telegram ID: ")

            complaint_texts = {
                "1.2": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {account_username}, а мой айди, если злоумышленник поменял юзернейм — {Telegram_account_ID}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
            }

            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    complaint_text = complaint_texts[complaint_choice]
                    complaint_body = complaint_text.format(account_username=account_username.strip(), Telegram_account_ID=Telegram_account_ID.strip())
                    send_email(receiver_email, sender_email, sender_password, "Я утерял свой телеграм-аккаунт", complaint_body)
                    print(f"Отправлено на {receiver_email} от {sender_email}!")

            print(" ")
            print(" ")
            

        elif complaint_choice == "1.3":
            account_username = input("Юзернейм: ")
            chat_link = input("Введите ссылку на чат: ")
            chat_violation_link = input("введите ссылку на нарушение в чате: ")

            complaint_texts = {
                "1.3": "Hello! Dear Telegram support! want to report a user {username} the fact is that he insults people proofs: {chat_link} {chat_violation_link} !"
            }
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    complaint_text = complaint_texts[complaint_choice]
                    complaint_body = complaint_text.format(account_username=account_username.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip())
                    
                    send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram аккаунт", complaint_body)
                    print(f"Отправлено на {receiver_email} от {sender_email}!")
            
            
            print(" ")
            print(" ")
           

                            
    elif choice == "2":
        os.system('cls')
        sleep(2)
        print("                                          ╔══════════════════════════════════════════════╗          ")
        print("                                          ║                                              ║          ")
        print("                                          ║                Выберите тип жалобы:          ║          ")
        print("                                          ║                8. Личные данные              ║          ")
        print("                                          ║                9. Для прайсов                ║          ")
        print("                                          ║                10. Для геймов                ║          ")
        print("                                          ║                11. ЦП                        ║          ")
        print("                                          ║                12. Скам                      ║          ")
        print("                                          ║                13. Продажа вирт номеров      ║          ")
        print("                                          ║                14. Расчлененка               ║          ")
        print("                                          ║                15. Живодерство               ║          ")
        print("                                          ║                                              ║          ")
        print("                                          ╚══════════════════════════════════════════════╝          ")
        
        sleep(1)
        complaint_type = input('''
                        root@userTP-LINK:~# ''')

        complaint_types = {
            "8": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются личные данные невинных людей. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform"],
            "9": ["Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{violation_link} Просьба заблокировать данный канал.", "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel."],
            "10": ["Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance", "Здравствуйте, уважаемая поддержка Telegram! Пожалуйста, заблокируйте канал {channel_link}. В этом канале угрожают расстрелом детей в школах и совершением террористических актов, вы можете увидеть это здесь {violation_link}. Заранее спасибо."],
            "11": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуется порнография с несовершеннолетними детьми. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel"],
            "12": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются посты с целью обмана и мошенничества. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform."],
            "13": ["Здравствуйте, поддержка telegram. Я бы хотел пожаловаться на телеграм канал продающий виртуальные номера, насколько я знаю это запрещено правилами вашей площадки. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link} . Спасибо что очищаете свою площадку от подобных каналов!", "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!"],
            "14": ["Доброго времени суток, уважаемая поддержка. На просторах вашей платформы мне попался канал, распространяющий шок контент с убийствами людей. Ссылка на канал - {channel_link} , ссылка на нарушение - {violation_link} . Просьба удалить данный канал, спасибо за внимание.", "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention."],
            "15": ["Здравствуйте, уважаемая поддержка. На вашей платформе я нашел канал который выкладывает жестокое обращение с животными. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link}. Спасибо за то что делаете телеграм чище.", "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you"],

        }

        if complaint_type not in complaint_types:
            print("                             Некорректный выбор.")
        else:
            complaint_texts = complaint_types[complaint_type]
            sleep(1)
            channel_link = input('''
                        root@userTP-LINK:~# Ссылка на канал:  ''')
            sleep(1)
            violation_link = input('''
                        root@userTP-LINK:~# Ссылка на нарушение:  ''') 

            for sender_email, sender_password in senders.items():
                for receiver_email in random.sample(receivers, min(2, len(receivers))):
                    complaint_body = complaint_texts[0].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                    send_email(receiver_email, sender_email, sender_password, "Жалоба на канал в Telegram", complaint_body)
                    print(f"Отправлено на {receiver_email}!")
                    sent_emails += 1

            print(" ")
            print(" ")
           

            if len(complaint_texts) > 1:
                for sender_email, sender_password in senders.items():
                    for receiver_email in random.sample(receivers, min(2, len(receivers))):
                        complaint_body = complaint_texts[1].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                        send_email(receiver_email, sender_email, sender_password, "Complaint about a channel in Telegram", complaint_body)
                        print(f"Sent to {receiver_email}!")
                        sent_emails += 1
        print("Отправлено!")
        print(" ")
        print(" ")
       

    elif choice == "3":
        os.system('cls')
        sleep(2)
        print(" ")
        print(" ")
        print("                                          ╔══════════════════════════════════════════════╗          ")
        print("                                          ║                                              ║          ")
        print("                                          ║             3.1 Гб                           ║          ")
        print("                                          ║             3.2 Прайсы в ботах (БЕТА)        ║          ")
        print("                                          ║             3.3 Любой бот для докса          ║          ")
        print("                                          ║                                              ║          ")
        print("                                          ╚══════════════════════════════════════════════╝          ")

        sleep(1)
        complaint_type = input('''
                        root@userTP-LINK:~# ''')

    complaint_types = {
        "3.1": "Здравствуйте, уважаемая поддержка телеграм. В вашей сети я нашел бота, который предоставляет запрещенные услуги, такие как доксинг (поиск информации). Ссылка на бота - {bot_link}. Просьба удалить данного бота с вашей платформы.",
        "3.2": "Здравствуйте, уважаемая поддержка. На просторах телеграм я заметил бота, который предоставляет покупку услуг доксинга и сваттинга. Ссылка на бота - {bot_link}. Просьба заблокировать данного бота.",
        "3.3": "Здравствуйте, уважаемая поддержка телеграм. В вашей сети я нашел бота, который предоставляет запрещенные услуги, такие как доксинг (поиск информации). Ссылка на бота - {bot_link}. Просьба удалить данного бота с вашей платформы."
    }

    if complaint_type not in complaint_types:
        print("                             Некорректный выбор.")
    else:
        complaint_texts = complaint_types[complaint_type]
        sleep(1)
        bot_username = input('''
                        root@userTP-LINK:~# Юзернейм бота: ''')
        for sender_email, sender_password in senders.items():
            for receiver_email in random.sample(receivers, min(2, len(receivers))):
                complaint_body = complaint_texts.format(bot_link=bot_username.strip())
                send_email(receiver_email, sender_email, sender_password, "Жалоба на бота в Telegram", complaint_body)
                print(f"Отправлено на {receiver_email}!")
                sent_emails += 1

            print(" ")
            print(" ")
            print("                                                         КОНОСЛЬ ЗАКРОЕТСЯ ЧЕРЕЗ 5 СЕКУНД")
            sleep(5)        

if __name__ == "__main__":
    handle_complaint(senders, receivers)
    
