# -*- coding: utf-8 -*-

#########################################
# Author: LATVER                        #
# Bot_v2.0: главное окно хелппера       #
#########################################

#TODO: 

#Библотеки
from tkinter import *
from tkinter import Entry, END, messagebox, Tk, Button, filedialog, Label, BooleanVar
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox, Scrollbar
import os, time, keyboard, requests, pyautogui, threading, sys, re, subprocess, random, webbrowser, datetime, PyPDF2, docx, psutil, getpass, builtins, speedtest, pdf2docx, ctypes, sys, win32api, pickle, tempfile
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO
from urllib.parse import urlparse, quote

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()
else:
    #Путь до файлов
    current_dir = os.getcwd()
    file_name = "Бот-помощник.exe"
    PATH = os.path.abspath(os.path.join(current_dir, file_name))

    def delete_symbols():
        enter.delete(0, END)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция питания ПК
    class menu_power_pc:
        # Выход из "Питание ПК"
        def exit_menu():
            try:
                window.deiconify()
                window_power_pc.destroy()
                window_power_pc.quit()
            except NameError:
                window.deiconify()
                window_power_pc.destroy()
                window_power_pc.quit()
            except TclError:
                window.deiconify()
                window_power_pc.destroy()
                window_power_pc.quit()

        #Калькулятор секунд
        def Calc_sec():
            try:
                window_power_pc.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()
                window_power_pc.destroy()
                window_power_pc.quit()

            timer = '0'
            global win_calc_sec
            #Выключение
            def shutdown():
                timing = result()
                subprocess.call([f'shutdown /s /t {timing} /f'])
            #Перезагрузка
            def reboot():
                timing = result()
                subprocess.call([f'shutdown /r /t {timing} /f'])
            #Сон
            def hyber_pc():
                timing = result()
                subprocess.call([f'timeout /t {timing} && rundll32.exe powrprof.dll,SetSuspendState 0,1,0'])
            #Отмена неизбежного выключения
            def cancel():
                subprocess.call(['shutdown -a'])
                time_1.configure(text = f'Отмена неизбежного выключения', font = ('Verdana', 10, 'bold'), bg = '#d3d3d3', fg = 'black')

            def enter_result(Return):
                result()

            def result():
                h1 = hours1.get()
                m1 = minutes1.get()
                s1 = seconds1.get()

                if re.search('-', h1):
                    time_1.configure(text='Ошибка: Отрицательное значение в часах', style='Custom.TButton')
                elif re.search('-', m1):
                    time_1.configure(text='Ошибка: Отрицательное значение в минутах', style='Custom.TButton')
                elif re.search('-', s1):
                    time_1.configure(text='Ошибка: Отрицательное значение в секундах', style='Custom.TButton')
                elif h1 == '':
                    time_1.configure(text='Ошибка: Пустое значение в часах', style='Custom.TButton')
                elif m1 == '':
                    time_1.configure(text='Ошибка: Пустое значение в минутах', style='Custom.TButton')
                elif s1 == '':
                    time_1.configure(text='Ошибка: Пустое значение в секундах', style='Custom.TButton')
                else:
                    hours_in_seconds1 = int(h1) * 60
                    hours_in_seconds2 = hours_in_seconds1 * 60
                    minutes_in_seconds = int(m1) * 60
                    final = hours_in_seconds2 + minutes_in_seconds + int(s1)
                    timer = final
                    time_1.configure(text=f'Результат: {timer} секунд', style='Custom.TButton')
                    return timer

            #Назад в Power_PC
            def exit_menu():
                try:
                    window_power_pc.deiconify()
                    win_calc_sec.destroy()
                    win_calc_sec.quit()
                except NameError:
                    window.deiconify()
                    win_calc_sec.destroy()
                    win_calc_sec.quit()
                except TclError:
                    window.deiconify()
                    win_calc_sec.destroy()
                    win_calc_sec.quit()
                
            win_calc_sec = Tk()
            win_calc_sec.title('Калькулятор времени')
            win_calc_sec.resizable(width=False, height=False)
            win_calc_sec.bind('<Return>', enter_result)
            win_calc_sec.protocol('WM_DELETE_WINDOW', exit_menu)

            # получаем размер экрана
            screen_width = win_calc_sec.winfo_screenwidth()
            screen_height = win_calc_sec.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            win_calc_sec.geometry(f"600x300+{center_x-400}+{center_y-300}")

            style_calc_sec_win = ttk.Style(win_calc_sec)
            style_calc_sec_win.theme_use('vista')
            style_calc_sec_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")
            style_calc_sec_win.configure("Entry.TButton", background="#4CAF50", foreground="black", font="Arial 12 bold")

            #Строки | Время
            hours1 = ttk.Entry(win_calc_sec, width = 5, style='Entry.TButton', font=('Arial 15'), justify='center')
            hours1.insert(0, '0')
            hours1.grid(row = 2, column = 0)

            minutes1 = ttk.Entry(win_calc_sec, width = 5, style='Entry.TButton', font=('Arial 15'), justify='center')
            minutes1.insert(0, '0')
            minutes1.grid(row = 2, column = 1)

            seconds1 = ttk.Entry(win_calc_sec, width = 5, style='Entry.TButton', font=('Arial 15'), justify='center')
            seconds1.insert(0, '0')
            seconds1.grid(row = 2, column = 2)

            #Текста обозначений
            hours = ttk.Label(win_calc_sec, style='Entry.TButton')
            hours.grid(row = 0, column = 0, stick = 'wens')
            hours.configure(text = 'Часы')

            minutes = ttk.Label(win_calc_sec, style='Entry.TButton')
            minutes.grid(row = 0, column = 1, stick = 'wens')
            minutes.configure(text = 'Минуты')

            seconds = ttk.Label(win_calc_sec, style='Entry.TButton')
            seconds.grid(row = 0, column = 2, stick = 'wens')
            seconds.configure(text = 'Секунды')

            #Кнопки
            button1 = ttk.Button(win_calc_sec, text = 'Рассчитать', width = 10, command = result, style='Custom.TButton')
            button1.grid(column = 0, row = 4, columnspan = 4, stick = 'wens')
            button2 = ttk.Button(win_calc_sec, text = 'Выключить ПК', width = 20, command = shutdown, style='Custom.TButton')
            button2.grid(column = 0, row = 5, stick = 'wens')
            button3 = ttk.Button(win_calc_sec, text = 'Перезагрузить ПК', width = 20, command = reboot, style='Custom.TButton')
            button3.grid(column = 1, row = 5, stick = 'wens')
            button5 = ttk.Button(win_calc_sec, text = 'Режим сна ПК', width = 20, command = hyber_pc, style='Custom.TButton')
            button5.grid(column = 2, row = 5, stick = 'wens')
            button6 = ttk.Button(win_calc_sec, text = 'Отмена неизбежного выключения', width = 10, command = cancel, style='Custom.TButton')
            button6.grid(column = 0, row = 6, columnspan = 4, stick = 'wens')

            #Результат
            time_1 = ttk.Label(win_calc_sec, style='Custom.TButton')
            time_1.grid(row = 8, column = 0, columnspan = 4, stick = 'wens')

            #Размеры по вертикали и горизонтали
            win_calc_sec.columnconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            win_calc_sec.rowconfigure([0, 1, 2, 3, 4, 5], weight = 1, minsize = 0)

            win_calc_sec.mainloop()

        #Шаблоны
        def templates():
            def exit_menu_5():
                try:
                    win.deiconify()
                    temp_win.destroy()
                    temp_win.quit()
                except NameError:
                    window.deiconify()
                    temp_win.destroy()
                    temp_win.quit()
                except TclError:
                    window.deiconify()
                    temp_win.destroy()
                    temp_win.quit()
            try:
                win.withdraw()
            except NameError:
                pass
            except TclError:
                pass

            temp_win = Tk()
            temp_win.title('Шаблоны')
            temp_win.resizable(width=False, height=False)
            temp_win.columnconfigure([0], weight = 1, minsize = 150)
            temp_win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            temp_win.protocol('WM_DELETE_WINDOW', exit_menu_5)

            # получаем размер экрана
            screen_width = temp_win.winfo_screenwidth()
            screen_height = temp_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            temp_win.geometry(f"300x160+{center_x-230}+{center_y-300}")

            style_temp_win = ttk.Style(temp_win)
            style_temp_win.theme_use('vista')
            style_temp_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button7 = ttk.Button(temp_win, text = 'Выключить ПК через 30 минут', width = 30, command = menu_power_pc.Power_off2, style='Custom.TButton')
            button7.grid(column = 0, row = 0, stick = 'wens')
            button8 = ttk.Button(temp_win, text = 'Выключить ПК через 1 час', width = 30, command = menu_power_pc.Power_off3, style='Custom.TButton')
            button8.grid(column = 0, row = 1, stick = 'wens')
            button9 = ttk.Button(temp_win, text = 'Выключить ПК через 1.5 часа', width = 30, command = menu_power_pc.Power_off4, style='Custom.TButton')
            button9.grid(column = 0, row = 2, stick = 'wens')
            button10 = ttk.Button(temp_win, text = 'Выключить ПК через 2 часа', width = 30, command = menu_power_pc.Power_off5, style='Custom.TButton')
            button10.grid(column = 0, row = 3, stick = 'wens')

            temp_win.mainloop()

        #Выключение
        def Power_off1():
            os.system('shutdown /s /t 1 /f')

        def Power_off2():
            os.system('shutdown /s /t 1800 /f')

        def Power_off3():
            os.system('shutdown /s /t 3600 /f')

        def Power_off4():
            os.system('shutdown /s /t 5400 /f')

        def Power_off5():
            os.system('shutdown /s /t 7200 /f')

        #Перезагрузка
        def Reboot1():
            os.system('shutdown /r /t 1 /f')

        def Reboot2():
            os.system('shutdown /r /t 1800 /f')

        def Reboot3():
            os.system('shutdown /r /t 3600 /f')

        def Reboot4():
            os.system('shutdown /r /t 5400 /f')

        def Reboot5():
            os.system('shutdown /r /t 7200 /f')

        #Отмена неизбежного действия
        def stop():
            os.system('shutdown /a')

        #Выключение ПК
        def Power_off():
            global win
            def exit_menu_4():
                try:
                    window_power_pc.deiconify()
                    win.destroy()
                    win.quit()
                except NameError:
                    window.deiconify()
                    win.destroy()
                    win.quit()
                except TclError:
                    window.deiconify()
                    win.destroy()
                    win.quit()

            try:
                window_power_pc.withdraw()
            except NameError:
                pass
            except TclError:
                pass

            win = Tk()
            win.title('Выключение ПК')
            win.resizable(width=False, height=False)
            win.columnconfigure([0], weight = 1, minsize = 150)
            win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            win.protocol('WM_DELETE_WINDOW', exit_menu_4)

            # получаем размер экрана
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            win.geometry(f"310x140+{center_x-230}+{center_y-300}")

            style_temp_win = ttk.Style(win)
            style_temp_win.theme_use('vista')
            style_temp_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button6 = ttk.Button(win, text = 'Выключить ПК', width = 32, command = menu_power_pc.Reboot1, style='Custom.TButton')
            button6.grid(column = 0, row = 0, stick = 'wens')
            button14 = ttk.Button(win, text = 'Шаблоны', width = 32, command = menu_power_pc.templates, style='Custom.TButton')
            button14.grid(column = 0, row = 1, stick = 'wens')
            button9 = ttk.Button(win, text = 'Отмена неизбежного выключения', width = 32, command = menu_power_pc.stop, style='Custom.TButton')
            button9.grid(column = 0, row = 2, stick = 'wens')

            win.mainloop()

        #Перезагрузка ПК
        def Reboot():
            global win
            def templates2():
                def exit_menu_3():
                    try:
                        win.deiconify()
                        temp_win.destroy()
                        temp_win.quit()
                    except NameError:
                        window.deiconify()
                        temp_win.destroy()
                        temp_win.quit()
                    except TclError:
                        window.deiconify()
                        temp_win.destroy()
                        temp_win.quit()

                try:
                    win.withdraw()
                except NameError:
                    pass
                except TclError:
                    window.deiconify()

                temp_win = Tk()
                temp_win.title('Шаблоны')
                temp_win.resizable(width=False, height=False)
                temp_win.columnconfigure([0], weight = 1, minsize = 150)
                temp_win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
                temp_win.protocol('WM_DELETE_WINDOW', exit_menu_3)

                # получаем размер экрана
                screen_width = temp_win.winfo_screenwidth()
                screen_height = temp_win.winfo_screenheight()

                # вычисляем координаты центра экрана
                center_x = int(screen_width / 2)
                center_y = int(screen_height / 2)

                temp_win.geometry(f"300x160+{center_x-230}+{center_y-300}")

                style_menu_reboot_win = ttk.Style(temp_win)
                style_menu_reboot_win.theme_use('vista')
                style_menu_reboot_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

                button7 = ttk.Button(temp_win, text = 'Перезагрузить ПК через 30 минут', width = 30, command = menu_power_pc.Reboot2, style='Custom.TButton')
                button7.grid(column = 0, row = 0, stick = 'wens')
                button8 = ttk.Button(temp_win, text = 'Перезагрузить ПК через 1 час', width = 30, command = menu_power_pc.Reboot3, style='Custom.TButton')
                button8.grid(column = 0, row = 1, stick = 'wens')
                button9 = ttk.Button(temp_win, text = 'Перезагрузить ПК через 1.5 часа', width = 30, command = menu_power_pc.Reboot4, style='Custom.TButton')
                button9.grid(column = 0, row = 2, stick = 'wens')
                button10 = ttk.Button(temp_win, text = 'Перезагрузить ПК через 2 часа', width = 30, command = menu_power_pc.Reboot5, style='Custom.TButton')
                button10.grid(column = 0, row = 3, stick = 'wens')

                temp_win.mainloop()

            def exit_menu_2():
                try:
                    window_power_pc.deiconify()
                    win.destroy()
                    win.quit()
                except NameError:
                    window.deiconify()
                    win.destroy()
                    win.quit()
                except TclError:
                    window.deiconify()
                    win.destroy()
                    win.quit()

            try:
                window_power_pc.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            win = Tk()
            win.title('Перезагрузка ПК')
            win.resizable(width=False, height=False)
            win.columnconfigure([0], weight = 1, minsize = 150)
            win.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 0)
            win.protocol('WM_DELETE_WINDOW', exit_menu_2)

            # получаем размер экрана
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            win.geometry(f"300x120+{center_x-230}+{center_y-300}")

            style_reboot_win = ttk.Style(win)
            style_reboot_win.theme_use('vista')
            style_reboot_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button6 = ttk.Button(win, text = 'Перезагрузить ПК', width = 32, command = menu_power_pc.Reboot1, style='Custom.TButton')
            button6.grid(column = 0, row = 0, stick = 'wens')
            button14 = ttk.Button(win, text = 'Шаблоны', width = 32, command = templates2, style='Custom.TButton')
            button14.grid(column = 0, row = 1, stick = 'wens')
            button9 = ttk.Button(win, text = 'Отмена неизбежной перезагрузки', width = 32, command = menu_power_pc.stop, style='Custom.TButton')
            button9.grid(column = 0, row = 2, stick = 'wens')

            win.mainloop()

        #Режим сна ПК
        def Sleep():
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        #Выход из учетной записи
        def Exit():
            os.system('logoff')
            os.system('shutdown /l')

        def menu_pc():
            global window_power_pc
            try:
                window.withdraw()
            except NameError:
                window.deiconify()
            except TclError:
                window.deiconify()

            window_power_pc = Tk()
            window_power_pc.title('Питание ПК')
            window_power_pc.resizable(width=False, height=False)
            window_power_pc.columnconfigure([0], weight = 1, minsize = 150)
            window_power_pc.rowconfigure([0, 1, 2, 3, 4], weight = 1, minsize = 0)
            window_power_pc.protocol('WM_DELETE_WINDOW', menu_power_pc.exit_menu)

            # получаем размер экрана
            screen_width = window_power_pc.winfo_screenwidth()
            screen_height = window_power_pc.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            window_power_pc.geometry(f"250x200+{center_x-230}+{center_y-300}")

            style_power_pc_win = ttk.Style(window_power_pc)
            style_power_pc_win.theme_use('vista')
            style_power_pc_win.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button1 = ttk.Button(window_power_pc, text = 'Меню выключения ПК', width = 25, command = menu_power_pc.Power_off, style='Custom.TButton')
            button1.grid(column = 0, row = 0, stick = 'wens')
            button2 = ttk.Button(window_power_pc, text = 'Меню перезагрузки ПК', width = 25, command = menu_power_pc.Reboot, style='Custom.TButton')
            button2.grid(column = 0, row = 1, stick = 'wens')
            button3 = ttk.Button(window_power_pc, text = 'Гибернация ПК', width = 25, command = menu_power_pc.Sleep, style='Custom.TButton')
            button3.grid(column = 0, row = 2, stick = 'wens')
            button4 = ttk.Button(window_power_pc, text = 'Выход из системы ПК', width = 25, command = menu_power_pc.Exit, style='Custom.TButton')
            button4.grid(column = 0, row = 3, stick = 'wens')
            button5 = ttk.Button(window_power_pc, text = 'Задать время', width = 25, command = menu_power_pc.Calc_sec, style='Custom.TButton')
            button5.grid(column = 0, row = 4, stick = 'wens')

            window.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция браузера
    class func_browser:
        global win
        def vk():
            def news():
                webbrowser.open('https://vk.com/feed')
            def messages():
                webbrowser.open('https://vk.com/im')
            def my_page():
                webbrowser.open('https://vk.com/id0')

            def exit_back_browser_3():
                try:
                    top.destroy()
                    win.deiconify()
                    top.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()

            try:
                win.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            top = Tk()
            top.title('VK')
            top.resizable(width=False, height=False)
            top.columnconfigure([0], weight = 1, minsize = 60)
            top.rowconfigure([0, 1, 2], weight = 1, minsize = 50)
            top.protocol('WM_DELETE_WINDOW', exit_back_browser_3)

            # получаем размер экрана
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            top.geometry(f"200x160+{center_x-230}+{center_y-300}")

            style_vk = ttk.Style(top)
            style_vk.theme_use('vista')
            # Определяем цвета для кнопок
            style_vk.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            topbut1 = ttk.Button(top, text='Новости', command=news, style='Custom.TButton')
            topbut1.grid(column=0, row=0, stick='wens')

            topbut2 = ttk.Button(top, text='Сообщения', command=messages, style='Custom.TButton')
            topbut2.grid(column=0, row=1, stick='wens')

            topbut3 = ttk.Button(top, text='Моя страница', command=my_page, style='Custom.TButton')
            topbut3.grid(column=0, row=2, stick='wens')

            top.mainloop()

        def youtube():
            webbrowser.open('https://youtube.com')
        def vk_and_youtube():
            webbrowser.open('https://youtube.com')
            webbrowser.open('https://vk.com/id0')
        def google_translate():
            webbrowser.open('https://translate.yandex.ru')
        def google_disk():
            webbrowser.open('https://drive.google.com/drive')
        def gmail():
            webbrowser.open('https://gmail.com')

        #Менеджер сайтов
        def read_site_com():
            read = open('C:\\Users\\' + os.environ['USERNAME'] + '\\Desktop\\Sites.txt', 'r')

        def save_site_com():
            site = adress.get().strip()
            if not site:
                return
            with open('C:\\Users\\' + os.environ['USERNAME'] + '\\Desktop\\Sites.txt', 'r') as f:
                sites = f.read()
            if site in sites:
                messagebox.showwarning("Предупреждение", "Сайт уже добавлен в список", parent=window_browser)
                return
            with open('C:\\Users\\' + os.environ['USERNAME'] + '\\Desktop\\Sites.txt', 'a') as f:
                f.write(site + '\n')
            messagebox.showinfo("Добавление", "Сайт добавлен в список", parent=window_browser)

        def sites_open():
            def clear_button():
                site_listbox.delete(0, tk.END)

            def add_site():
                site = site_entry.get().strip()
                if site:
                    # получаем все значения из списка
                    sites = site_listbox.get(0, tk.END)
                    # проверяем наличие сайта в списке
                    if site in sites:
                        messagebox.showwarning("Предупреждение", "Этот сайт уже есть в списке!", parent=window_browser)
                    else:
                        # добавляем сайт в список
                        site_listbox.insert(tk.END, site)
                        site_entry.delete(0, tk.END)

            def delete_site():
                selection = site_listbox.curselection()
                if selection:
                    site_listbox.delete(selection)

            def save_sites():
                filename = filename_entry.get().strip()
                if filename:
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    with open(filename, 'w') as f:
                        for site in site_listbox.get(0, tk.END):
                            f.write(site + '\n')
                    filename_entry.delete(0, tk.END)
                    messagebox.showinfo("Сохранение", "Список сайтов сохранен", parent=window_browser)
                else:
                    messagebox.showerror("Ошибка", "Введите имя файла для сохранения", parent=window_browser)

            def load_sites():
                filename = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"),))
                if filename:
                    with open(filename, 'r') as f:
                        site_listbox.delete(0, tk.END)
                        for line in f:
                            site = line.strip()
                            if site:
                                site_listbox.insert(tk.END, site)
                    messagebox.showinfo("Загрузка", "Список сайтов загружен", parent=window_browser)
                else:
                    messagebox.showwarning("Предупреждение", "Не выбран файл для загрузки", parent=window_browser)

            def open_selected_site(event):
                selection = site_listbox.curselection()
                site = site_listbox.get(selection)
                webbrowser.open(site)

            directory = r'C:\Users\{}\Desktop\sites'.format(os.environ["USERNAME"])  # Абсолютный путь к директории

            def exit_back_browser_2():
                try:
                    win.deiconify()
                    window_browser.destroy()
                    window_browser.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()

            try:
                win.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            window_browser = Tk()
            window_browser.title("Менеджер сайтов")
            window_browser.geometry("420x660")
            window_browser.resizable(width=False, height=False)
            window_browser.protocol('WM_DELETE_WINDOW', exit_back_browser_2)

            # получаем размер экрана
            screen_width = window_browser.winfo_screenwidth()
            screen_height = window_browser.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            window_browser.geometry(f"500x700+{center_x-300}+{center_y-300}")

            style_manager_sites = ttk.Style(window_browser)
            style_manager_sites.theme_use('vista')
            style_manager_sites.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")
            style_manager_sites.configure("Custom.TEntry", background="#4CAF50", foreground="black")

            # Создаем основной фрейм
            main_frame = tk.Frame(window_browser)
            main_frame.pack(fill=tk.BOTH, expand=1)

            # Создаем фрейм для ввода нового сайта
            add_frame = tk.LabelFrame(main_frame, text="Добавить сайт", padx=10, pady=10)
            add_frame.pack(padx=10, pady=10)

            site_entry = ttk.Entry(add_frame, style='Custom.TEntry', font=('Arial', 14), justify='center')
            site_entry.pack(side=tk.LEFT, padx=5)

            add_button = ttk.Button(add_frame, text="Добавить", command=add_site, style='Custom.TButton')
            add_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для списка сохраненных сайтов
            list_frame = tk.LabelFrame(main_frame, text="Список сайтов", padx=10, pady=10)
            list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)

            site_listbox = tk.Listbox(list_frame, width=40, font=('Arial', 12))
            site_listbox.pack(fill=tk.BOTH, expand=1)
            site_listbox.bind('<Double-Button-1>', open_selected_site)

            # Создаем фрейм для кнопок управления списком сайтов
            button_frame = tk.Frame(list_frame)
            button_frame.pack(pady=5)

            delete_button = ttk.Button(button_frame, text="Удалить", command=delete_site, style='Custom.TButton')
            delete_button.pack(side=tk.LEFT)

            clear_button = ttk.Button(button_frame, text="Очистить", command=clear_button, style='Custom.TButton')
            clear_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для сохранения списка сайтов
            save_frame = tk.LabelFrame(main_frame, text="Сохранить список", padx=10, pady=10)
            save_frame.pack(padx=10, pady=10)

            filename_entry = ttk.Entry(save_frame, style='Custom.TEntry', font=('Arial', 14), justify='center')
            filename_entry.pack(side=tk.LEFT, padx=5)

            save_button = ttk.Button(save_frame, text="Сохранить", command=save_sites, style='Custom.TButton')
            save_button.pack(side=tk.LEFT, padx=5)

            # Создаем фрейм для загрузки списка сайтов
            load_frame = tk.LabelFrame(main_frame, text="Загрузить список", padx=10, pady=10)
            load_frame.pack(padx=10, pady=10)

            load_button = ttk.Button(load_frame, text="Загрузить", command=load_sites, style='Custom.TButton')
            load_button.pack()

            window_browser.mainloop()

        #Главное меню
        def menu():
            global win

            def exit_back_browser():
                try:
                    window.deiconify()
                    win.destroy()
                    win.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()

            try:
                window.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            win = Tk()
            win.resizable(width=False, height=False)
            win.title('Браузер')
            win.protocol('WM_DELETE_WINDOW', exit_back_browser)

            # получаем размер экрана
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            win.geometry(f"250x300+{center_x-230}+{center_y-300}")

            # задаем цвета для стиля Vista
            style_browser_1 = ttk.Style(win)
            style_browser_1.theme_use('vista')
            # Определяем цвета для кнопок
            style_browser_1.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")
            style_browser_1.configure("Purple.TButton", background="#4CAF50", foreground="purple", padding=10, font="Arial 12 bold")

            win.columnconfigure([0], weight=3, minsize=0)
            win.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=3, minsize=0)

            button1 = ttk.Button(win, text='Вконтакте + YouTube', command=func_browser.vk_and_youtube, style='Custom.TButton')
            button1.grid(row=0, column=0, columnspan=4, stick='wens')
            button2 = ttk.Button(win, text='Вконтакте', command=func_browser.vk, style='Custom.TButton')
            button2.grid(row=1, column=0, columnspan=4, stick='wens')
            button3 = ttk.Button(win, text='YouTube', command=func_browser.youtube, style='Custom.TButton')
            button3.grid(row=2, column=0, columnspan=4, stick='wens')
            button4 = ttk.Button(win, text='Переводчик', command=func_browser.google_translate, style='Custom.TButton')
            button4.grid(row=3, column=0, columnspan=4, stick='wens')
            button5 = ttk.Button(win, text='Google Диск', command=func_browser.google_disk, style='Custom.TButton')
            button5.grid(row=4, column=0, columnspan=4, stick='wens')
            button6 = ttk.Button(win, text='Gmail', command=func_browser.gmail, style='Custom.TButton')
            button6.grid(row=5, column=0, columnspan=4, stick='wens')
            button7 = ttk.Button(win, text='Менеджер сайтов', command=func_browser.sites_open, style='Purple.TButton')
            button7.grid(row=6, column=0, columnspan=4, stick='wens')

            win.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция автокликера
    counter = 0
    dbs = 0
    class status_on:
        # Справка о баге
        def bug():
            messagebox.showinfo("Подсказка", "Если вы хотите больше кликов чем 3 в секунду, то нажмите на кнопку автокликера несколько раз и клик суммируется.\nЕсли вы выберете для каждого клика свою клавишу, то при нажатии на нее, будет происходит тот клик, на который вы назначили клавишу.", parent=None)

        # Справка об автокликере
        def reference():
            ref_win = Tk()
            ref_win.title("Справка")
            ref_win.geometry("498x113")
            ref_win.resizable(width=False, height=False)
            ref_win.columnconfigure([0], weight = 1, minsize = 150)
            ref_win.rowconfigure([0], weight = 1, minsize = 0)

            # получаем размер экрана
            screen_width = ref_win.winfo_screenwidth()
            screen_height = ref_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            ref_win.geometry(f"498x113+{center_x-300}+{center_y-200}")

            label_ref = Label(ref_win, font=("Verdana", 10, "bold"), text="Если удерживать клавишу контролирующего клика,\nто клик будет происходить по вашему нажатию на клавишу.\nЕсли нажать клавишу 1, то автокликер будет постоянно кликать.\nЕсли нажать клавишу 2, то автокликер перестанет кликать.\nЕсли нажать клавишу 3, то автокликер завершит работу", fg="black")
            label_ref.grid(column=0, row=0)

            ref_button = Button(ref_win, text="Подсказка", font=("Verdana", 10, "bold"), width=15, height=1, command=status_on.bug, bg="#d3d3d3", fg="red")
            ref_button.grid(column=0, row=1, stick="wens")

        # Один клик
        def one_click_win():
            # Поток для тройного клика
            def thread1():
                threading.Thread(target=all_clicks_one).start()

            def clicks_one():
                global dbs, counter
                value = enter_one_win.get()
                dbs += 1
                counter += 1
                label_one_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(dbs) + ' раз в секунду')
                enter_one_win.configure(state=DISABLED)

            # Сброс значений dbs и counter
            def reset_values_one():
                global dbs, counter
                dbs = 0
                counter = 0
                label_one_win.configure(text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
                enter_one_win.configure(state=NORMAL)
                enter_one_win.delete(0, END)

            # Функция выполнения одного клика в секунду
            def one_click():
                value = enter_one_win.get()
                if value in ["1", "2", "3", ""]:
                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")
                    key_error.resizable(width=False, height=False)

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(key_error, font=("Verdana", 16, "bold"), text='Невозможно использовать клавишу "{}"'.format(value), fg="red", bg="white")
                    key_label.grid(column=0, row=0)

                    key_error_button = Button(key_error, font=('Verdana', 10, 'bold'), text='Как пользоваться?', fg='red',
                                               bg='#d3d3d3', command=status_on.reference)
                    key_error_button.grid(column=0, row=1, stick='wens')

                    reset_values_one()

                    key_error.mainloop()
                else:
                    try:

                        # Цикл работы автокликера
                        while True:

                            # Автокликер запущен, клавиша нажата
                            if keyboard.is_pressed(value):

                                # Функция одного клика в секунду при контролирующей клавише
                                pyautogui.click()

                            # Автокликер запущен
                            elif keyboard.is_pressed("1"):

                                # Цикл работы автокликера при нажатии клавиши "1"
                                while True:

                                    # Функция одного клика в секунду
                                    pyautogui.Click()

                                    # Автокликер не запущен
                                    if keyboard.is_pressed("2"):

                                        # Выход из цикла в предыдущий
                                        break

                                    # Выход из кода в главное меню
                                    elif keyboard.is_pressed("3"):
                                        try:
                                            reset_values_one()
                                            status_win.deiconify()
                                            one_win.destroy()
                                            one_win.quit()
                                            return
                                        except NameError:
                                            reset_values_one()
                                            window.deiconify()
                                            one_win.destroy()
                                            one_win.quit()
                                            return
                                            try:
                                                reset_values_one()
                                                window.deiconify()
                                                one_win.destroy()
                                                one_win.quit()
                                                return
                                            except NameError:
                                                reset_values_one()
                                                window.deiconify()
                                                one_win.destroy()
                                                one_win.quit()
                                                return
                                        except TclError:
                                            reset_values_one()
                                            window.deiconify()
                                            one_win.destroy()
                                            one_win.quit()
                                            return

                            # Выход из кода в главное меню
                            elif keyboard.is_pressed("3"):
                                try:
                                    reset_values_one()
                                    status_win.deiconify()
                                    one_win.destroy()
                                    one_win.quit()
                                    return
                                except NameError:
                                    reset_values_one()
                                    window.deiconify()
                                    one_win.destroy()
                                    one_win.quit()
                                    return
                                    try:
                                        reset_values_one()
                                        window.deiconify()
                                        one_win.destroy()
                                        one_win.quit()
                                        return
                                    except NameError:
                                        reset_values_one()
                                        window.deiconify()
                                        one_win.destroy()
                                        one_win.quit()
                                        return
                                except TclError:
                                    reset_values_one()
                                    window.deiconify()
                                    one_win.destroy()
                                    one_win.quit()
                                    return
                    except ValueError:
                        one_win.withdraw()
                        messagebox.showerror("Ошибка", "Введите пожалуйста любой символ", parent=one_win)
                        one_win.deiconify()
                    except TclError:
                        pass

            def one_win_close_window():
                if enter_one_win.get() and one_win_button and keyboard != '3':
                    one_win.withdraw()
                    messagebox.showerror("Предупреждение", 'Выйдите из цикла нажав на цифру "3"\nЕсли вы не нажали клавишу запуска, то уберите символ из поля ввода\nПодробнее в "Справка"', parent=one_win)
                    one_win.deiconify()
                else:
                    try:
                        status_win.deiconify()
                        one_win.destroy()
                        one_win.quit()
                    except NameError:
                        window.deiconify()
                        one_win.destroy()
                        one_win.quit()
                    except TclError:
                        window.deiconify()
                        one_win.destroy()
                        one_win.quit()
            try:
                status_win.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            def all_clicks_one():
                clicks_one()
                one_click()

            global enter_three_win, one_win
            # Окно одного клика в секунду
            one_win = Tk()
            one_win.title("Один клик")
            one_win.resizable(width=False, height=False)
            one_win.protocol('WM_DELETE_WINDOW', one_win_close_window)
            one_win.rowconfigure([0, 1], weight=15, minsize=0)
            one_win.columnconfigure([0], weight=15, minsize=0)

            # получаем размер экрана
            screen_width = one_win.winfo_screenwidth()
            screen_height = one_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            one_win.geometry(f"370x150+{center_x-280}+{center_y-200}")

            style_autoclicker = ttk.Style(one_win)
            style_autoclicker.theme_use('vista')
            style_autoclicker.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            label_one_win = Label(one_win, text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
            label_one_win.grid(column=0, row=0)

            # Поле для ввода буквы
            enter_one_win = Entry(one_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black", justify='center')
            enter_one_win.grid(column=0, row=1)

            one_win_button = ttk.Button(one_win, text="Запуск", width=15, command=thread1, style='Custom.TButton')
            one_win_button.grid(column=0, row=2, stick="wens")
            two_win_button = ttk.Button(one_win, text="Справка", width=15, command=status_on.reference, style='Custom.TButton')
            two_win_button.grid(column=0, row=3, stick="wens")

            one_win.mainloop()

        # Двойной клик
        def two_click_win():
            # Поток двойного клика в секунду
            def thread2():
                threading.Thread(target=all_clicks_two).start()

            def clicks_two():
                global dbs, counter
                value = enter_two_win.get()
                dbs += 2
                counter += 1
                label_two_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(dbs) + ' раз в секунду')
                enter_two_win.configure(state=DISABLED)

            # Сброс значений dbs и counter
            def reset_values_two():
                global dbs, counter
                dbs = 0
                counter = 0
                label_two_win.configure(text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
                enter_two_win.configure(state=NORMAL)
                enter_two_win.delete(0, END)

            # Функция выполнения тройного клика в секунду
            def two_click():
                value = enter_two_win.get()
                if value in ["1", "2", "3"]:
                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")
                    key_error.resizable(width=False, height=False)

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(key_error, font=("Verdana", 16, "bold"), text='Невозможно использовать клавишу "{}"'.format(value), fg="red", bg="white")
                    key_label.grid(column=0, row=0)

                    key_error_button = Button(key_error, font=('Verdana', 10, 'bold'), text='Как пользоваться?', fg='red',
                                               bg='#d3d3d3', command=status_on.reference)
                    key_error_button.grid(column=0, row=1, stick='wens')

                    reset_values_two()

                    key_error.mainloop()
                else:
                    try:

                        # Цикл работы автокликера
                        while True:

                            # Автокликер запущен, клавиша нажата
                            if keyboard.is_pressed(value):

                                # Функция одного клика в секунду при контролирующей клавише
                                pyautogui.click()

                            # Автокликер запущен
                            elif keyboard.is_pressed("1"):

                                # Цикл работы автокликера при нажатии клавиши "1"
                                while True:

                                    # Функция одного клика в секунду
                                    pyautogui.doubleClick()

                                    # Автокликер не запущен
                                    if keyboard.is_pressed("2"):

                                        # Выход из цикла в предыдущий
                                        break

                                    # Выход из кода в главное меню
                                    elif keyboard.is_pressed("3"):
                                        try:
                                            reset_values_two()
                                            status_win.deiconify()
                                            two_win.destroy()
                                            two_win.quit()
                                            return
                                        except NameError:
                                            reset_values_two()
                                            window.deiconify()
                                            two_win.destroy()
                                            two_win.quit()
                                            return
                                            try:
                                                reset_values_two()
                                                window.deiconify()
                                                two_win.destroy()
                                                two_win.quit()
                                                return
                                            except NameError:
                                                reset_values_two()
                                                window.deiconify()
                                                two_win.destroy()
                                                two_win.quit()
                                                return
                                        except TclError:
                                            reset_values_two()
                                            window.deiconify()
                                            two_win.destroy()
                                            two_win.quit()
                                            return

                            # Выход из кода в главное меню
                            elif keyboard.is_pressed("3"):
                                try:
                                    reset_values_two()
                                    status_win.deiconify()
                                    two_win.destroy()
                                    two_win.quit()
                                    return
                                except NameError:
                                    reset_values_two()
                                    window.deiconify()
                                    two_win.destroy()
                                    two_win.quit()
                                    return
                                    try:
                                        reset_values_two()
                                        window.deiconify()
                                        two_win.destroy()
                                        two_win.quit()
                                        return
                                    except NameError:
                                        reset_values_two()
                                        window.deiconify()
                                        two_win.destroy()
                                        two_win.quit()
                                        return
                                except TclError:
                                    reset_values_two()
                                    window.deiconify()
                                    two_win.destroy()
                                    two_win.quit()
                                    return
                    except ValueError:
                        two_win.withdraw()
                        messagebox.showerror("Ошибка", "Введите пожалуйста любой символ", parent=two_win)
                        two_win.deiconify()
                    except TclError:
                        pass

            def two_win_close_window():
                if enter_two_win.get() and one_win_button and keyboard != '3':
                    two_win.withdraw()
                    messagebox.showerror("Предупреждение", 'Выйдите из цикла нажав на цифру "3"\nЕсли вы не нажали клавишу запуска, то уберите символ из поля ввода\nПодробнее в "Справка"', parent=two_win)
                    two_win.deiconify()
                else:
                    try:
                        two_win.destroy()
                        status_win.deiconify()
                        two_win.quit()
                    except NameError:
                        window.deiconify()
                    except TclError:
                        window.deiconify()
            try:
                status_win.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            def all_clicks_two():
                clicks_two()
                two_click()

            global enter_two_win, two_win, label_two_win
            # Окно двойного клика
            two_win = Tk()
            two_win.title("Два клика")
            two_win.resizable(width=False, height=False)
            two_win.protocol('WM_DELETE_WINDOW', two_win_close_window)
            two_win.rowconfigure([0, 1, 2], weight=15, minsize=0)
            two_win.columnconfigure([0], weight=15, minsize=0)

            # получаем размер экрана
            screen_width = two_win.winfo_screenwidth()
            screen_height = two_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            two_win.geometry(f"370x150+{center_x-280}+{center_y-200}")

            style_autoclicker = ttk.Style(two_win)
            style_autoclicker.theme_use('vista')
            style_autoclicker.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            label_two_win = Label(two_win, text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
            label_two_win.grid(column=0, row=0)
            enter_two_win = Entry(two_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black", justify='center')
            enter_two_win.grid(column=0, row=1)

            one_win_button = ttk.Button(two_win, text="Запуск", width=15, command=thread2, style='Custom.TButton')
            one_win_button.grid(column=0, row=2, stick="wens")
            two_win_button = ttk.Button(two_win, text="Справка", width=15, command=status_on.reference, style='Custom.TButton')
            two_win_button.grid(column=0, row=3, stick="wens")

            two_win.mainloop()

        # Тройной клик
        def three_click_win():
            # Поток для тройного клика
            def thread3():
                threading.Thread(target=all_clicks_three).start()

            def clicks_three():
                global dbs, counter
                value = enter_three_win.get()
                dbs += 3
                counter += 1
                label_three_win.configure(font = ('Verdana', 8, 'bold'), text = 'Вы назначили контролирующую клавишу "' + str(value) + '"\nВы нажали на кнопку запуск ' + str(counter) + ' раз\nВаш текущий клик: ' + str(dbs) + ' раз в секунду')
                enter_three_win.configure(state=DISABLED)

            # Сброс значений dbs и counter
            def reset_values_three():
                global dbs, counter
                dbs = 0
                counter = 0
                label_three_win.configure(text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
                enter_three_win.configure(state=NORMAL)
                enter_three_win.delete(0, END)

            # Функция выполнения тройного клика в секунду
            def three_click():
                value = enter_three_win.get()
                if value in ["1", "2", "3", ""]:
                    key_error = Tk()
                    key_error.title("Ошибка!")
                    key_error.geometry("490x58")
                    key_error.resizable(width=False, height=False)

                    key_error.columnconfigure([0, 1], minsize=0)
                    key_error.rowconfigure([0], minsize=0)

                    key_label = Label(key_error, font=("Verdana", 16, "bold"), text='Невозможно использовать клавишу "{}"'.format(value), fg="red", bg="white")
                    key_label.grid(column=0, row=0)

                    key_error_button = Button(key_error, font=('Verdana', 10, 'bold'), text='Как пользоваться?', fg='red',
                                               bg='#d3d3d3', command=status_on.reference)
                    key_error_button.grid(column=0, row=1, stick='wens')

                    reset_values_three()

                    key_error.mainloop()
                else:
                    try:

                        # Цикл работы автокликера
                        while True:

                            # Автокликер запущен, клавиша нажата
                            if keyboard.is_pressed(value):

                                # Функция тройного клика в секунду при контролирующей клавише
                                pyautogui.click()

                            # Автокликер запущен
                            elif keyboard.is_pressed("1"):

                                # Цикл работы автокликера при нажатии клавиши "1"
                                while True:

                                    # Функция одного клика в секунду
                                    pyautogui.tripleClick()

                                    # Автокликер не запущен
                                    if keyboard.is_pressed("2"):

                                        # Выход из цикла в предыдущий
                                        break

                                    # Выход из кода в главное меню
                                    elif keyboard.is_pressed("3"):
                                        try:
                                            reset_values_three()
                                            status_win.deiconify()
                                            three_win.destroy()
                                            three_win.quit()
                                            return
                                        except NameError:
                                            reset_values_three()
                                            window.deiconify()
                                            three_win.destroy()
                                            three_win.quit()
                                            return
                                            try:
                                                reset_values_three()
                                                window.deiconify()
                                                three_win.destroy()
                                                three_win.quit()
                                                return
                                            except NameError:
                                                reset_values_three()
                                                window.deiconify()
                                                three_win.destroy()
                                                three_win.quit()
                                                return
                                        except TclError:
                                            reset_values_three()
                                            window.deiconify()
                                            three_win.destroy()
                                            three_win.quit()
                                            return

                            # Выход из кода в главное меню
                            elif keyboard.is_pressed("3"):
                                try:
                                    reset_values_three()
                                    status_win.deiconify()
                                    three_win.destroy()
                                    three_win.quit()
                                    return
                                except NameError:
                                    reset_values_three()
                                    window.deiconify()
                                    three_win.destroy()
                                    three_win.quit()
                                    return
                                    try:
                                        reset_values_three()
                                        window.deiconify()
                                        three_win.destroy()
                                        three_win.quit()
                                        return
                                    except NameError:
                                        reset_values_three()
                                        window.deiconify()
                                        three_win.destroy()
                                        three_win.quit()
                                        return
                                except TclError:
                                    reset_values_three()
                                    window.deiconify()
                                    three_win.destroy()
                                    three_win.quit()
                                    return
                    except ValueError:
                        three_win.withdraw()
                        messagebox.showerror("Ошибка", "Введите пожалуйста любой символ", parent=three_win)
                        three_win.deiconify()
                    except TclError:
                        pass

            def three_win_close_window():
                if enter_three_win.get() and one_win_button and keyboard != '3':
                    three_win.withdraw()
                    messagebox.showerror("Предупреждение", 'Выйдите из цикла нажав на цифру "3"\nЕсли вы не нажали клавишу запуска, то уберите символ из поля ввода\nПодробнее в "Справка"', parent=three_win)
                    three_win.deiconify()
                else:
                    try:
                        three_win.destroy()
                        status_win.deiconify()
                        three_win.quit()
                    except NameError:
                        window.deiconify()
                    except TclError:
                        window.deiconify()
            try:
                status_win.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            def all_clicks_three():
                clicks_three()
                three_click()

            global enter_three_win
            # Окно тройного клика в секунду
            three_win = Tk()
            three_win.title("Три кликa")
            three_win.resizable(width=False, height=False)
            three_win.protocol('WM_DELETE_WINDOW', three_win_close_window)
            three_win.rowconfigure([0, 1], weight=15, minsize=0)
            three_win.columnconfigure([0], weight=15, minsize=0)

            # получаем размер экрана
            screen_width = three_win.winfo_screenwidth()
            screen_height = three_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            three_win.geometry(f"370x150+{center_x-280}+{center_y-200}")

            style_autoclicker = ttk.Style(three_win)
            style_autoclicker.theme_use('vista')
            style_autoclicker.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            label_three_win = Label(three_win, text="Назначьте клавишу контролирующего клика", font=("Verdana", 9, "bold"))
            label_three_win.grid(column=0, row=0)

            # Поле для ввода буквы
            enter_three_win = Entry(three_win, font=("Verdana", 10, "bold"), bg="#d3d3d3", fg="black", justify='center')
            enter_three_win.grid(column=0, row=1)

            one_win_button = ttk.Button(three_win, text="Запуск", width=15, command=thread3, style='Custom.TButton')
            one_win_button.grid(column=0, row=2, stick="wens")
            two_win_button = ttk.Button(three_win, text="Справка", width=15, command=status_on.reference, style='Custom.TButton')
            two_win_button.grid(column=0, row=3, stick="wens")

            three_win.mainloop()

        def exit_back():
            try:
                win.deiconify()
                status_win.destroy()
                status_win.quit()
            except NameError:
                window.deiconify()
            except TclError:
                window.deiconify()

        # Автокликер
        def status():
            global status_win
            win.withdraw()
            status_win = Tk()
            status_win.title("Автокликер")
            status_win.protocol('WM_DELETE_WINDOW', status_on.exit_back)
            status_win.columnconfigure([0], weight=15, minsize=0)
            status_win.rowconfigure([0, 1, 2], weight=15, minsize=0)

            # получаем размер экрана
            screen_width = status_win.winfo_screenwidth()
            screen_height = status_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            status_win.geometry(f"350x200+{center_x-280}+{center_y-200}")

            style_autoclicker = ttk.Style(status_win)
            style_autoclicker.theme_use('vista')
            style_autoclicker.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button1 = ttk.Button(status_win, text="1 клик в секунду", width=15, command=status_on.one_click_win, style='Custom.TButton')
            button1.grid(column=0, row=0, stick="wens")
            button2 = ttk.Button(status_win, text="2 клика в секунду", width=15, command=status_on.two_click_win, style='Custom.TButton')
            button2.grid(column=0, row=1, stick="wens")
            button3 = ttk.Button(status_win, text="3 клика в секунду", width=15, command=status_on.three_click_win, style='Custom.TButton')
            button3.grid(column=0, row=2, stick="wens")

            status_win.mainloop()

        def window_menu():

            # Выход в главное меню
            def exit_menu():
                try:
                    win.destroy()
                    window.deiconify()
                    win.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()
            try:
                window.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            global win
            # Родительское окно
            win = Tk()
            win.title("Автокликер")
            win.resizable(width=False, height=False)
            win.protocol('WM_DELETE_WINDOW', exit_menu)
            win.rowconfigure([0, 1], weight=15, minsize=0)
            win.columnconfigure([0], weight=15, minsize=0)

            # получаем размер экрана
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            win.geometry(f"300x200+{center_x-280}+{center_y-200}")

            style_autoclicker = ttk.Style(win)
            style_autoclicker.theme_use('vista')
            style_autoclicker.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button1 = ttk.Button(win, text="Меню автокликера", width=15, command=status_on.status, style='Custom.TButton')
            button1.grid(column=0, row=0, stick="wens")
            button2 = ttk.Button(win, text="Как использовать?", width=15, command=status_on.reference, style='Custom.TButton')
            button2.grid(column=0, row=1, stick="wens")

            win.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция починки ПК
    class FixPC:
        def clear_pc():
            global progress_bar
            progress_bar = ttk.Progressbar(fixpc_window, orient=HORIZONTAL, length=200, mode='indeterminate')
            progress_bar.grid(column=0, row=4, pady=10)

            def task():
                try:
                    button1.config(state='disabled')
                    button2.config(state='disabled')
                    button3.config(state='disabled')

                    progress_bar.config(mode='determinate', maximum=10, value=0)
                    progress_bar.start()

                    # Список команд для выполнения с названиями операций
                    commands = {
                    'Удаление временных файлов': f'RMDIR /S /Q "{os.path.join("C:", "Users", getpass.getuser(), "AppData", "Local", "Temp")}"',
                    'Очистка корзины': r'PowerShell.exe -Command "Clear-RecycleBin -Force"',
                    'Очистка журналов приложений': r'wevtutil el | Foreach-Object {wevtutil cl "$_"}',
                    'Очистка журналов системы': r'PowerShell.exe -Command "wevtutil.exe cl System"',
                    'Остановка службы обновления Windows': r'PowerShell.exe -Command "Stop-Service wuauserv"',
                    'Очистка загрузок обновлений Windows': f'RMDIR /S /Q "{os.path.join("C:", "Windows", "SoftwareDistribution", "Download")}"',
                    'Запуск службы обновления Windows': 'PowerShell.exe -Command "Start-Service wuauserv"',
                    'Очистка кэша Microsoft Store': r'PowerShell.exe -Command "Remove-Item -Force -Recurse $env:LOCALAPPDATA\\Packages\\Microsoft.WindowsStore*\\LocalCache"',
                    'Очистка кэша Prefetch': r'PowerShell.exe -Command "del /q/f/s "%systemwindow_pdf_to_word%\Prefetch\*""',
                    'Очистка журналов проверки обновлений': r'PowerShell.exe -Command "Get-ChildItem -Path $env:windir\logs\cbs -Recurse | Where-Object { $_.Name -like `"*log*`" } | Remove-Item -Force"',
                    'Очистка истории браузера IE': r'PowerShell.exe -Command "RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8"',
                    'Очистка временной папки': r'PowerShell.exe -Command "Get-ChildItem -Path $env:TEMP -Force | Remove-Item -Force -Recurse"',
                    'Очистка временной папки Windows': r'PowerShell.exe -Command "Get-ChildItem -Path C:\Windows\Temp -Force | Remove-Item -Force -Recurse"'

                    }

                    for i, (operation, command) in enumerate(commands.items()):
                        try:
                            subprocess.call(command, shell=True)
                            progress_bar['value'] = (i + 1) * 10
                            fix_label.config(text=operation + '...')
                            fixpc_window.update()
                        except FileExistsError:
                            messagebox.showinfo('Ошибка', 'Невозможно создать файл, так как он уже существует', parent=fixpc_window)

                    progress_bar.stop()
                    progress_bar.grid_remove()
                    fix_label.config(text='')

                    messagebox.showinfo('Успех!', 'Очистка ПК завершена', parent=fixpc_window)

                    button1.config(state='enabled')
                    button2.config(state='enabled')
                    button3.config(state='enabled')
                except RuntimeError:
                    pass

            thread = threading.Thread(target=task)
            thread.start()


        def check_files():
            progress_bar = ttk.Progressbar(fixpc_window, orient=HORIZONTAL, length=200, mode='indeterminate')
            progress_bar.grid(column=0, row=4, pady=10)

            def task():
                try:
                    button1.config(state='disabled')
                    button2.config(state='disabled')
                    button3.config(state='disabled')

                    progress_bar.start(10)

                    # Выполнение команды sfc
                    fix_label.config(text="Проверка целостности файлов...")
                    subprocess.call("sfc /scannow", shell=True)
                    progress_bar.step(1)

                    # Выполнение команды DISM для проверки здоровья образа
                    fix_label.config(text="Проверка целостности образа Windows...")
                    subprocess.call("DISM /Online /Cleanup-Image /CheckHealth", shell=True)
                    progress_bar.step(1)

                    # Выполнение команды DISM для сканирования здоровья образа
                    fix_label.config(text="Вторичная проверка целостности образа Windows...")
                    subprocess.call("DISM /Online /Cleanup-Image /ScanHealth", shell=True)
                    progress_bar.step(1)

                    # Выполнение команды DISM для восстановления здоровья образа
                    fix_label.config(text="Восстановление файлов Windows...")
                    subprocess.call("DISM /Online /Cleanup-Image /RestoreHealth", shell=True)
                    progress_bar.step(1)

                    progress_bar.stop()
                    progress_bar.grid_remove()
                    fix_label.config(text="")

                    messagebox.showinfo('Успех!', 'Проверка и восстановление поврежденных файлов завершена', parent=fixpc_window)

                    button1.config(state='enabled')
                    button2.config(state='enabled')
                    button3.config(state='enabled')
                except RuntimeError:
                    pass

            thread = threading.Thread(target=task)
            thread.start()

        def fix_sound():
            def fix_sound_threading():
                try:
                    button1.config(state='disabled')
                    button2.config(state='disabled')
                    button3.config(state='disabled')

                    fix_label.config(text="Перезапуск службы звука...")
                    os.system('net stop audiosrv')
                    os.system('net start audiosrv')
                    answer = messagebox.askyesno("Починка звука №1", "Помогло данное решение?", parent=fixpc_window)
                    if answer == True:
                        fix_label.config(text='Рад был помочь!')
                        button1.config(state='enabled')
                        button2.config(state='enabled')
                        button3.config(state='enabled')
                    elif answer == False:
                        fix_label.config(text="Перезапуск службы звука №2...")
                        os.system('net stop "Windows Audio"')
                        os.system('net start "Windows Audio"')
                        answer_2 = messagebox.askyesno("Починка звука №2", "Помогло данное решение?", parent=fixpc_window)
                        if answer_2 == True:
                            fix_label.config(text='Рад был помочь!')
                            button1.config(state='enabled')
                            button2.config(state='enabled')
                            button3.config(state='enabled')
                        else:
                            fix_label.config(text="Меняем тип запуска звука...")
                            os.system('sc config Audiosrv start= auto')
                            answer_3 = messagebox.askyesno("Починка звука №3", "Помогло данное решение?", parent=fixpc_window)
                            if answer_3 == True:
                                fix_label.config(text='Рад был помочь!')
                                button1.config(state='enabled')
                                button2.config(state='enabled')
                                button3.config(state='enabled')
                            else:
                                messagebox.showinfo('Другие способы', 'Попробуйте запустить пункт "Проверка файлов"', parent=fixpc_window)
                                button1.config(state='enabled')
                                button2.config(state='enabled')
                                button3.config(state='enabled')
                                fix_label.config(text="")
                except RuntimeError:
                    pass

            thread = threading.Thread(target=fix_sound_threading)
            thread.start()

        def start_window_FixPC():
            global fixpc_window, fix_label, button1, button2, button3

            def exit_back_fixpc():
                try:
                    window.deiconify()
                    fixpc_window.destroy()
                    fixpc_window.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()

            try:
                window.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            fixpc_window = Tk()
            fixpc_window.title('Починка ПК')
            fixpc_window.resizable(width=False, height=False)
            fixpc_window.columnconfigure([0], weight=1, minsize=250)
            fixpc_window.rowconfigure([0, 1, 2], weight=1, minsize=0)
            fixpc_window.protocol('WM_DELETE_WINDOW', exit_back_fixpc)

            # получаем размер экрана
            screen_width = fixpc_window.winfo_screenwidth()
            screen_height = fixpc_window.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            fixpc_window.geometry(f"370x200+{center_x-280}+{center_y-200}")

            style_fixpc = ttk.Style(fixpc_window)
            style_fixpc.theme_use('vista')
            # Определяем цвета для кнопок
            style_fixpc.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            button1 = ttk.Button(fixpc_window, text='Очистка ПК', width=15, command=FixPC.clear_pc, style='Custom.TButton')
            button1.grid(column=0, row=0, sticky='wens')
            button2 = ttk.Button(fixpc_window, text='Проверка файлов', width=15, command=FixPC.check_files, style='Custom.TButton')
            button2.grid(column=0, row=1, sticky='wens')
            button3 = ttk.Button(fixpc_window, text='Починка звука', width=15, command=FixPC.fix_sound, style='Custom.TButton')
            button3.grid(column=0, row=2, sticky='wens')

            fix_label = Label(fixpc_window, text="", font=("Arial", 12))
            fix_label.grid(column=0, row=3, sticky='wens')

            fixpc_window.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция системы Windows
    class system_windows():
        #Потоки на функции
        def thread_cmds():
            threading.Thread(target = system_windows.cmds).start()
        def thread_autoloading():
            threading.Thread(target = system_windows.autoloading).start()
        def thread_regedit():
            threading.Thread(target = system_windows.regedit).start()
        def thread_services():
            threading.Thread(target = system_windows.services).start()
        def thread_appdata():
            threading.Thread(target = system_windows.appdata).start()
        def thread_device_manager():
            threading.Thread(target = system_windows.device_manager).start()

        def cmds():
            os.system('explorer C:\\Windows\\System32\\cmd.exe')
        def autoloading():
            os.system('explorer C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        def regedit():
            os.system('%windir%\\regedit.exe')
        def services():
            os.system('%windir%\\system32\\services.msc')
        def appdata():
            os.system('explorer C:\\Users\\' + os.environ['USERNAME'] + '\\AppData')
        def device_manager():
            os.system('explorer C:\\Windows\\System32\\devmgmt.msc')

        def on_closing():
            try:
                window_system.destroy()
                window.deiconify()
                window_system.quit()
            except NameError:
                window.deiconify()
            except TclError:
                window.deiconify()

        #Завершение процесса
        def finish_process():
            try:
                window_system.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            def kill_finish_process():
                nonlocal entry_finish_process
                value = entry_finish_process.get()
                os.system('Taskkill /PID ' + value + ' /F /T')

            def enter_finish_process(event=None):
                kill_finish_process()

            taskkill = subprocess.getoutput('TASKLIST /FI "USERNAME ne NT AUTHORITY\\SYSTEM" /FI "STATUS eq running"')
            process_list = []
            max_name_length = 0
            for line in taskkill.split('\n')[3:]:
                line = line.split()
                if len(line) > 1:
                    name = line[0]
                    pid = line[1]
                    process_list.append((name, pid))
                    max_name_length = max(max_name_length, len(name))

            def exit_back_system():
                try:
                    finish_process_win.destroy()
                    window_system.deiconify()
                    finish_process_win.quit()
                except NameError:
                    window.deiconify()
                except TclError:
                    window.deiconify()

            finish_process_win = Tk()
            finish_process_win.title('Завершить процесс')
            finish_process_win.protocol('WM_DELETE_WINDOW', exit_back_system)

            # получаем размер экрана
            screen_width = finish_process_win.winfo_screenwidth()
            screen_height = finish_process_win.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            finish_process_win.geometry(f"300x400+{center_x-280}+{center_y-200}")

            style_process_window = ttk.Style(finish_process_win)
            style_process_window.theme_use('vista')
            style_process_window.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            label_finish_process = ttk.Label(finish_process_win, text='Выберите процесс:', style='Custom.TButton')
            label_finish_process.grid(column=0, row=0, sticky='wens')

            lb = Listbox(finish_process_win, font=('Verdana', 10, 'bold'), height=len(process_list), width=max_name_length + 10)
            lb.grid(column=0, row=1, sticky='wens')

            # Показ только имени процесса и его PID
            for process in process_list:
                lb.insert(END, f'{process[0]}, [{process[1]}]')

            entry_finish_process = Entry(finish_process_win, font=('Verdana', 10, 'bold'))
            entry_finish_process.grid(column=0, row=2, sticky='wens')
            
            def update_process_list():
                current_selection = lb.curselection()
                current_position = lb.yview()
                taskkill = subprocess.getoutput('TASKLIST /FI "USERNAME ne NT AUTHORITY\\SYSTEM" /FI "STATUS eq running"')
                process_list = []
                max_name_length = 0
                for line in taskkill.split('\n')[3:]:
                    line = line.split()
                    if len(line) > 1:
                        name = line[0]
                        pid = line[1]
                        process_list.append((name, pid))
                        max_name_length = max(max_name_length, len(name))
                lb.delete(0, END)
                # Показ только имени процесса и его PID
                for process in process_list:
                    lb.insert(END, f'{process[0]}, [{process[1]}]')
                lb.yview_moveto(current_position[0])
                if current_selection:
                    lb.select_set(current_selection[0])
                finish_process_win.after(1000, update_process_list)
            update_process_list()

            button_finish_process = ttk.Button(finish_process_win, text='Завершить процесс', command=kill_finish_process, style='Custom.TButton')
            button_finish_process.grid(column=0, row=3, sticky='wens')

            def on_select(evt):
                nonlocal entry_finish_process
                selected_process = lb.get(lb.curselection())
                selected_pid = selected_process[selected_process.index('[') + 1:selected_process.index(']')]
                entry_finish_process.delete(0, END)
                entry_finish_process.insert(END, selected_pid)

            lb.bind('<<ListboxSelect>>', on_select)

            finish_process_win.bind('<Return>', enter_finish_process)
            finish_process_win.columnconfigure([0], weight=1, minsize=150)
            finish_process_win.rowconfigure([0, 1, 2], weight=1, minsize=0)
            finish_process_win.mainloop()

            taskkill = subprocess.getoutput('TASKLIST /FI "USERNAME ne NT AUTHORITY\\SYSTEM" /FI "STATUS eq running"')
            process_list = []
            max_name_length = 0
            for line in taskkill.split('\n')[3:]:
                line = line.split()
                if len(line) > 1:
                    name = line[0]
                    pid = line[1]
                    process_list.append((name, pid))
                    max_name_length = max(max_name_length, len(name))
            lb.delete(0, END)
            # Показ только имени процесса и его PID
            for process in process_list:
                lb.insert(END, f'{process[0]}, [{process[1]}]')

        def menu():
            global window_system
            try:
                window.withdraw()
            except NameError:
                pass
            except TclError:
                window.deiconify()

            #Родительское окно
            window_system = Tk()
            window_system.title('Система')
            window_system.resizable(width=False, height=False)
            window_system.protocol('WM_DELETE_WINDOW', system_windows.on_closing)
            window_system.columnconfigure([0], minsize = 150)
            window_system.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize = 0)

            # получаем размер экрана
            screen_width = window_system.winfo_screenwidth()
            screen_height = window_system.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            window_system.geometry(f"298x330+{center_x-280}+{center_y-200}")

            style_window_system = ttk.Style(window_system)
            style_window_system.theme_use('vista')
            style_window_system.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

            #Кнопки родительского окна
            button1 = ttk.Button(window_system, text = 'Командная строка', command = system_windows.thread_cmds, width = 30, style='Custom.TButton')
            button1.grid(column = 0, row = 0, stick = 'wens')
            button2 = ttk.Button(window_system, text = 'Папка автозагрузки', command = system_windows.thread_autoloading, width = 30, style='Custom.TButton')
            button2.grid(column = 0, row = 1, stick = 'wens')
            button3 = ttk.Button(window_system, text = 'Реестр', command = system_windows.thread_regedit, width = 30, style='Custom.TButton')
            button3.grid(column = 0, row = 2, stick = 'wens')
            button4 = ttk.Button(window_system, text = 'Службы', command = system_windows.thread_services, width = 30, style='Custom.TButton')
            button4.grid(column = 0, row = 3, stick = 'wens')
            button5 = ttk.Button(window_system, text = 'Папка appdata', command = system_windows.thread_appdata, width = 30, style='Custom.TButton')
            button5.grid(column = 0, row = 4, stick = 'wens')
            button6 = ttk.Button(window_system, text = 'Диспетчер устройств', command = system_windows.thread_device_manager, width = 30, style='Custom.TButton')
            button6.grid(column = 0, row = 5, stick = 'wens')
            button7 = ttk.Button(window_system, text = 'Завершить процесс приложения', command = system_windows.finish_process, width = 30, style='Custom.TButton')
            button7.grid(column = 0, row = 6, stick = 'wens')

            window_system.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция рандомайзера
    def random_exit_menu_random_2():
        try:
            main_random_win.withdraw()
            random_win.deiconify()
        except NameError:
            window.deiconify()
        except TclError:
            window.deiconify()

    # Скрытие меню случайного числа и открытие генератора чисел
    def withdraw_generator_number():
        try:
            main_random_win.withdraw()
            generator_number()
        except NameError:
            window.withdraw()
            generator_number()
        except TclError:
            random_number_random_win()

    # Скрытие меню случайного числа и открытие вывода
    def withdraw_random_number():
        try:
            main_random_win.withdraw()
            random_number()
        except NameError:
            window.withdraw()
            random_number()
        except TclError:
            random_number_random_win()

    # Меню случайного числа и генератора чисел
    def random_number_random_win():
        try:
            random_win.withdraw()
        except NameError:
            window.deiconify()
        except TclError:
            window.deiconify()

        try:
            window.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        global main_random_win
        main_random_win = Tk()
        main_random_win.resizable(width=False, height=False)
        main_random_win.title('Случайное число')
        main_random_win.protocol('WM_DELETE_WINDOW', random_exit_menu_random_2)

        # получаем размер экрана
        screen_width = main_random_win.winfo_screenwidth()
        screen_height = main_random_win.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        main_random_win.geometry(f"300x140+{center_x-280}+{center_y-200}")

        style_random = ttk.Style(main_random_win)
        style_random.theme_use('vista')

        # Определяем цвета для кнопок
        style_random.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        main_random_win.columnconfigure([0,1], weight=1, minsize=60)
        main_random_win.rowconfigure([0,1], weight=1, minsize=70)
        
        button1 = ttk.Button(main_random_win, text='Случайное число \n от 1 до 100', command=withdraw_random_number, style="Custom.TButton")
        button1.grid(row=0, column=0, columnspan=4, sticky='wens')
        button2 = ttk.Button(main_random_win, text='Генератор чисел', command=withdraw_generator_number, style="Custom.TButton")
        button2.grid(row=1, column=0, columnspan=4, sticky='wens')

    # Вывод из случайного числа от 1 до 100
    def random_number():
        def exit_menu_random():
            try:
                main_random_win.deiconify()
                output_main_random_win.destroy()
            except NameError:
                window.deiconify()
                output_main_random_win.destroy()
            except TclError:
                window.deiconify()
                output_main_random_win.destroy()

        def generated_random_number():
            text_r.configure(text=f'Ваше число: {random.randint(0, 100)}')
        def generated_random_number_enter(Return):
            generated_random_number()

        window.withdraw()
        output_main_random_win = Tk()
        output_main_random_win.resizable(width=False, height=False)
        output_main_random_win.title('Вывод')
        output_main_random_win.protocol('WM_DELETE_WINDOW', exit_menu_random)

        # получаем размер экрана
        screen_width = output_main_random_win.winfo_screenwidth()
        screen_height = output_main_random_win.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        output_main_random_win.geometry(f"219x83+{center_x-280}+{center_y-200}")

        style_random_2 = ttk.Style(output_main_random_win)
        style_random_2.theme_use('vista')
        style_random_2.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        text_r = ttk.Label(output_main_random_win, font=('Arial', 20))
        text_r.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='wens')
        text_r.configure(text=f'Ваше число: {random.randint(0, 100)}')

        button_output_main_random_win = ttk.Button(output_main_random_win, text='Сгенерировать еще раз', command=generated_random_number, style='Custom.TButton')
        button_output_main_random_win.grid(row=1, column=0, columnspan=4, rowspan=1, sticky='wens')

        output_main_random_win.bind('<Return>', generated_random_number_enter)
                
    def generator_number():
        N = 'N'
    
        def enter_generate(Return):
            generate()

        def generate():
            try:
                b = before.get()
                t = to.get()
                if b > t:
                    text_f.grid(row = 6, column = 2, columnspan = 4, rowspan = 2, sticky = 'wens')
                    text_f.configure(text = 'Ошибка!', font=('Arial 15'))
                b1 = int(b)
                t1 = int(t)
                N = random.randint(b1, t1)
                text_f.configure(text = f'Ваше число: {N}')
            except ValueError:
                    text_f.grid(row = 6, column = 2, columnspan = 4, rowspan = 2, sticky = 'wens')
                    text_f.configure(text = 'Ошибка!', font=('Arial 15'))

        try:
            random_win.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        def exit_menu():
            try:
                main_random_win.deiconify()
                generator_number_win.destroy()
            except NameError:
                window.deiconify()
                generator_number_win.destroy()
            except TclError:
                window.deiconify()
                generator_number_win.destroy()

        generator_number_win = Tk()
        generator_number_win.resizable(width=False, height=False)
        generator_number_win.title('Генератор чисел "От" и "До"')
        generator_number_win.bind('<Return>', enter_generate)
        generator_number_win.protocol('WM_DELETE_WINDOW', exit_menu)

        # получаем размер экрана
        screen_width = generator_number_win.winfo_screenwidth()
        screen_height = generator_number_win.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        generator_number_win.geometry(f"300x140+{center_x-280}+{center_y-200}")

        generator_number_win.columnconfigure([0,1,2], weight=1, minsize=10)
        generator_number_win.rowconfigure([0,1,2], weight=1, minsize=10)

        style_random_3 = ttk.Style(generator_number_win)
        style_random_3.theme_use('vista')
        style_random_3.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        text_g = ttk.Label(generator_number_win, font = ('Verdana', 10))
        text_g.grid(row = 0, column = 0, columnspan = 2, rowspan = 1, stick = 'wens')
        text_g.configure(text = 'От', font=('Arial 15'))

        text2_g = ttk.Label(generator_number_win, font = ('Verdana', 10))
        text2_g.grid(row = 1, column = 0, columnspan = 2, rowspan = 3, stick = 'wens')
        text2_g.configure(text = 'До', font=('Arial 15'))

        before = ttk.Entry(generator_number_win, justify=LEFT, font = ('Arial', 15))
        before.grid(row = 0, column = 2, columnspan = 1, sticky='wens')

        to = ttk.Entry(generator_number_win, justify=LEFT, font = ('Arial', 15))
        to.grid(row = 1, column = 2, rowspan = 3, columnspan = 1, sticky='wens')

        text_f = ttk.Label(generator_number_win, font = ('Verdana', 10, 'bold'))
        text_f.grid(row = 6, column = 1, columnspan = 2, rowspan = 1, stick = 'wens')
        text_f.configure(text = f'Ваше число: {N}', font=('Arial 15'))

        button_r = ttk.Button(generator_number_win, text = 'Сгенерировать', command = generate, style='Custom.TButton')
        button_r.grid(row = 4, column = 0, columnspan = 4, sticky = 'wens')

    def heads_or_tails():
        try:
            random_win.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        def exit_menu():
            try:
                random_win.deiconify()
                heads_or_tails_win.destroy()
                heads_or_tails_win.quit()
            except NameError:
                window.deiconify()
                heads_or_tails_win.destroy()
                heads_or_tails_win.quit()
            except TclError:
                window.deiconify()
                heads_or_tails_win.destroy()
                heads_or_tails_win.quit()
        try:
            window.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        heads_or_tails_win = Tk()
        heads_or_tails_win.geometry('280x100')
        heads_or_tails_win.resizable(width=False, height=False)
        heads_or_tails_win.title('Орёл или Решка')
        heads_or_tails_win.protocol('WM_DELETE_WINDOW', exit_menu)

        # получаем размер экрана
        screen_width = heads_or_tails_win.winfo_screenwidth()
        screen_height = heads_or_tails_win.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        heads_or_tails_win.geometry(f"219x83+{center_x-280}+{center_y-200}")

        style_random_4 = ttk.Style(heads_or_tails_win)
        style_random_4.theme_use('vista')
        style_random_4.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        heads_or_tails_win.columnconfigure([0,1], weight=1, minsize=10)
        heads_or_tails_win.rowconfigure([0,1], weight=1, minsize=10)

        text_h = Label(heads_or_tails_win,text = 'Нажмите на кнопку', font = ('Arial', 15, 'bold'))
        text_h.grid(row = 0, column = 0, stick = 'wens')

        def throw_coin_not_enter():
            list = ['Орёл', 'Решка', 'Орёл', 'Решка']
            text_h.configure(text = f'{random.choice(list)}', font=('Arial', 20, 'bold'))
            text_h.grid(row = 0, column = 0, columnspan=2, stick = 'wens')

        def throw_coin(enter):
            throw_coin_not_enter()

        button1 = ttk.Button(heads_or_tails_win, text = 'Бросить еще раз', command = throw_coin_not_enter, style='Custom.TButton')
        button1.grid(row = 1, column = 0, columnspan=4, sticky='wens')
        heads_or_tails_win.bind('<Return>', throw_coin)

        heads_or_tails_win.mainloop()

    def menu():
        def exit_menu_2():
            try:
                window.deiconify()
                random_win.destroy()
                random_win.quit()
            except NameError:
                window.deiconify()
            except TclError:
                window.deiconify()

        try:
            window.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        global random_win
        random_win = Tk()
        random_win.resizable(width=False, height=False)
        random_win.title('Рандомайзер')
        random_win.protocol('WM_DELETE_WINDOW', exit_menu_2)

        # получаем размер экрана
        screen_width = random_win.winfo_screenwidth()
        screen_height = random_win.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        random_win.geometry(f"253x94+{center_x-280}+{center_y-200}")

        # стиль в стиле Vista
        style_random_5 = ttk.Style(random_win)
        style_random_5.theme_use('vista')

        # добавление стиля для кнопок
        style_random_5.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        # добавление кнопок с новым стилем
        button1 = ttk.Button(random_win, text='Случайное число', width = 25, command=random_number_random_win, style='Custom.TButton')
        button1.grid(row=0, column=0, columnspan=4, sticky='wens')
        button3 = ttk.Button(random_win, text='Орёл или Решка', width = 25, command=heads_or_tails, style='Custom.TButton')
        button3.grid(row=1, column=0, columnspan=4, sticky='wens')

        random_win.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция настроек бота
    def new_win():
        def update_window():
            # Перерисовываем кнопку but
            but.grid_forget()
            but_text = "Добавить бота в автозагрузку" if not check_startup_file() else "Бот в автозагрузке"
            but_state = NORMAL if not check_startup_file() else DISABLED
            but.config(text=but_text, state=but_state, style='Custom.TButton')
            but.grid(column=0, row=0, sticky='wens')

            # Перерисовываем кнопку but2
            but2.grid_forget()
            but2_text = "Убрать бота из автозагрузки" if check_startup_file() else "Бот не в автозагрузке"
            but2_state = NORMAL if check_startup_file() else DISABLED
            but2.config(text=but2_text, state=but2_state, style='Custom.TButton')
            but2.grid(column=0, row=1, sticky='wens')

        def check_startup_file():
            return os.path.isfile(os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "Бот-помощник.exe"))

        def auto_launch():
            os.system(f'copy /y {PATH} "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"')
            but.config(text="Бот успешно добавлен!", state=DISABLED, style='Custom.TButton')
            switch_button_states()
            update_window()

        def not_launch():
            os.system('del /q "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Бот-помощник.exe"')
            but2.config(text="Бот успешно убран!", state=DISABLED, style='Custom.TButton')
            switch_button_states()
            update_window()

        def exit_menu_2():
            try:
                nwin.destroy()
                window_setting_bot.deiconify()
                nwin.quit()
            except NameError:
                nwin.quit()
                window.deiconify()
            except TclError:
                nwin.quit()
                window.deiconify()

        try:
            window_setting_bot.withdraw()
            window.withdraw()
        except NameError:
            pass
        except TclError:
            pass

        nwin = Tk()
        nwin.resizable(width=False, height=False)
        nwin.title('Автозагрузка')
        nwin.columnconfigure([0], weight=1, minsize=150)
        nwin.rowconfigure([0, 1], weight=1, minsize=0)
        nwin.protocol('WM_DELETE_WINDOW', exit_menu_2)

        # получаем размер экрана
        screen_width = nwin.winfo_screenwidth()
        screen_height = nwin.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        nwin.geometry(f"300x150+{center_x-280}+{center_y-200}")

        style_setting_bot_autoload = ttk.Style(nwin)
        style_setting_bot_autoload.theme_use('vista')
        style_setting_bot_autoload.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        check_startup_file_result = check_startup_file()
        
        # Кнопки
        but_text = "Добавить бота в автозагрузку" if not check_startup_file_result else "Бот в автозагрузке"
        but_state = NORMAL if not check_startup_file_result else DISABLED
        but = ttk.Button(nwin, text=but_text, width=55, command=auto_launch, state=but_state, style='Custom.TButton')
        but.grid(column=0, row=0, sticky='wens')

        but2_text = "Убрать бота из автозагрузки" if check_startup_file_result else "Бот не в автозагрузке"
        but2_state = NORMAL if check_startup_file_result else DISABLED
        but2 = ttk.Button(nwin, text=but2_text, width=55, command=not_launch, state=but2_state, style='Custom.TButton')
        but2.grid(column=0, row=1, sticky='wens')

        # При нажатии на одну кнопку, другая становиться активной
        def switch_button_states():
            but_state = but['state']
            but2_state = but2['state']
            if but_state == NORMAL:
                but2['state'] = NORMAL
                but['state'] = DISABLED
            elif but2_state == NORMAL:
                but['state'] = NORMAL
                but2['state'] = DISABLED

        # Привяжем функцию switch_button_states к обработчикам событий на кнопках
        but.config(command=lambda: [switch_button_states(), auto_launch()])
        but2.config(command=lambda: [switch_button_states(), not_launch()])

        nwin.mainloop()

    # Выход из настроек бота
    def exit_menu():
        try:
            window_setting_bot.destroy()
            window.deiconify()
            window_setting_bot.quit()
        except NameError:
            window.deiconify()
        except TclError:
            window.deiconify()

    # Главное окно настроек бота
    def main_setting_bot():
        try:
            window.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()

        global window_setting_bot
        window_setting_bot = Tk()
        window_setting_bot.resizable(width=False, height=False)
        window_setting_bot.title('Настройки бота')
        window_setting_bot.columnconfigure([0], weight = 1, minsize = 150)
        window_setting_bot.rowconfigure([0,1], weight = 1, minsize = 0)
        window_setting_bot.protocol('WM_DELETE_WINDOW', exit_menu)

        # получаем размер экрана
        screen_width = window_setting_bot.winfo_screenwidth()
        screen_height = window_setting_bot.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_setting_bot.geometry(f"160x40+{center_x-190}+{center_y-200}")

        style_setting_bot = ttk.Style(window_setting_bot)
        style_setting_bot.theme_use('vista')
        style_setting_bot.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        #Кнопки
        button1 = ttk.Button(window_setting_bot, text = 'Автозагрузка', width = 15, command = new_win, style='Custom.TButton')
        button1.grid(column = 0, row = 0, sticky = 'wens')

        window.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Функция всего прочего
    def test_ethernet():
        global is_running, window_speed_test
        is_running = True
        def get_network_usage():
            network_io_counters = psutil.net_io_counters()
            sent_bytes = network_io_counters.bytes_sent
            recv_bytes = network_io_counters.bytes_recv
            time.sleep(1)
            network_io_counters = psutil.net_io_counters()
            sent_bytes_diff = network_io_counters.bytes_sent - sent_bytes
            recv_bytes_diff = network_io_counters.bytes_recv - recv_bytes
            total_bytes = sent_bytes_diff + recv_bytes_diff
            if total_bytes < 1024:
                return f"{total_bytes:.2f} Б/с"
            elif total_bytes < 1048576:
                return f"{total_bytes/1024:.2f} Кб/с"
            elif total_bytes < 1073741824:
                return f"{total_bytes/1048576:.2f} Мб/с"
            else:
                return f"{total_bytes/1073741824:.2f} Гб/с"

        def update_network_load():
            while True:
                network_usage = get_network_usage()
                label.config(text=f"Скорость интернета: {network_usage}")

        def test_speed():
            try:
                test_label.config(text="Подождите, идет тестирование...")
                window_speed_test.update() # обновление окна
                speed_test = speedtest.Speedtest()
                server_names = []
                speed_test.get_servers(server_names)
                test_label.config(text="Выбор лучшего сервера...")
                speed_test.get_best_server()
                test_label.config(text="Вычисляем скорость загрузки...")
                download_speed = speed_test.download()
                test_label.config(text="Вычисляем скорость выгрузки...")
                upload_speed = speed_test.upload()
                if download_speed < 1024:
                    download_result = f"{download_speed:.2f} Б/с"
                elif download_speed < 1048576:
                    download_result = f"{download_speed/1024:.2f} Кб/с"
                elif download_speed < 1073741824:
                    download_result = f"{download_speed/1048576:.2f} Мб/с"
                else:
                    download_result = f"{download_speed/1073741824:.2f} Гб/с"
                if upload_speed < 1024:
                    upload_result = f"{upload_speed:.2f} Б/с"
                elif upload_speed < 1048576:
                    upload_result = f"{upload_speed/1024:.2f} Кб/с"
                elif upload_speed < 1073741824:
                    upload_result = f"{upload_speed/1048576:.2f} Мб/с"
                else:
                    upload_result = f"{upload_speed/1073741824:.2f} Гб/с"
                test_label.config(text=f"Скорость загрузки: {download_result},\nСкорость выгрузки: {upload_result}")
                test_button.config(state=tk.ACTIVE)
            except speedtest.ConfigRetrievalError:
                test_label.config(text="Не удалось получить конфигурацию с сервера.")
                test_button.config(state=tk.ACTIVE)
            except speedtest.NoMatchedServers:
                test_label.config(text="Нет подходящих серверов\nдля тестирования скорости.")
                test_button.config(state=tk.ACTIVE)
            except speedtest.SpeedtestException:
                test_label.config(text="Произошла ошибка при тестировании скорости.")
                test_button.config(state=tk.ACTIVE)

        def test_speed_thread():
            global Thread
            test_button.config(state="disabled")
            Thread = threading.Thread(target=test_speed)
            Thread.start()

        def speed_window():
            global only_speed_window
            def update_network_load_2():
                while True:
                    network_usage = get_network_usage()
                    label.configure(text=f"Скорость интернета: {network_usage}")
            
            def exit_in_window_other_menu():
                try:
                    window_other_menu.deiconify()
                    only_speed_window.destroy()
                    only_speed_window.quit()
                except NameError:
                    window.deiconify()
                    only_speed_window.destroy()
                    only_speed_window.quit()
                except TclError:
                    window.deiconify()
                    only_speed_window.destroy()
                    only_speed_window.quit()

            try:
                window_speed_test.destroy()
                window_speed_test.quit()
            except NameError:
                pass
            except TclError:
                window_speed_test.destroy()
                window_speed_test.quit()
                window.deiconify()

            only_speed_window = Tk()
            only_speed_window.resizable(width=False, height=False)
            only_speed_window.title('Нагрузка')
            only_speed_window.columnconfigure([0], weight=1, minsize=150)
            only_speed_window.rowconfigure([0, 1, 2, 3], weight=1, minsize=0)
            only_speed_window.protocol("WM_DELETE_WINDOW", exit_in_window_other_menu)
            only_speed_window.attributes("-topmost", True)

            # получаем размер экрана
            screen_width = only_speed_window.winfo_screenwidth()
            screen_height = only_speed_window.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            only_speed_window.geometry(f"300x30+{center_x-220}+{center_y-200}")

            label = tk.Label(only_speed_window, text="Загрузка...", font=("Arial", 14))
            label.pack()

            thread = threading.Thread(target=update_network_load_2)
            thread.start()
            
            only_speed_window.mainloop()

        def on_top_test_speed():
            button_on_top.config(state=DISABLED)
            button_off_top.config(state=ACTIVE)
            window_speed_test.attributes("-topmost", True)
        def off_top_test_speed():
            button_on_top.config(state=ACTIVE)
            button_off_top.config(state=DISABLED)
            window_speed_test.attributes("-topmost", False)

        def on_closing():
            try:
                window_other_menu.deiconify()
                window_speed_test.destroy()
                window_speed_test.quit()
            except NameError:
                window.deiconify()
                window_speed_test.destroy()
                window_speed_test.quit()
            except TclError:
                window.deiconify()
                window_speed_test.destroy()
                window_speed_test.quit()

        try:
            window_other_menu.withdraw()
        except NameError:
            pass
        except TclError:
            window_speed_test.destroy()
            window_speed_test.quit()
            window.deiconify()

        window_speed_test = tk.Tk()
        window_speed_test.geometry('300x250')
        window_speed_test.resizable(width=False, height=False)
        window_speed_test.title('Нагрузка')
        window_speed_test.columnconfigure([0], weight=1, minsize=150)
        window_speed_test.rowconfigure([0, 1, 2, 3], weight=1, minsize=0)
        window_speed_test.protocol("WM_DELETE_WINDOW", on_closing)

        # получаем размер экрана
        screen_width = window_speed_test.winfo_screenwidth()
        screen_height = window_speed_test.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_speed_test.geometry(f"300x258+{center_x-220}+{center_y-200}")

        style_test_speed = ttk.Style(window_speed_test)
        style_test_speed.theme_use('vista')
        style_test_speed.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        label = tk.Label(window_speed_test, text="Загрузка...", font=("Arial", 14))
        label.pack()
        test_label = tk.Label(window_speed_test, text="", font=("Arial", 12))
        test_label.pack()

        test_button = ttk.Button(window_speed_test, text="Тест скорости интернета", width = 25, command=test_speed_thread, style='Custom.TButton')
        test_button.pack()
        button_on_top = ttk.Button(window_speed_test, text='Поверх всех окон', width = 25, command=on_top_test_speed, style='Custom.TButton')
        button_on_top.pack()
        button_on_top.config(state=DISABLED)
        button_off_top = ttk.Button(window_speed_test, text='Не поверх всех окон', width = 25, command=off_top_test_speed, style='Custom.TButton')
        button_off_top.pack()
        button_speed_window = ttk.Button(window_speed_test, text='Только скорость интернета', width = 25, command=speed_window, style='Custom.TButton')
        button_speed_window.pack()

        thread = threading.Thread(target=update_network_load)
        thread.start()
        
        window_speed_test.mainloop()

    # PDF → WORD
    def pdf_word_convert():
        global window_pdf_to_word
        def exit_pdf_word_menu():
            try:
                window_other_menu.deiconify()
                window_pdf_to_word.destroy()
                window_pdf_to_word.quit()
            except NameError:
                window.deiconify()
                window_pdf_to_word.destroy()
                window_pdf_to_word.quit()
            except TclError:
                window.deiconify()
                window_pdf_to_word.destroy()
                window_pdf_to_word.quit()

        try:
            window_other_menu.withdraw()
        except NameError:
            window.withdraw()
        except TclError:
            pass

        # создаем окно приложения
        window_pdf_to_word = tk.Tk()
        window_pdf_to_word.title('Конвертер PDF в Word')
        window_pdf_to_word.protocol('WM_DELETE_WINDOW', exit_pdf_word_menu)

        # Получаем размер экрана
        screen_width = window_pdf_to_word.winfo_screenwidth()
        screen_height = window_pdf_to_word.winfo_screenheight()

        # Задаем размеры окна
        window_pdf_to_word.geometry(f"347x47+{center_x - int(window_width / 2)}+{center_y - int(window_height / 2)}")

        # Устанавливаем стиль оформления
        style = ttk.Style(window_pdf_to_word)
        style.theme_use("vista")

        # Определяем цвета для кнопок
        style.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        # функция для открытия диалогового окна выбора PDF-файла
        def choose_pdf():
            pdf_button.config(text='Выбрать PDF файл', state="disabled")
            convert_button.config(text='Конвертировать', state="disabled")
            filename = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"),))
            pdf_path.set(filename)

            pdf_file_3 = pdf_path.get()

            if pdf_file_3:
                pdf_button.config(text='Выбрать PDF файл', state="normal")
                convert_button.config(text='Конвертировать', state="normal")
            else:
                pdf_button.config(state="normal")
                convert_button.config(state="disabled")

        # функция для конвертации PDF в Word
        def convert_pdf():
            pdf_file = pdf_path.get()
            if pdf_file:
                # блокировка кнопок на время выполнения конвертации
                pdf_button.config(text='Подождите, идет', state="disabled")
                convert_button.config(text='конвертация', state="disabled")

                # задаем имя для конвертированного файла
                word_file = pdf_file.split('.')[0] + '.docx'

                # вызываем функцию конвертации из библиотеки pdf2docx
                pdf2docx.parse(pdf_file, word_file)
                messagebox.showinfo('Успех', 'Конвертация завершена!', parent=window_pdf_to_word)

                # разблокировка кнопок на время выполнения конвертации
                pdf_button.config(text='Выбрать PDF файл', state="normal")
                convert_button.config(text='Конвертировать', state="disabled")
                
                # открытие пути к сконвертированному файлу
                dir_path = os.path.dirname(pdf_file)
                os.startfile(dir_path)
            else:
                convert_button.config(text='Конвертировать', state="disabled")
                messagebox.showerror('Ошибка', 'Выберите PDF файл', parent=window_pdf_to_word)

        def thread_convert_pdf():
            threading.Thread(target=convert_pdf).start()

        # переменная для хранения пути к PDF-файлу
        pdf_path = tk.StringVar()

        # Кнопка для выбора файла
        pdf_button = ttk.Button(window_pdf_to_word, text='Выбрать PDF файл', command=choose_pdf, style='Custom.TButton')
        pdf_button.config(state='normal')
        pdf_button.grid(column=0, row=0)

        # Кнопка для конвертации
        convert_button = ttk.Button(window_pdf_to_word, text='Конвертировать', command=thread_convert_pdf, style='Custom.TButton')
        convert_button.grid(column=1, row=0)

        pdf_file_2 = pdf_path.get()

        if pdf_file_2:
            pdf_button.config(text='Выбрать PDF файл', state="normal")
            convert_button.config(text='Конвертировать', state="normal")
        else:
            convert_button.config(text='Конвертировать', state="disabled")

        # запускаем главный цикл окна приложения
        window_pdf_to_word.mainloop()

    def Weather():
        global window_weather
        def get_weather(*args):
            global treeview

            try:
                treeview.destroy()
            except NameError:
                pass
            except TclError:
                pass

            # Одна точка
            label_weather.config(text="Загрузка погоды.", fg="black")
            window_weather.update()

            city = edit_city.get()
            api_key = "26aecdf5b56cf2b82e37bdac6985cff6"
            geocode_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
            response = requests.get(geocode_url)
            if city == "":
                label_weather.config(text="Вы не ввели город", fg="red")
            elif response.status_code == 200:
                location_data = response.json()
                if location_data:
                    
                    # Две точки
                    label_weather.config(text="Загрузка погоды..", fg="black")
                    window_weather.update()

                    lat = location_data[0]["lat"]
                    lon = location_data[0]["lon"]
                    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={api_key}&lang=ru"
                    response = requests.get(url)
                    if response.status_code == 200:
                        
                        # Три точки
                        label_weather.config(text="Загрузка погоды...", fg="black")
                        window_weather.update()

                        weather_data = response.json()
                        forecast = ''

                        # Создаем фрейм с Treeview и заголовками столбцов
                        treeview = ttk.Treeview(window_weather)
                        treeview['columns'] = ['weather', 'temp_min', 'temp_max', 'feels_like', 'pressure', 'humidity', 'wind_speed']
                        treeview.heading('#0', text='День')
                        treeview.heading('weather', text='Погода')
                        treeview.heading('temp_min', text='Мин. темп., °C')
                        treeview.heading('temp_max', text='Макс. темп., °C')
                        treeview.heading('feels_like', text='Ощущается, °C')
                        treeview.heading('pressure', text='Давление, мм рт. ст.')
                        treeview.heading('humidity', text='Влажность, %')
                        treeview.heading('wind_speed', text='Скорость ветра, м/с')

                        treeview.column('#0', width=100)
                        treeview.column('weather', width=150)
                        treeview.column('temp_min', width=100)
                        treeview.column('temp_max', width=100)
                        treeview.column('feels_like', width=100)
                        treeview.column('pressure', width=120)
                        treeview.column('humidity', width=100)
                        treeview.column('wind_speed', width=120)

                        treeview.pack(side='bottom')

                        label_weather.config(text="", fg="black")

                        # Добавляем строки с данными
                        for day in weather_data["daily"]:
                            timestamp = day["dt"]
                            date = datetime.datetime.fromtimestamp(timestamp)
                            day_of_week = date.strftime("%A").replace("Monday", "Понедельник").replace("Tuesday", "Вторник").replace("Wednesday", "Среда").replace("Thursday", "Четверг").replace("Friday", "Пятница").replace("Saturday", "Суббота").replace("Sunday", "Воскресенье")
                            weather = day["weather"][0]["description"]
                            temp_min = round(day["temp"]["min"] - 273.15, 1)
                            temp_max = round(day["temp"]["max"] - 273.15, 1)
                            feels_like = round(day["feels_like"]["day"] - 273.15, 1)
                            pressure = round(day["pressure"] * 0.750062, 1)
                            humidity = day["humidity"]
                            wind_speed = round(day["wind_speed"], 1)
                            treeview.insert('', 'end', text=day_of_week, values=(weather, f"{temp_min:.1f}", f"{temp_max:.1f}", f"{feels_like:.1f}", f"{pressure:.1f}", f"{humidity} %", f"{wind_speed} м/с"))
                        treeview.pack(pady=10)
                    else:
                        label_weather.config(text="Не удалось получить прогноз погоды\n", fg="black")
                        label_weather.config(text=label_weather.cget("text") + "Проверьте доступ в интернет", fg="red")
                else:
                    label_weather.config(text="Не удалось найти координаты города\n", fg="black")
                    label_weather.config(text=label_weather.cget("text") + "Проверьте правильность написания города", fg="red")
            else:
                label_weather.config(text="Не удалось найти город\n", fg="black")
                label_weather.config(text=label_weather.cget("text") + "Попробуйте снова нажать кнопку или проверьте правильность написания города", fg="red")

        def exit_window_weather():
            try:
                window_other_menu.deiconify()
                window_weather.destroy()
                window_weather.quit()
            except NameError:
                window.deiconify()
                window_weather.destroy()
                window_weather.quit()
            except TclError:
                window.deiconify()
                window_weather.destroy()
                window_weather.quit()

        def select_city(event):
            value = event.widget.get()
            var_city.set(value)

        def update_combobox(*args):
            # Обновляем значения в комбобоксе и получаем значение из поля ввода
            current_text = edit_city.get().lower()

            # Фильтруем список городов по значению в поле ввода
            filtered_cities = [city for city in cities if current_text in city.lower()]

            # Обновляем значения в выпадающем списке
            combobox_city['values'] = filtered_cities

        def on_mousewheel(event):
            try:
                combobox_city.yview_scroll(int(-1*(event.delta/120)), "units")
            except AttributeError:
                pass

        # Создаем список городов
        cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты', 'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск',
'Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово', 'Белогорск', 'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан', 'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук', 'Буйнакск', 
'Великие Луки', 'Великий Новгород', 'Верхняя Пышма', 'Видное', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжск', 'Волжский', 'Вологда', 'Вольск', 'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Выборг', 'Выкса', 'Вязьма,' 
'Гатчина', 'Геленджик', 'Георгиевск', 'Глазов', 'Горно-Алтайск', 'Грозный', 'Губкин', 'Гудермес', 'Гуково', 'Гусь-Хрустальный', 
'Дербент', 'Дзержинск', 'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна', 
'Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки', 
'Железногорск', 'Жигулевск', 'Жуковский',
'Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст', 
'Иваново', 'Ивантеевка', 'Ижевск, Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай', 
'Йошкар-Ола',
'Казань', 'Калининград', 'Калуга', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск', 'Каспийск', 'Кемерово', 'Керчь', 'Кинешма', 'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск', 'Клин', 'Клинцы', 'Ковров', 'Когалым', 'Коломна', 'Комсомольск-на-Амуре', 'Копейск', 'Королев', 'Кострома', 'Котлас', 'Красногорск', 'Краснодар', 'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск', 'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк', 'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл', 'Лабинск', 
'Лениногорск', 'Ленинск-Кузнецкий', 'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва', 'Лыткарино', 'Люберцы', 
'Магадан', 'Магнитогорск', 'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные Воды', 'Минусинск', 'Михайловка', 'Михайловск', 'Мичуринск', 'Москва', 'Мурманск', 'Муром', 'Мытищи', 
'Набережные Челны', 'Назарово', 'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находка', 'Невинномысск', 'Нерюнгри', 'Нефтекамск', 'Нефтеюганск', 'Нижневартовск', 'Нижнекамск', 'Нижний Новгород', 'Нижний Тагил', 'Новоалтайск', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк', 'Новоуральск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Уренгой', 'Ногинск', 'Норильск', 'Ноябрьск', 'Нягань', 
'Обнинск', 'Одинцово', 'Озерск', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево', 'Орск', 
'Павлово', 'Павловский Посад', 'Пенза', 'Первоуральск', 'Пермь', 'Петрозаводск', 'Петропавловск-Камчатский', 'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино', 'Пятигорск', 
'Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Рубцовск', 'Рыбинск', 'Рязань', 
'Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Свободный', 'Севастополь', 'Северодвинск', 'Северск', 'Сергиев Посад', 'Серов', 'Серпухов', 'Сертолово', 'Сибай', 'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск', 'Сосновый Бор', 'Сочи', 'Ставрополь', 'Старый Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань', 'Сыктывкар', 
'Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тольятти', 'Томск', 'Троицк', 'Туапсе', 'Туймазы', 'Тула', 'Тюмень', 
'Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан', 'Усолье-Сибирское', 'Уссурийск', 'Усть-Илимск', 'Уфа', 'Ухта', 
'Феодосия', 'Фрязино', 
'Хабаровск', 'Ханты-Мансийск', 'Хасавюрт', 'Химки', 
'Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово', 'Череповец', 'Черкесск', 'Черногорск', 'Чехов', 'Чистополь', 'Чита', 
'Шадринск', 'Шали', 'Шахты', 'Шуя', 
'Щекино', 'Щелково',
'Электросталь', 'Элиста', 'Энгельс', 
'Южно-Сахалинск', 'Юрга, Якутск',
'Ялта', 'Ярославль']

        try:
            window_other_menu.withdraw()
        except NameError:
            window.withdraw()
        except TclError:
            window.deiconify()

        window_weather = tk.Tk()
        window_weather.title("Погода")
        window_weather.resizable(width=False, height=False)
        window_weather.config(bg="#DFE4E2")
        window_weather.protocol('WM_DELETE_WINDOW', exit_window_weather)

        # получаем размер экрана
        screen_width = window_weather.winfo_screenwidth()
        screen_height = window_weather.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_weather.geometry(f"900x373+{center_x-500}+{center_y-300}")

        style_weather_menu = ttk.Style(window_weather)
        style_weather_menu.theme_use('vista')
        style_weather_menu.configure("Custom.TButton", background="#4CAF50", foreground="black", font="Arial 17 bold")

        font = 'Arial 15'

        # Создаем виджеты
        label_city = ttk.Label(window_weather, text="Введите город", style='Custom.TButton')
        label_city.place(x=250, y=10)

        label_weather = tk.Label(window_weather, font=("Arial", 14), bg="#DFE4E2")
        label_weather.place(x=350, y=200)

        combobox_label = ttk.Label(window_weather, text="Выберите город", style='Custom.TButton')
        combobox_label.place(x=450, y=10)

        # Создаем выпадающий список
        var_city = tk.StringVar()

        # Задаем первый элемент списка как значение по умолчанию
        var_city.set(cities[0])

        combobox_city = ttk.Combobox(window_weather, font=('Arial 17'), style='Custom.TButton', textvariable=var_city)
        combobox_city.place(x=450, y=50, width=199)

        combobox_city.bind("<Return>", get_weather)
        combobox_city.bind('<KeyRelease>', update_combobox)
        combobox_city.bind("<MouseWheel>", on_mousewheel)
        combobox_city.bind("<<ComboboxSelected>>", select_city)

        var_city.set(combobox_city.get())

        # Список вариантов для комбобокса
        combobox_city['values'] = cities

        # Кнопка получения погоды
        button_weather = ttk.Button(window_weather, text="Получить погоду", command=get_weather, style='Custom.TButton')
        button_weather.place(x=250, y=90, width=399)

        # Поле для ввода города
        edit_city = ttk.Entry(window_weather, font=('Arial 17'), textvariable=var_city, style='Custom.TButton', justify='center')
        edit_city.place(x=250, y=50, width=180)
        edit_city.bind("<Return>", get_weather)
        edit_city.bind('<KeyRelease>', update_combobox)

        # Запускаем главный цикл приложения
        window_weather.mainloop()

    # Новости
    def News():
        global window_news
        # Определить функцию для получения новостей
        def get_news():
            nonlocal news_list
            # Очистить список новостей
            news_list.delete(0, tk.END)
            # Создать окно загрузки
            loading_window = Tk()
            loading_window.title("Загрузка...")
            loading_window.resizable(width=False, height=False)
            loading_label = tk.Label(loading_window, text="Идет загрузка новостей, пожалуйста, подождите...")
            loading_label.pack(pady=10)
            loading_window.update()

            # получаем размер экрана
            screen_width = loading_window.winfo_screenwidth()
            screen_height = loading_window.winfo_screenheight()

            # вычисляем координаты центра экрана
            center_x = int(screen_width / 2)
            center_y = int(screen_height / 2)

            loading_window.geometry(f"300x140+{center_x-200}+{center_y-200}")

            # URL сайта TASS, который нужно спарсить
            url = "https://tass.ru/rss/v2.xml"

            # Запросить XML содержимое сайта
            response = requests.get(url)
            xml_content = response.content

            # Разобрать XML содержимое с помощью BeautifulSoup
            soup = BeautifulSoup(xml_content, "xml")

            # Найти заголовки и ссылки всех статей
            articles = soup.find_all("item")

            # Перебрать статьи и добавить в список новостей
            for article in articles:
                headline = article.find("title").text
                link = article.find("link").text
                news_list.insert(tk.END, headline)
                news_list.insert(tk.END, "\n")
                # Сохранить ссылку на статью в список ссылок
                news_links.append(link)

            # Закрыть окно загрузки
            loading_window.destroy()

        def exit_window_news():
            try:
                window_other_menu.deiconify()
                window_news.destroy()
                window_news.quit()
            except NameError:
                window.deiconify()
                window_news.destroy()
                window_news.quit()
            except TclError:
                window.deiconify()
                window_news.destroy()
                window_news.quit()

        try:
            window_other_menu.withdraw()
        except NameError:
            window.withdraw()
        except TclError:
            window.deiconify()

        window_news = tk.Tk()
        window_news.resizable(width=False, height=False)
        window_news.title("Новости")
        window_news.protocol('WM_DELETE_WINDOW', exit_window_news)

        # получаем размер экрана
        screen_width = window_news.winfo_screenwidth()
        screen_height = window_news.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_news.geometry(f"900x420+{center_x-500}+{center_y-300}")

        style_news = ttk.Style(window_news)
        style_news.theme_use('vista')
        style_news.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        # Создать кнопку
        button = ttk.Button(window_news, text="Получить новости", command=get_news, style='Custom.TButton')
        button.pack()

        # Создать список для отображения новостей
        news_list = tk.Listbox(window_news, width=100, height=20, font=('Arial 12'))
        news_list.pack(pady=10)

        # Создать список ссылок на новости
        news_links = []

        # Создать функцию для открытия ссылки новости в браузере
        def open_link(event):
            if news_list.curselection() and news_links:
                url = news_links[news_list.curselection()[0]]
                webbrowser.open(url)

        # Привязать функцию к событию нажатия на список новостей
        news_list.bind("<Double-Button-1>", open_link)

        # Запустить главный цикл обработки событий Tkinter
        window_news.mainloop()

    # Игры
    global window_other_menu
    # Игра виселица
    def update_remaining_label():
        global remaining_label
        remaining = len(secret_word) - len(set(guessed_letters).intersection(set(secret_word)))
        remaining_label.configure(text=f"Осталось неразгаданных букв: {remaining}")

    def update_word_label():
        global word_label
        word_state = "".join([c if c in guessed_letters else "_" for c in secret_word])
        word_label.configure(text=f"Слово: {word_state}")

    def update_attempts_label():
        global attempts_label
        attempts_label.configure(text=f"Осталось попыток: {num_attempts}")

    def guess_letter():
        global guessed_letters, num_attempts, guess_letter, letter
        letter = letter_entry.get().lower()
        if letter in guessed_letters:
            letter_entry.delete(0, END)
            show_message("Вы уже угадали эту букву. Попробуйте другую.")
        elif letter in secret_word:
            guessed_letters.add(letter)
            update_word_label()
            update_remaining_label()
            if all([c in guessed_letters for c in secret_word]):
                show_message(f"Поздравляем! Вы угадали слово '{secret_word}'!")
                new_game()
        else:
            num_attempts -= 1
            update_attempts_label()
            if num_attempts == 0:
                show_message(
                    f"Извините, вы израсходовали все попытки. Слово было '{secret_word}'. Удачи в следующий раз!")
                new_game()
        letter_entry.delete(0, tk.END)
        letter_entry.focus_set()

    def show_message(message):
        tk.messagebox.showinfo("Игра 'Виселица'", message, parent=window_widgets_viselica)

    def get_secret_word():
        words = ["яблоко", "банан", "апельсин", "груша", "персик", "ананас", "слива", "виноград", "манго", "киви", "абрикос",
                    "мандарин", "грейпфрут", "лайм", "лайчи", "нектарин", "папайя", "слизень", "бамбук", "коала", "бублик", "вертолет",
                    "корабль", "самолет", "карандаш", "книга", "микроскоп", "компьютер", "автомобиль", "оладушек", "домино", "луна",
                    "треугольник", "железо", "дракон", "солнце", "радуга", "пароход", "водопад", "гитара", "виолончель", "саксофон",
                    "горшок", "гамак", "воздушный шар", "крокодил", "стекло", "молоток", "микрофон", "снеговик", "кашалот", "креветка",
                    "барсук", "краб", "сардинка", "коньки", "кактус", "каштан", "фотоаппарат", "рюкзак", "канат", "ракета", "самовар",
                    "кокос", "камера", "космонавт", "бомба", "банк", "бухта", "ворона", "гусеница", "дельфин", "дерево", "диск", "ежик",
                    "жираф", "змея", "зонт", "иголка", "кабан", "календарь", "капуста", "клавиатура", "клюшка", "колесо", "колонка",
                    "комод", "коробка", "косичка", "лампочка", "лифт", "лужа", "лук", "маяк", "мармелад", "мартышка", "метла", "муравей",
                    "музыка", "мыло", "мышь", "ножницы", "носок", "ноутбук", "олень", "орел", "паук", "палец", "парашют", "педаль", "печенье",
                    "пилот", "пистолет", "пицца", "подушка", "поезд", "попугай", "пружина", "пылесос", "радио", "резинка", "розетка", "рубашка",
                    "рыба", "салат", "салют", "самокат", "макарон", "картина", "молоко", "флейта", "галстук", "шоколад", "кошелек", "метро", 
                    "бейсбол", "фонарь", "бутылка", "зонтик", "пианино", "камень", "ковер", "кровать", "душ", "кольцо", "картошка", "пыль", 
                    "кресло", "диван", "зеркало", "конфета", "мороженое", "лимонад", "рыцарь", "бинокль", "клавиша", "лента", "телефон", 
                    "мыльница", "шарф", "перо", "медведь", "сковорода", "вилка", "ложка", "нож", "пила", "стул", "табурет", "ковш", "карантин", 
                    "горшочек", "крючок", "веревка", "костюм", "трусы", "галочка", "крючок", "шторы", "часы", "шампунь", "ластик", "бумага", 
                    "чашка", "сумка", "банка", "дверь", "окно", "полотенце", "море", "небо", "трава", "солнце", "медаль", "котелок", "футбол", 
                    "змейка", "кошка", "попкорн", "скрипка", "муха", "свеча", "песок", "майка", "бокал", "горшок", "сумочка", "курица", "книжка", 
                    "ручка", "свитер", "забор", "ваза", "морковь", "динозавр", "бегемот", "овца", "орех", "тапки", "кот", "пес", "крокус", "мак", 
                    "краски", "кисть", "метка", "листок", "ручей", "океан", "ящик", "роза", "бабочка", "змея", "деревня", "молоток", "жаба", "вода", 
                    "мука", "торт", "сок", "пиво", "аптечка", "щетка", "морс", "капли", "принцесса", "космос", "футляр", "персона", "кондиционер", 
                    "вазон", "чехол", "велосипед", "плащ", "сапоги", "куртка", "шапка", "воздух", "золото", "метеорит", "радость", "гитарист", "конь"]

        return random.choice(words)

    def new_game():
        global secret_word, guessed_letters, num_attempts
        secret_word = get_secret_word()
        guessed_letters = set()
        num_attempts = 15
        update_word_label()
        update_remaining_label()
        update_attempts_label()

    def create_widgets():
        global word_label, attempts_label, letter_entry, new_game, remaining_label, window_widgets_viselica
        def exit_back_viselica_menu():
            try:
                window_game_menu.deiconify()
                window_widgets_viselica.destroy()
            except NameError:
                window.deiconify()
                window_widgets_viselica.destroy()
            except TclError:
                window.deiconify()
                window_widgets_viselica.destroy()
                window_widgets_viselica.quit()

        try:
            window_game_menu.withdraw()
        except NameError:
            pass
        except TclError:
            window_widgets_viselica.destroy()
            window_widgets_viselica.quit()

        window_widgets_viselica = Tk()
        window_widgets_viselica.title('Отгадай слово')
        window_widgets_viselica.resizable(width=False, height=False)
        window_widgets_viselica.protocol('WM_DELETE_WINDOW', exit_back_viselica_menu)

        # получаем размер экрана
        screen_width = window_widgets_viselica.winfo_screenwidth()
        screen_height = window_widgets_viselica.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_widgets_viselica.geometry(f"580x250+{center_x-280}+{center_y-200}")

        style_viselica = ttk.Style(window_widgets_viselica)
        style_viselica.theme_use("vista")
        style_viselica.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        # Отображение загаданного слова
        word_label = ttk.Label(window_widgets_viselica, text=" ", style="Custom.TButton")
        word_label.grid(row=0, column=0)

        # Создание label для отображения количества неразгаданных букв
        remaining_label = ttk.Label(window_widgets_viselica, text="Осталось неразгаданных букв: 0", style='Custom.TButton')
        remaining_label.grid(row=0, column=1)

        def validate_entry(text):
            return len(text) <= 1

        # Поле для ввода буквы
        letter_entry = EntryWithPlaceholder(window_widgets_viselica, font=('Arial 16'), placeholder="Пишите здесь...", validate="key")
        letter_entry.grid(row=1, column=0, padx=10, pady=10)
        letter_entry.focus()
        vcmd = (window_widgets_viselica.register(validate_entry), '%P')
        letter_entry.configure(validatecommand=vcmd)

        # Проверка символа в поле ввода и ограничение поля ввода до 1 символа
        def guess_letter_2():
            letter = letter_entry.get()
            if len(letter) == 0:
                guess_letter()
                letter_entry.delete(0, END)
                messagebox.showerror("Ошибка", "Нельзя проверить букву, которой нет в поле ввода", parent=window_widgets_viselica)
                window_widgets_viselica.focus_force()
                letter_entry.focus()
            elif len(letter) == 1:
                guess_letter()
                letter_entry.insert(len(letter_entry.get()) // 2, letter)
                letter_entry.delete(0, END)

        def guess_letter_enter(Return):
            letter = letter_entry.get()
            if len(letter) == 0:
                guess_letter()
                letter_entry.delete(0, END)
                messagebox.showerror("Ошибка", "Нельзя проверить букву, которой нет в поле ввода", parent=window_widgets_viselica)
                window_widgets_viselica.focus_force()
                letter_entry.focus()
            elif len(letter) == 1:
                guess_letter()
                letter_entry.insert(len(letter_entry.get()) // 2, letter)
                letter_entry.delete(0, END)

        guess_button = ttk.Button(window_widgets_viselica, text="Угадать", command=guess_letter_2, style='Custom.TButton')
        guess_button.grid(row=1, column=1, padx=10, pady=10)

        # Отображение оставшихся попыток
        attempts_label = ttk.Label(window_widgets_viselica, style='Custom.TButton')
        attempts_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Кнопка для начала новой игры
        new_game_button = ttk.Button(window_widgets_viselica, text="Новая игра", command=new_game, style='Custom.TButton')
        new_game_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Создание новой игры
        new_game()

        window_widgets_viselica.bind("<Return>", guess_letter_enter)

    # Поиск игр
    def find_game():
        global find_game_window
        def closing_find_game():
            try:
                window_other_menu.deiconify()
                find_game_window.destroy()
                find_game_window.quit()
            except NameError:
                window.deiconify()
                find_game_window.destroy()
                find_game_window.quit()
            except TclError:
                window.deiconify()
                find_game_window.destroy()
                find_game_window.quit()

        try:
            window_other_menu.withdraw()
        except NameError:
            pass
        except TclError:
            window_other_menu.quit()
            find_game_window.quit()

        def search_game():
            game_name = game_name_entry.get()
            url = f"https://iwillplay.ru/games?search={quote(game_name)}"
            try:
                response = requests.get(url)
                response.raise_for_status() # проверка на ошибки
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Ошибка", f"Ошибка при выполнении запроса: {e}", parent=find_game_window)
                return
            soup = BeautifulSoup(response.content, "html.parser")
            results = soup.find_all("div", class_="iwp-card-body mt-3")
            game_list.delete(*game_list.get_children())
            for result in results:
                game_name = result.find("h6", class_="text-dark mb-1").text.strip()
                price = result.find("span", class_="text-dark").text.strip()
                game_link = result.find("a")
                if game_link:
                    parsed_url = urlparse(game_link["href"])
                    game_slug = parsed_url.path.split("/")[-1]
                    game_url = f"https://iwillplay.ru/game/{game_slug}"
                    game_list.insert('', 'end', values=(game_name, price, game_url))
                else:
                    game_list.insert('', 'end', values=(game_name, price))

        def open_game(event):
            item = game_list.selection()[0]
            game_name = game_list.item(item)["values"][0]

            # заменяем пробелы на дефисы только в имени игры
            game_name = re.sub(r'-+', '-', game_name.replace(" ", "-").replace(":", "").replace(".", "").replace("&", "").replace(",", "-").replace("'", "-"))

            url = f"https://iwillplay.ru/game/{game_name}"
            webbrowser.open(url)

        def search_game_return(Return):
            search_game()

        # создаем окно приложения
        find_game_window = tk.Tk()
        find_game_window.title("Поиск игры")
        find_game_window.columnconfigure([0], weight=1, minsize=200)
        find_game_window.rowconfigure([0, 1, 2], weight=1, minsize=0)
        find_game_window.protocol('WM_DELETE_WINDOW', closing_find_game)
        find_game_window.resizable(width=False, height=False)

        # Вычисляем координаты центра экрана
        center_x = int(screen_width / 1.5)
        center_y = int(screen_height / 1.5)

        # Задаем размеры окна
        find_game_window.geometry(f"603x274+{center_x - int(window_width / 0.4)}+{center_y - int(window_height / 1.5)}")

        # Устанавливаем стиль оформления
        style = ttk.Style(find_game_window)
        style.theme_use("vista")

        # Определяем цвета для кнопок
        style.configure("Custom.TButton", background="#4CAF50", foreground="black", font="Arial 12 bold")
        style.configure("iwillplay.TButton", background="#4CAF50", foreground="green", font="Arial 12 bold")

        # создаем поле ввода
        game_name_entry = EntryWithPlaceholder(find_game_window, placeholder="Название игры...")
        game_name_entry.configure(font='Arial 15', width=15)
        game_name_entry.place(x=215, y=0)

        # создаем надпись "при поддержке iwillplay"
        find_game_label = ttk.Label(find_game_window, text='при поддержке iwillplay', style='iwillplay.TButton')
        find_game_label.grid(row=0, column=0)
        find_game_label.place(x=406, y=0)

        # создаем кнопку для поиска игры
        search_button = ttk.Button(find_game_window, text="Поиск", command=search_game, style='Custom.TButton')
        search_button.grid(row=0, column=0, columnspan=2)
        search_button.configure(width=21)
        search_button.place(x=0, y=0)

        # создаем виджет Treeview для отображения результатов
        cols = ("Название игры", "Цена")
        game_list = ttk.Treeview(find_game_window, columns=cols, show="headings")
        for col in cols:
            game_list.heading(col, text=col, anchor=tk.CENTER)
            game_list.column(col, width=300, anchor=tk.CENTER) # задаем ширину и выравнивание для колонки
        game_list.grid(row=3, column=0, columnspan=2, stick='wens')

        # привязываем обработчик события "double click" к виджету Treeview
        game_list.bind("<Double-1>", open_game)

        find_game_window.bind('<Return>', search_game_return)

        # запускаем главный цикл приложения
        find_game_window.mainloop()

    def main_menu_other():
        global window_game_menu
        def exit_back_game_menu():
            try:
                window_other_menu.deiconify()
                window_game_menu.destroy()
                window_game_menu.quit()
            except NameError:
                window.deiconify()
                window_game_menu.destroy()
                window_game_menu.quit()
            except TclError:
                window.deiconify()
                window_game_menu.destroy()
                window_game_menu.quit()

        try:
            window_other_menu.withdraw()
            window.withdraw()
        except NameError:
            pass
        except TclError:
            window.deiconify()


        window_game_menu = Tk()
        window_game_menu.title('Игры')
        window_game_menu.resizable(width=False, height=False)
        window_game_menu.columnconfigure([0], weight=1, minsize=150)
        window_game_menu.rowconfigure([0], weight=1, minsize=0)
        window_game_menu.protocol('WM_DELETE_WINDOW', exit_back_game_menu)

        # получаем размер экрана
        screen_width = window_game_menu.winfo_screenwidth()
        screen_height = window_game_menu.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_game_menu.geometry(f"150x40+{center_x-200}+{center_y-200}")

        #Устанавливаем стиль оформления
        style_game_menu = ttk.Style(window_game_menu)
        style_game_menu.theme_use("vista")
        style_game_menu.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        #Создаем кнопки
        button_window_game_1 = ttk.Button(window_game_menu, text='Отгадай слово', width=15, command=create_widgets, style='Custom.TButton')
        button_window_game_1.grid(column=0, row=0, sticky='wens')

        window_game_menu.mainloop()

    # Главное окно "Прочее"
    def parent_menu():
        global window_other_menu
        def exit_back_menu_other():
            try:
                window.deiconify()
                try:
                    only_speed_window.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_speed_test.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_pdf_to_word.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_weather.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_news.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_widgets_viselica.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_game_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_other_menu.destroy()
                    window_other_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
            except NameError:
                window.deiconify()
                try:
                    only_speed_window.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_speed_test.destroy()
                    window_speed_test.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_pdf_to_word.destroy()
                    window_pdf_to_word.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_weather.destroy()
                    window_weather.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_news.destroy()
                    window_news.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_widgets_viselica.destroy()
                    window_widgets_viselica.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_game_menu.destroy()
                    window_game_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_other_menu.destroy()
                    window_other_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
            except TclError:
                window.deiconify()
                try:
                    only_speed_window.destroy()
                    only_speed_window.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_speed_test.destroy()
                    window_speed_test.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_pdf_to_word.destroy()
                    window_pdf_to_word.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_weather.destroy()
                    window_weather.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_news.destroy()
                    window_news.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_widgets_viselica.destroy()
                    window_widgets_viselica.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_game_menu.destroy()
                    window_game_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
                try:
                    window_other_menu.destroy()
                    window_other_menu.quit()
                except NameError:
                    pass
                except TclError:
                    pass
        try:
            window.withdraw()
        except NameError:
            window.deiconify()
        except TclError:
            window.deiconify()

        window_other_menu = Tk()
        window_other_menu.title('Прочее')
        window_other_menu.resizable(width=False, height=False)
        window_other_menu.columnconfigure([0], weight=1, minsize=150)
        window_other_menu.rowconfigure([0,1,2,3,4,5], weight=1, minsize=0)
        window_other_menu.protocol('WM_DELETE_WINDOW', exit_back_menu_other)

        # получаем размер экрана
        screen_width = window_other_menu.winfo_screenwidth()
        screen_height = window_other_menu.winfo_screenheight()

        # вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        window_other_menu.geometry(f"230x230+{center_x-200}+{center_y-200}")

        style_other_menu = ttk.Style(window_other_menu)
        style_other_menu.theme_use("vista")
        style_other_menu.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")

        # Кнопки родительского окна
        button_window_other_menu_1 = ttk.Button(window_other_menu, text='Погода', width=20, command=Weather, style='Custom.TButton')
        button_window_other_menu_1.grid(column=0, row=0, sticky='wens')
        button_window_other_menu_2 = ttk.Button(window_other_menu, text='Новости', width=20, command=News, style='Custom.TButton')
        button_window_other_menu_2.grid(column=0, row=1, sticky='wens')
        button_window_other_menu_3 = ttk.Button(window_other_menu, text='PDF → Word', width=20, command=pdf_word_convert, style='Custom.TButton')
        button_window_other_menu_3.grid(column=0, row=2, sticky='wens')
        button_window_other_menu_4 = ttk.Button(window_other_menu, text='Игры', width=20, command=main_menu_other, style='Custom.TButton')
        button_window_other_menu_4.grid(column=0, row=3, sticky='wens')
        button_window_other_menu_5 = ttk.Button(window_other_menu, text='Скорость интернета', width=20, command=test_ethernet, style='Custom.TButton')
        button_window_other_menu_5.grid(column=0, row=4, sticky='wens')
        button_window_other_menu_6 = ttk.Button(window_other_menu, text='Поиск игр', width=20, command=find_game, style='Custom.TButton')
        button_window_other_menu_6.grid(column=0, row=5, sticky='wens')

        window.mainloop()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Главное окно поверх всех окон
    def on_top():
        window.attributes("-topmost", topmost.get())

    #При нажатии клавиши enter переходит в функцию files
    def press_enter(Return):
        files()

    #Функция горячих клавиш
    def files():
        global enter
        value = enter.get()

        # список горячих клавиш
        hotkeys = ['11', '111', '112', '113', '114', '1121', '1122', '1123', '1124',
        '12', '121', '122', '123', '124', '1221', '1222', '1223', '1224', '13', '14', '15', 
        '21', '22', '221', '222', '223', '23', '24', '25', '26', '27', 
        '31', '32', '33', '34', '35', '36', '37',
        '41', '411', '412', '413', '42',
        '51', '52', '53',
        '611', '612', '62', '71',
        '81', '82', '83', '84', '85', '86'] 

        # проверяем, соответствует ли введенная строка формату URL
        if re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', value):
            url = value
            webbrowser.open_new(url)
            enter.delete(0, END)
        elif value not in hotkeys:
            if '.' in value:  # если вводится имя сайта, а не запрос
                url = 'https://' + value
                enter.delete(0, END)
            else:
                url = 'https://www.google.com/search?q=' + value
            webbrowser.open_new(url)
            enter.delete(0, END)
        else:
            # введенная строка не является URL, выполняем запрос в командной строке
            subprocess.run(value, shell=True)
            enter.delete(0, END)

            # Питание ПК
            if value == '11':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.Power_off()
            elif value == '111':
                window.withdraw()
                enter.delete(0, END)
                os.system('shutdown /s /t 1 /f')
            elif value == '112':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.templates()
            elif value == '113':
                window.withdraw()
                enter.delete(0, END)
                os.system('shutdown -a')
            elif value == '114':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.Calc_sec()
            elif value == '1121':
                enter.delete(0, END)
                os.system('shutdown /s /t 1800 /f')
            elif value == '1122':
                enter.delete(0, END)
                os.system('shutdown /s /t 3600 /f')
            elif value == '1123':
                enter.delete(0, END)
                os.system('shutdown /s /t 5400 /f')
            elif value == '1124':
                enter.delete(0, END)
                os.system('shutdown /s /t 7200 /f')
            elif value == '12':
                window.withdraw()
                enter.delete(0, END)
                class_reboot.Reboot()
            elif value == '121':
                window.withdraw()
                enter.delete(0, END)
                os.system('shutdown /r /t 1 /f')
            elif value == '122':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.templates()
            elif value == '123':
                enter.delete(0, END)
                os.system('shutdown -a')
            elif value == '124':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.Calc_sec()
            elif value == '1221':
                enter.delete(0, END)
                os.system('shutdown /r /t 1800 /f')
            elif value == '1222':
                enter.delete(0, END)
                os.system('shutdown /r /t 3600 /f')
            elif value == '1223':
                enter.delete(0, END)
                os.system('shutdown /r /t 5400 /f')
            elif value == '1224':
                enter.delete(0, END)
                os.system('shutdown /r /t 7200 /f')
            elif value == '13':
                enter.delete(0, END)
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            elif value == '14':
                enter.delete(0, END)
                os.system('shutdown /l')
            elif value == '15':
                window.withdraw()
                enter.delete(0, END)
                menu_power_pc.Calc_sec()

            #браузер
            elif value == '21':
                enter.delete(0, END)
                func_browser.vk_and_youtube()
                enter.delete(0, END)
            elif value == '22':
                enter.delete(0, END)
                func_browser.vk()
            elif value == '221':
                webbrowser.open('https://vk.com/feed')
                enter.delete(0, END)
            elif value == '222':
                webbrowser.open('https://vk.com/im')
                enter.delete(0, END)
            elif value == '223':
                webbrowser.open('https://vk.com/id0')
                enter.delete(0, END)
            elif value == '23':
                enter.delete(0, END)
                func_browser.youtube()
            elif value == '24':
                enter.delete(0, END)
                func_browser.google_translate()
            elif value == '25':
                enter.delete(0, END)
                func_browser.google_disk()
            elif value == '26':
                enter.delete(0, END)
                func_browser.gmail() 
            elif value == '27':
                enter.delete(0, END)
                window.withdraw()
                func_browser.sites_open()

            # Система
            elif value == '31':
                enter.delete(0, END)
                system_windows.thread_cmds()
            elif value == '32':
                enter.delete(0, END)
                system_windows.autoloading()
            elif value == '33':
                enter.delete(0, END)
                system_windows.thread_regedit()
            elif value == '34':
                enter.delete(0, END)
                system_windows.thread_services()
            elif value == '35':
                enter.delete(0, END)
                system_windows.thread_appdata()
            elif value == '36':
                enter.delete(0, END)
                system_windows.thread_device_manager()
            elif value == '37':
                enter.delete(0, END)
                window.withdraw()
                system_windows.finish_process()

            # Автокликер
            elif value == '41':
                enter.delete(0, END)
                window.withdraw()
                status_on.window_menu()
            elif value == '411':
                enter.delete(0, END)
                window.withdraw()
                status_on.one_click_win()
            elif value == '412':
                enter.delete(0, END)
                window.withdraw()
                status_on.two_click_win()
            elif value == '413':
                enter.delete(0, END)
                window.withdraw()
                status_on.three_click_win()
            elif value == '42':
                enter.delete(0, END)
                window.withdraw()
                status_on.reference()

            # Починка ПК
            elif value == '51':
                enter.delete(0, END)
                window.withdraw()
                messagebox.showinfo('Предупреждение', 'Данная функция имеет всего одно окно', parent=None)
                FixPC.start_window_FixPC()
            elif value == '52':
                enter.delete(0, END)
                window.withdraw()
                messagebox.showinfo('Предупреждение', 'Данная функция имеет всего одно окно', parent=None)
                FixPC.start_window_FixPC()
            elif value == '53':
                enter.delete(0, END)
                window.withdraw()
                messagebox.showinfo('Предупреждение', 'Данная функция имеет всего одно окно', parent=None)
                FixPC.start_window_FixPC()

            # Рандомайзер
            elif value == '611':
                enter.delete(0, END)
                window.withdraw()
                withdraw_random_number()
            elif value == '612':
                enter.delete(0, END)
                window.withdraw()
                withdraw_generator_number()
            elif value == '62':
                enter.delete(0, END)
                heads_or_tails()

            # Настройки бота
            elif value == '71':
                enter.delete(0, END)
                window.withdraw()
                new_win()

            # Прочее
            elif value == '81':
                enter.delete(0, END)
                window.withdraw()
                Weather()
            elif value == '82':
                enter.delete(0, END)
                window.withdraw()
                News()
            elif value == '83':
                enter.delete(0, END)
                window.withdraw()
                pdf_word_convert()
            elif value == '84':
                enter.delete(0, END)
                window.withdraw()
                main_menu_other()
            elif value == '841':
                enter.delete(0, END)
                window.withdraw()
                create_widgets()
            elif value == '85':
                enter.delete(0, END)
                window.withdraw()
                test_ethernet()
            elif value == '86':
                enter.delete(0, END)
                window.withdraw()
                find_game()

            #Проверка ввода в поле
            elif not value:
                enter.delete(0, END)
                enter.insert(0, "Не введено число")
                enter.config(fg='red', font=('Arial', 12, 'bold'))
                button9.config(state='disabled')
                enter.config(state='disabled')
                enter.after(2000, lambda: reset_field(enter))
            else:
                enter.delete(0, END)
                enter.insert(0, "Введено неверное число")
                enter.config(fg='red', font=('Arial', 12, 'bold'))
                button9.config(state='disabled')
                enter.config(state='disabled')
                enter.after(2000, lambda: reset_field(enter))

            def reset_field(field):
                button9.config(state='normal')
                enter.config(state='normal')
                field.delete(0, END)
                field.config(fg='black', font=('Arial', 12, 'bold'))

    def hotkeys():
        window_hotkeys = Tk()
        window_hotkeys.title('Горячие клавиши')
        window_hotkeys.columnconfigure([0], weight=1, minsize=200)
        window_hotkeys.rowconfigure([0], weight=1, minsize=0)
        window_hotkeys.resizable(width=False, height=False)
        # Устанавливаем стиль оформления
        style_window_hotkeys = ttk.Style(window_hotkeys)
        style_window_hotkeys.theme_use("vista")

        # Определяем цвета для кнопок
        style_window_hotkeys.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 9 bold")
        style_window_hotkeys.configure("Label.TButton", background="#4CAF50", foreground="black", font='Arial 1 bold')

        # Горячие клавиши "Питание ПК"
        hotkeys_label_power_pc = ttk.Label(window_hotkeys, text='11 - Меню выключения ПК\n111 - Принудительное выключение ПК\n112 - Шаблоны выключения ПК\n113 - Отмена выключения ПК\n114 - Задать время выключения ПК\n1121 - Выключение ПК через 30 минут\n1122 - Выключение ПК через 1 час\n1123 - Выключение ПК через 1.5 часа\n1124 - Выключение ПК через 2 часа', style='Custom.TButton')
        hotkeys_label_reboot_pc = ttk.Label(window_hotkeys, text='12 - Меню перезагрузки ПК\n121 - Принудительная перезагрузка ПК\n122 - Шаблоны перезагрузки ПК\n123 - Отмена перезагрузки ПК\n124 - Задать время перезагрузки ПК\n1221 - Перезагрузка ПК через 30 минут\n1222 - Перезагрузка ПК через 1 час\n1223 - Перезагрузка ПК через 1.5 часа\n1224 - Перезагрузка ПК через 2 часа', style='Custom.TButton')
        hotkeys_label_hyber_and_logout = ttk.Label(window_hotkeys, text='13 - Гибернация ПК\n14 - Выход из системы\n15 - Задать время', style='Custom.TButton')

        # Отступ между строками
        hotkeys_label_enter_1_row = ttk.Label(window_hotkeys, style='Label.TButton')

        # Горячие клавиши "Браузер"
        hotkeys_label_browser_vk = ttk.Label(window_hotkeys, text='21 - Открыть "Вконтакте" и "YouTube"\n22 - Меню "Вконтакте"\n221 - Открыть "Моя страница" в "Вконтакте"\n222 - Открыть "Сообщения" в "Вконтакте"\n223 - Открыть "Моя страница" в "Вконтакте"', style='Custom.TButton')
        hotkeys_label_browser = ttk.Label(window_hotkeys, text='23 - Открыть "YouTube"\n24 - Открыть "Переводчик"\n25 - Открыть "Гугл диск"\n26 - Открыть "Gmail"\n27 - Менеджер сайтов', style='Custom.TButton')

        # Отступ между строками
        hotkeys_label_enter_2_row = ttk.Label(window_hotkeys, style='Label.TButton')

        # Горячие клавиши "Система"
        hotkeys_label_system = ttk.Label(window_hotkeys, text='31 - Открыть командную строку\n32 - Открыть папку автозагрузки\n33 - Открыть реестр\n34 - Открыть службы\n35 - Открыть appdata\n36 - Открыть диспетчер устройств\n37 - Завершить процесс приложения', style='Custom.TButton')
        # Горячие клавиши "Автокликер"
        hotkeys_label_autoclicker = ttk.Label(window_hotkeys, text='41 - Меню автокликера\n411 - Один клик в секунду\n412 - Два клика в секунду\n413 - Три кликa в секунду\n42 - Справка об автокликере', style='Custom.TButton')
        # Горячие клавиши "Рандомайзер"
        hotkeys_label_randomizer = ttk.Label(window_hotkeys, text='611 - Случайное число от 1 до 100\n612 - Генератор чисел\n62 - Орел или решка', style='Custom.TButton')

        # Отступ между строками
        hotkeys_label_enter_3_row = ttk.Label(window_hotkeys, style='Label.TButton')

        # Горячие клавиши "Настройки бота"
        hotkeys_label_setting_bot = ttk.Label(window_hotkeys, text='71 - Автозагрузка бота', style='Custom.TButton')

        # Отступ между строками
        hotkeys_label_enter_4_row = ttk.Label(window_hotkeys, style='Label.TButton')

        # Горячие клавиши "Прочее"
        hotkeys_label_other = ttk.Label(window_hotkeys, text='81 - Погода\n82 - Новости\n83 - PDF → WORD\n84 - Игры\n841 - Игра "Отгадай слово"\n85 - Проверка скорости интернета\n86 - Поиск игр по минимальным ценам', style='Custom.TButton')

        # Положение "Питание ПК"
        hotkeys_label_power_pc.grid(column=0, row=0, stick='wens')
        hotkeys_label_reboot_pc.grid(column=1, row=0, stick='wens')
        hotkeys_label_hyber_and_logout.grid(column=2, row=0, stick='wens')
        
        # Положение 1 отступа между строками
        hotkeys_label_enter_1_row.grid(column=0, row=1, columnspan=3, stick='wens')
        
        # Положение "Браузер"
        hotkeys_label_browser_vk.grid(column=0, row=2, stick='wens')
        hotkeys_label_browser.grid(column=1, row=2, columnspan=3, stick='wens')

        # Положение 2 отступа между строками
        hotkeys_label_enter_2_row.grid(column=0, row=3, columnspan=3, stick='wens')

        # Положение "Система"
        hotkeys_label_system.grid(column=0, row=4, stick='wens')
        # Положение "Автокликер"
        hotkeys_label_autoclicker.grid(column=1, row=4, stick='wens')
        # Положение "Рандомайзер"
        hotkeys_label_randomizer.grid(column=2, row=4, stick='wens')

        # Положение 3 отступа между строками
        hotkeys_label_enter_3_row.grid(column=0, row=5, columnspan=3, stick='wens')

        # Положение "Настройки бота"
        hotkeys_label_setting_bot.grid(column=0, row=6, stick='wens')
        # Положение "Прочее"
        hotkeys_label_other.grid(column=1, row=6, columnspan=3, stick='wens')

        # Положение 4 отступа между строками
        hotkeys_label_enter_4_row.grid(column=0, row=7, columnspan=3, stick='wens')

    def exit_bot():
        window.quit()

    def exit_bot_thread():
        try:
            threading.Thread(target=exit_bot).start()
        except RuntimeError:
            exit_bot()

    def resize_window(event=None):
        # Определяем минимальный размер окна, чтобы вместить все кнопки
        min_width = max(button.winfo_width() for button in buttons)
        min_height = sum(button.winfo_height() for button in buttons)

        # Получаем размер экрана
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Вычисляем размеры окна
        window_width = int(screen_width * 0.13)
        window_height = int(screen_height * 0.55)

        # Устанавливаем минимальный размер окна
        window.minsize(min_width, min_height)

        # Вычисляем координаты центра экрана
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)

        # Задаем размеры окна
        window.geometry(f"{window_width}x{window_height}+{center_x - int(window_width / 1.5)}+{center_y - int(window_height / 1.7)}")

    window = Tk()
    window.title('Бот-помощник')
    window.columnconfigure([0], weight=1, minsize=200)
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], weight=1, minsize=0)
    window.protocol('WM_DELETE_WINDOW', exit_bot_thread)
    window.resizable(width=False, height=False)

    # Получаем размер экрана
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)

    # Вычисляем размеры окна
    window_width = int(screen_width * 0.13)
    window_height = int(screen_height * 0.55)

    # Вычисляем координаты центра экрана
    center_x = int(screen_width / 2)
    center_y = int(screen_height / 2)

    # Задаем размеры окна
    window.geometry(f"{window_width}x{window_height}+{center_x - int(window_width / 1.5)}+{center_y - int(window_height / 1.7)}")

    # Устанавливаем стиль оформления
    style = ttk.Style(window)
    style.theme_use("vista")

    # Определяем цвета для кнопок
    style.configure("Custom.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 12 bold")
    style.configure("Custom2.TButton", background="#4CAF50", foreground="black", padding=10, font="Arial 11 bold")

    # Создаем кнопки с кастомным стилем
    buttons = []
    button1 = ttk.Button(window, text='Питание ПК', width=15, command=menu_power_pc.menu_pc, style="Custom.TButton")
    button2 = ttk.Button(window, text='Браузер', width=15, command=func_browser.menu, style="Custom.TButton")
    button3 = ttk.Button(window, text='Система', width=15, command=system_windows.menu, style="Custom.TButton")
    button4 = ttk.Button(window, text='Автокликер', width=15, command=status_on.window_menu, style="Custom.TButton")
    button5 = ttk.Button(window, text='Починка ПК', width=15, command=FixPC.start_window_FixPC, style="Custom.TButton")
    button6 = ttk.Button(window, text='Рандомайзер', width=15, command=menu, style="Custom.TButton")
    button7 = ttk.Button(window, text='Настройки бота', width=15, command=main_setting_bot, style="Custom.TButton")
    button8 = ttk.Button(window, text='Прочее', width=15, command=parent_menu, style="Custom.TButton")
    button9 = ttk.Button(window, text='Перейти', width=10, command=files, style='Custom.TButton')
    button10 = ttk.Button(window, text='Справка о горячих клавишах', width=10, command=hotkeys, style='Custom2.TButton')

    button1.grid(column=0, row=0, sticky='wens')
    button2.grid(column=0, row=1, sticky='wens')
    button3.grid(column=0, row=2, sticky='wens')
    button4.grid(column=0, row=3, sticky='wens')
    button5.grid(column=0, row=4, sticky='wens')
    button6.grid(column=0, row=5, sticky='wens')
    button7.grid(column=0, row=6, sticky='wens')
    button8.grid(column=0, row=7, sticky='wens')
    button9.grid(column=0, row=10, sticky='wens')
    button10.grid(column=0, row=11, sticky='wens')

    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    buttons.append(button4)
    buttons.append(button5)
    buttons.append(button6)
    buttons.append(button7)
    buttons.append(button8)
    buttons.append(button9)
    buttons.append(button10)

    # Привязываем обработчик событий изменения размеров окна
    window.bind("<Configure>", resize_window)

    #Нажатие клавиши "enter" переходит по введенной горячей клавише в функцию press_enter
    window.bind('<Return>', press_enter)

    # Создаем стиль оформления для чекбокса
    style_2 = ttk.Style()
    style_2.configure('my.TCheckbutton', font=('Arial', 14), background='white', foreground='black', padding=10)
    style_2.configure('my.TCheckbutton', width=20, height=20)

    # Создаем чекбокс с новым стилем
    topmost = BooleanVar()
    topmost.set(False)
    check = ttk.Checkbutton(window, text='Поверх всех окон', variable=topmost, onvalue=True, offvalue=False, command=on_top, style='my.TCheckbutton')
    check.grid(column=0, row=8, sticky='wens')

    #Поле ввода placeholder
    class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="Пишите здесь...", color='grey', *args, **kwargs):
            super().__init__(master, *args, **kwargs)
            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']
            self.bind("<FocusIn>", self._clear_placeholder)
            self.bind("<FocusOut>", self._add_placeholder)
            self._add_placeholder()

        def _clear_placeholder(self, event):
            if self['fg'] == self.placeholder_color:
                self.delete(0, END)
                self['fg'] = self.default_fg_color

        def _add_placeholder(self, event=None):
            if not self.get():
                self.insert(0, self.placeholder)
                self['fg'] = self.placeholder_color

    enter = EntryWithPlaceholder(window, font=('Arial', 12, 'bold'), placeholder="Введите что-либо...", width=30, justify='center')
    enter.grid(column=0, row=9)
    enter.focus()

    # Создаем список значений цветов в формате RGB (например, из файла)
    colors = [(18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (15, 21, 62), (15, 21, 62), (15, 21, 62), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (34, 26, 75), (73, 31, 98), (90, 34, 109), (83, 33, 105), (55, 28, 87), (26, 23, 69), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (34, 26, 75), (122, 40, 129), (199, 54, 177), (228, 59, 195), (237, 61, 201), (234, 60, 196), (217, 57, 188), (162, 47, 153), (70, 30, 96), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (15, 21, 62), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (17, 20, 63), (26, 23, 69), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (45, 26, 81), (172, 50, 160), (237, 61, 201), (240, 61, 202), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (240, 61, 202), (217, 57, 188), (98, 36, 114), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (29, 19, 91), (33, 19, 102), (22, 20, 75), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (17, 20, 63), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (162, 47, 153), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (240, 61, 202), (217, 57, 188), (73, 31, 98), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (37, 18, 112), (68, 12, 192), (73, 11, 204), (57, 14, 163), (23, 20, 78), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (90, 34, 109), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (237, 61, 201), (240, 61, 202), (172, 50, 160), (26, 23, 69), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (34, 26, 75), (73, 11, 204), (75, 10, 209), (75, 10, 209), (75, 10, 209), (47, 15, 141), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (26, 23, 69), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (162, 47, 153), (240, 61, 202), (237, 61, 201), (240, 61, 202), (237, 61, 201), (226, 67, 200), (237, 61, 201), (237, 61, 201), (237, 61, 201), (240, 61, 202), (240, 61, 202), (237, 61, 201), (210, 55, 192), (66, 27, 106), (47, 15, 141), (52, 15, 150), (29, 19, 91), (26, 20, 85), (57, 14, 163), (75, 10, 209), (75, 10, 209), (75, 10, 209), (75, 10, 209), (68, 12, 192), (29, 19, 91), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (26, 23, 69), (17, 20, 63), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (23, 20, 78), (195, 53, 174), (237, 61, 201), (240, 61, 202), (213, 76, 201), (107, 135, 202), (74, 158, 207), (151, 117, 212), (230, 66, 192), (235, 57, 184), (235, 57, 184), (200, 48, 201), (127, 26, 206), (102, 19, 206), (75, 10, 209), (75, 10, 209), (75, 10, 209), (68, 12, 192), (66, 12, 187), (73, 11, 204), (73, 11, 204), (75, 10, 209), (73, 11, 204), (75, 10, 209), (75, 10, 209), (42, 17, 125), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (17, 20, 63), (18, 26, 68), (18, 21, 64), (30, 28, 76), (34, 26, 75), (30, 28, 76), (30, 28, 76), (55, 28, 87), (203, 60, 185), (238, 66, 206), (213, 76, 201), (84, 146, 201), (71, 163, 219), (150, 141, 239), (184, 131, 248), (202, 102, 221), (212, 62, 164), (212, 62, 164), (166, 49, 174), (91, 26, 201), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (83, 19, 211), (62, 18, 157), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (26, 23, 69), (17, 20, 63), (17, 20, 63), (18, 36, 76), (62, 75, 136), (151, 117, 212), (171, 115, 219), (171, 115, 219), (171, 115, 219), (204, 123, 240), (215, 116, 236), (194, 73, 187), (103, 54, 192), (93, 36, 215), (101, 34, 217), (101, 34, 217), (86, 36, 183), (63, 50, 121), (48, 136, 166), (42, 166, 198), (42, 166, 198), (127, 126, 230), (204, 123, 240), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 112, 245), (179, 105, 247), (154, 66, 181), (66, 27, 106), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (26, 23, 69), (17, 20, 63), (17, 20, 63), (17, 20, 63), (16, 56, 92), (74, 158, 207), (77, 63, 207), (179, 105, 247), (189, 106, 255), (179, 105, 247), (147, 64, 220), (105, 19, 199), (75, 10, 209), (75, 10, 209), (66, 12, 187), (44, 15, 133), (23, 20, 78), (17, 20, 63), (16, 50, 87), (9, 150, 167), (0, 198, 204), (0, 198, 204), (151, 155, 241), (205, 137, 254), (205, 137, 254), (205, 137, 254), (205, 137, 254), (205, 137, 254), (207, 138, 255), (207, 138, 255), (195, 138, 251), (129, 88, 169), (43, 26, 77), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (14, 50, 85), (13, 127, 158), (40, 126, 202), (103, 54, 192), (68, 12, 192), (62, 12, 181), (62, 12, 181), (57, 14, 163), (42, 17, 125), (26, 20, 85), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 36, 76), (12, 91, 119), (10, 138, 158), (32, 130, 162), (129, 88, 169), (199, 88, 192), (208, 123, 238), (207, 138, 255), (207, 138, 255), (195, 138, 251), (152, 152, 241), (84, 146, 201), (18, 36, 76), (15, 21, 62), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (13, 55, 90), (14, 50, 85), (22, 20, 75), (22, 20, 75), (22, 20, 75), (26, 23, 69), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (60, 25, 79), (122, 40, 129), (108, 152, 219), (95, 167, 226), (59, 177, 217), (15, 188, 204), (14, 84, 114), (15, 21, 62), (15, 21, 62), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (15, 21, 62), (15, 21, 62), (18, 30, 71), (9, 132, 152), (0, 198, 204), (0, 198, 204), (9, 132, 152), (18, 30, 71), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (15, 21, 62), (15, 21, 62), (15, 21, 62), (18, 36, 76), (12, 102, 128), (12, 102, 128), (18, 36, 76), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 36, 76), (18, 30, 71), (17, 20, 63), (18, 30, 71), (18, 36, 76), (18, 30, 71), (16, 50, 87), (16, 48, 86), (16, 48, 86), (18, 30, 71), (18, 26, 68), (17, 44, 82), (17, 44, 82), (16, 50, 87), (18, 36, 76), (17, 44, 82), (14, 50, 85), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (14, 110, 135), (16, 56, 92), (17, 20, 63), (13, 96, 124), (10, 138, 158), (17, 44, 82), (12, 115, 139), (8, 145, 163), (14, 110, 135), (12, 102, 128), (14, 75, 107), (12, 115, 139), (10, 138, 158), (12, 115, 139), (14, 84, 114), (10, 138, 158), (11, 123, 146), (12, 91, 119), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (11, 123, 146), (15, 61, 96), (18, 36, 76), (10, 138, 158), (9, 150, 167), (14, 75, 107), (15, 66, 100), (12, 115, 139), (18, 36, 76), (9, 132, 152), (9, 132, 152), (14, 75, 107), (8, 151, 168), (12, 115, 139), (14, 75, 107), (8, 145, 163), (9, 132, 152), (12, 102, 128), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (12, 115, 139), (9, 132, 152), (12, 107, 133), (12, 115, 139), (14, 110, 135), (12, 107, 133), (15, 66, 100), (12, 102, 128), (17, 20, 63), (12, 102, 128), (9, 132, 152), (17, 44, 82), (9, 132, 152), (12, 115, 139), (14, 84, 114), (11, 123, 146), (12, 115, 139), (14, 84, 114), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 36, 76), (16, 48, 86), (17, 44, 82), (18, 30, 71), (18, 21, 64), (18, 36, 76), (18, 30, 71), (18, 36, 76), (18, 21, 64), (18, 30, 71), (18, 36, 76), (26, 23, 69), (17, 44, 82), (17, 44, 82), (18, 36, 76), (18, 36, 76), (18, 30, 71), (18, 36, 76), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (26, 23, 69), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (17, 20, 63), (17, 20, 63), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (26, 23, 69), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 26, 68), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), 
    (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64), (18, 21, 64)]

    # Получаем размеры изображения на основе количества значений цветов
    width = height = int(len(colors) ** 0.5)

    # Создаем новый объект изображения в библиотеке PIL
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            index = y * width + x
            if index < len(colors):
                pixels[x, y] = colors[index]

    # Создаем объект PhotoImage на основе изображения
    photo_image = ImageTk.PhotoImage(image)

    # Отображаем изображение в заголовке окна
    window.iconphoto(True, photo_image)

    window.mainloop()

is_admin()