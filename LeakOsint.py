import requests #line:2
import colorama #line:3
import faker #line:4
from faker import Faker #line:5
import os #line:6
import sys #line:7
import socket #line:8
from pystyle import *#line:9
import pystyle #line:10
import time #line:11
from time import sleep #line:12
from colorama import Fore ,init ,Style #line:13
def idi (OOOOO0O000OOOO0OO ):#line:15
    global last_search_time #line:16
    try :#line:17
        Write .Print (f"\n[INFO] Запрос: {OOOOO0O000OOOO0OO}",interval =0.0001 )#line:18
        O000O00OOO00O00OO =time .time ()#line:19
        if O000O00OOO00O00OO -last_search_time <60 :#line:20
            Write .Print ("\n[!] Подождите минуту перед следующим запросом\n",Colors .blue_to_cyan ,interval =0.0001 )#line:21
            return #line:22
        OO00O00O000O0OOOO ="https://server.leakosint.com/"#line:24
        OOO00O00O0OO0OO0O ={"Content-Type":"application/json"}#line:27
        OO0OOO00O000O0O0O ={"token":"6607575831:mrjoz662","request":OOOOO0O000OOOO0OO ,"limit":100 ,"lang":"ru"}#line:33
        O000O000OO000OO0O =requests .post (OO00O00O000O0OOOO ,json =OO0OOO00O000O0O0O ,headers =OOO00O00O0OO0OO0O )#line:35
        if O000O000OO000OO0O .status_code !=200 :#line:37
            Write .Print (f"\n[ERROR] Ошибка HTTP {O000O000OO000OO0O.status_code}: {O000O000OO000OO0O.reason}\n",Colors .blue_to_cyan ,interval =0.0001 )#line:39
            return #line:40
        O0OOOO0OOO00000OO =O000O000OO000OO0O .json ().get ('List',{})#line:41
        if not O0OOOO0OOO00000OO :#line:43
            Write .Print ("\n[SORRY] Ничего не найдено\n",Colors .blue_to_cyan ,interval =0.0001 )#line:44
            return #line:45
        for OOOOO00O0OO00O000 ,O000OOO0OOOO0O0OO in O0OOOO0OOO00000OO .items ():#line:47
            if "No results found"in OOOOO00O0OO00O000 :#line:48
                Write .Print ("\n[SORRY] Ничего не найдено\n",Colors .blue_to_cyan ,interval =0.0001 )#line:49
                break #line:50
            Write .Print ("\n[DB] База данных -!> ",Colors .blue_to_cyan ,interval =0.0001 )#line:52
            Write .Print (OOOOO00O0OO00O000 ,Colors .white ,interval =0.0001 )#line:53
            Write .Print ("\n\n[#] Описание -!> ",Colors .blue_to_cyan ,interval =0.0001 )#line:54
            Write .Print (f"{O000OOO0OOOO0O0OO['InfoLeak']}\n",Colors .blue_to_cyan ,interval =0.0001 )#line:55
            for OO00OO00O0O000O00 in O000OOO0OOOO0O0OO ['Data']:#line:57
                for OOO0OO00OOO0OOOOO ,OOOO0O0O0OO0000OO in OO00OO00O0O000O00 .items ():#line:58
                    Write .Print (f"\n[S] {OOO0OO00OOO0OOOOO} -!> ",Colors .blue_to_cyan ,interval =0.0001 )#line:59
                    Write .Print (OOOO0O0O0OO0000OO ,Colors .white ,interval =0.0001 )#line:60
            print ()#line:61
        last_search_time =O000O00OOO00O00OO #line:63
    except Exception as OO00000OO0OOO0OO0 :#line:64
        Write .Print (f"\n[ERROR] Произошла ошибка: {OO00000OO0OOO0OO0}\n",Colors .blue_to_cyan ,interval =0.0001 )#line:65
def ip_lookup (OOOOO0O0O000000O0 ):#line:67
    O00OO00O0000OO000 =f"http://ip-api.com/json/{OOOOO0O0O000000O0}"#line:68
    try :#line:69
        O000OO0O0OO0O0OO0 =requests .get (O00OO00O0000OO000 )#line:70
        O00OO0OOO000O0OO0 =O000OO0O0OO0O0OO0 .json ()#line:71
        if O00OO0OOO000O0OO0 .get ("status")=="fail":#line:72
            Write .Print (f"[!] Произошла ошибка: {O00OO0OOO000O0OO0['message']}\n",Colors .red ,interval =0.0005 )#line:73
        else :#line:74
            O0O0OOOO0000OOOOO =""#line:75
            for OO00OOO0O000OO0O0 ,O0O0OO000OOO0OOO0 in O00OO0OOO000O0OO0 .items ():#line:76
                O0O0OOOO0000OOOOO +=f"[+] {OO00OOO0O000OO0O0}: {O0O0OO000OOO0OOO0}\n"#line:77
            Write .Print (O0O0OOOO0000OOOOO ,Colors .blue_to_cyan ,interval =0.005 )#line:78
    except Exception as OOO00OOO000O00OOO :#line:79
        Write .Print (f"[!] Произошла ошибка: {str(OOO00OOO000O00OOO)}\n",Colors .blue_to_cyan ,interval =0.0005 )#line:80
def warning ():#line:82
    Write .Print ("""Автор не несет ответственности за ваши действия. Вся информация взята с открытых источников и несет исключительно ознакомительный характер. 

Автор не несет цели кого то оскорбить или унизить! Все, что покажется запрещенным является недействительным! 
           
Вся информация в Сервисе предоставляется «как есть», без каких-либо гарантий полноты, точности, своевременности или результатов, полученных от использования этой информации, 

а также без каких-либо гарантий, явных или подразумеваемых, включая, помимо прочего, гарантии производительности, товарного состояния и пригодности для определенной цели.

Автор не будет нести ответственности перед Вами или кем-либо еще за любое решение или действие, предпринятое на основании информации, 

предоставленной Сервисом, или за любой косвенный, особый или аналогичный ущерб, даже если было сообщено о возможности такого ущерба.           
   
Вся информация предоставляется в исходном виде, без гарантий полноты или своевременности, и без иных явно выраженных или подразумеваемых гарантий. 

Доступ к Сервису, а также использование его Содержимого осуществляются исключительно по вашему усмотрению и на ваш риск.

Так же хочу прояснить, не возлагайте на что то большие надежды и не думайте что что то новое будет обязательно крутым,

Я хочу сказать, что если софт "не оправдает ваши ожидания" то ко мне (и другому овнеру) претензий не должно быть, вы сами себе накрутили

то, что софт будет крутым, отчитываться и тем более возвращать я (и другой овнер) вам ничего не буду (не будет)! 

16+                                                
 
Используя данный софт, вы тем самым соглашаетесь с нашим отказом от ответственности а так же на его условия.""",Colors .blue_to_cyan ,interval =0.005 )#line:107
banner2 =f''' 

██╗     ███████╗ █████╗ ██╗  ██╗     ██████╗ ███████╗██╗███╗   ██╗████████╗
██║     ██╔════╝██╔══██╗██║ ██╔╝    ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║     █████╗  ███████║█████╔╝     ██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║     ██╔══╝  ██╔══██║██╔═██╗     ██║   ██║╚════██║██║██║╚██╗██║   ██║   
███████╗███████╗██║  ██║██║  ██╗    ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝  '''#line:116
menu ="""
                            MAIN MANU   
[1]Поиск по почте                           [6]Поиск по ФИО
[2]Поиск по юзернейм                        [7]Поиск по ВК
[3]Поиск по телефону                        [8]Поиск по МАС-адресу
[4]Поиск по IP                              [9]Выход из программы
[5]Поиск по паролю                          [10]Дисклеймер

"""#line:125
def main ():#line:128
 O0OO0OO0OO0000O0O =['token']#line:129
while True :#line:132
        print (Colorate .Horizontal (Colors .blue_to_cyan ,Center .XCenter (banner2 )))#line:134
        print (Colorate .Horizontal (Colors .blue_to_cyan ,Center .XCenter (menu )))#line:135
        choice =Write .Input (f"root@userTP-LINK:~# Выберите пункт: ",Colors .blue_to_cyan ,interval =0.05 )#line:137
        if choice .isdigit ()and 1 <=int (choice )<=12 :#line:139
            choice =int (choice )#line:140
            if choice ==1 :#line:141
                 nahui =Write .Input ("Введите почту: ",Colors .blue_to_cyan ,interval =0.0005 )#line:142
                 idi ()#line:143
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:144
            elif choice ==2 :#line:145
                 req =Write .Input ("Введите юзернейм: ",Colors .blue_to_cyan ,interval =0.0005 )#line:146
                 idi ()#line:147
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:148
            elif choice ==3 :#line:149
                 req =Write .Input ("Введите номер: ",Colors .blue_to_cyan ,interval =0.0005 )#line:150
                 idi ()#line:151
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:152
            elif choice ==4 :#line:153
                ip =input ("Введите IP-адрес: ")#line:154
                ip_lookup (ip )#line:155
                input (f"\n Нажмите Enter для возврата в меню >> ")#line:156
            elif choice ==5 :#line:158
                 req =Write .Input ("Введите пароль: ",Colors .blue_to_cyan ,interval =0.0005 )#line:159
                 idi ()#line:160
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:161
            elif choice ==6 :#line:162
                 req =Write .Input ("Введите ФИО: ",Colors .blue_to_cyan ,interval =0.0005 )#line:163
                 idi ()#line:164
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:165
            elif choice ==7 :#line:166
                  req =Write .Input ("Введите ВК айди: ",Colors .blue_to_cyan ,interval =0.0005 )#line:167
                  idi ()#line:168
                  input (f"\n Нажмите Enter для возврата в меню >> ")#line:169
            elif choice ==8 :#line:170
                 req =Write .Input ("Введите MAC-адрес: ",Colors .blue_to_cyan ,interval =0.0005 )#line:171
                 idi ()#line:172
                 input (f"\n Нажмите Enter для возврата в меню >> ")#line:173
            elif choice ==9 :#line:175
                print ("Выход...",pystyle .Colors .red )#line:176
                break #line:177
            elif choice ==10 :#line:179
                sleep (3 )#line:180
                warning ()#line:181
        else :#line:184
             print (f"Неверный выбор, попробуйте снова.",pystyle .Colors .red )#line:185
             input (f"\nНажмите Enter для возврата в меню >> ",pystyle .Colors .red )#line:186
if __name__ =="__main__":#line:188
    main ()