import speech_recognition
import time
import pyautogui as pg
import os
import pyperclip
import webbrowser
from playsound import playsound
import pygetwindow as gw

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1.2
next_command = None
last = False
sounds = False
now = os.getcwd()
soob = False
words = ["сайт", "youtube", "на", "папку"]


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Не понял что вы сказали, Сэр."


def music(name):
    pyperclip.copy(name)
    webbrowser.open_new_tab("www.youtube.com\n")
    time.sleep(0.5)
    pg.moveTo(721, 115)
    time.sleep(2)
    pg.click()
    pg.hotkey("ctrl", "v")
    pg.hotkey(["enter"])
    time.sleep(1)
    pg.moveTo(594, 356)
    pg.click()

    print("Выполнено, Сэр.")


def soft(name):
    pyperclip.copy(name)
    pg.hotkey("winleft")

    pg.hotkey("ctrl", "v")
    pg.hotkey(["enter"])

    print("Есть, Сэр.")


def say(text):
    global sounds
    os.chdir(os.path.join(now, "sounds"))
    if text == "Досвидания, Сэр.":
        playsound("goodbuy.mp3")
    elif text == "Скриншот сделан, Сэр.":
        playsound("screenshot.mp3")
    elif text == "Папка создана":
        playsound("sozdana.mp3")
    elif text == "Папка удалена":
        playsound("udalena.mp3")
    elif text == "существует":
        playsound("uje.mp3")
    elif text == "извините":
        playsound("sorry.mp3")
    elif text == "название":
        playsound("nazvanie.mp3")
    elif text == "не существует":
        playsound("nes.mp3")
    elif text == "повтор":
        playsound("povtor.mp3")
    elif text == "откр":
        playsound("otkr.mp3")
    elif text == "добав":
        playsound("dobav.mp3")
    elif text == "есть":
        playsound("est.mp3")
    elif text == "прив":
        playsound("hi.mp3")
    elif text == "заг":
        playsound("zag.mp3")
    elif text == "все":
        playsound("vse.mp3")
    elif text == "сооб":
        playsound("soob.mp3")
    elif text == "отпр":
        playsound("otpr.mp3")


def main():
    global next_command
    global last
    global soob

    query = listen_command()

    if query.split()[0] == "открой" and query.split()[1] not in words:
        say("заг")
        soft(" ".join(query.split()[1:]))

    elif " ".join(query.split()[:2]) == "включи песню":
        say("заг")
        music(" ".join(query.split()[2:]))

    elif query == "сделай скриншот":
        os.chdir(now)
        pg.screenshot("screenshot.png")
        need = "\\"
        way = str(os.getcwd()) + need[0] + "screenshot.png"
        os.startfile(way)
        print("Скриншот сделан, Сэр.")
        say("Скриншот сделан, Сэр.")

    elif query == "конец работы":
        next_command = False

    elif query == "открой youtube":
        say("заг")
        webbrowser.open_new_tab("www.youtube.com\n")

    elif query == "выключи компьютер":
        os.system("shutdown /s /t 1")

    elif query == "перезагрузи компьютер":
        os.system("shutdown /r /t 1")

    elif " ".join(query.split()[:2]) == "создай папку":
        os.chdir(now)
        name = " ".join(query.split()[2:])
        try:
            os.mkdir(name)
            print(f"Папка '{name}' создана, Сэр.")
            say("Папка создана")

        except FileExistsError:
            print(f"Папка '{name}' уже существует, Сэр.")
            say("существует")

        except FileNotFoundError:
            print("Извините, не расслышал, Сэр.")
            say("извините")

    elif " ".join(query.split()[:2]) == "удали папку":
        os.chdir(now)
        name = " ".join(query.split()[2:])
        try:
            os.rmdir(" ".join(query.split()[2:]))
            print(f"Папка '{name}' удалена, Сэр.")
            say("Папка удалена")

        except FileNotFoundError:
            print("Такой папки не существует, Сэр.")
            say("не существует")

    elif " ".join(query.split()[:2]) == "открой папку":
        os.chdir(now)
        if " ".join(query.split()[2:]) != "":
            try:
                os.startfile(" ".join(query.split()[2:]))
                say("откр")
            except FileNotFoundError:
                print("Такой папки не существует, Сэр.")
                say("не существует")
        else:
            print("Извините, не расслышал, Сэр.")
            say("извините")

    elif " ".join(query.split()[:3]) == "измени имя папки":
        os.chdir(now)
        name_1 = ""
        count = 0
        for el in query.split()[3:]:
            if el != "на":
                name_1 += el + " "
                count += 1
            else:
                break
        name_2 = ""
        for el in query.split()[3 + count + 1:]:
            name_2 += el + " "
        try:
            os.rename(name_1[:-1], name_2[:-1])
            print(f"Название папки '{name_1}' было изменено на '{name_2}', Сэр.")
            say("название")

        except FileNotFoundError:
            print("Извините, не расслышал, Сэр.")
            say("извините")

    elif " ".join(query.split()[:2]) == "смени язык":
        pg.hotkey("alt", "shift")
        say("есть")

    elif " ".join(query.split()[:3]) == "уменьши громкость на":
        num = int(query.split()[-1])
        for i in range(num // 2):
            pg.press("volumedown")
        say("есть")

    elif " ".join(query.split()[:3]) == "увеличь громкость на":
        num = int(query.split()[-1])
        for i in range(num // 2):
            pg.press("volumeup")
        say("есть")

    elif " ".join(query.split()[:2]) == "закрой окно":
        pg.hotkey("alt", "f4")
        say("есть")

    elif " ".join(query.split()[:4]) == "открой на весь экран":
        pg.hotkey("winleft", "up")
        say("есть")

    elif " ".join(query.split()[:3]) == "сверни все окна":
        pg.hotkey("winleft", "d")
        say("есть")

    elif " ".join(query.split()[:3]) == "джарвис ты тут":
        say("все")

    elif " ".join(query.split()[:2]) == "напиши пользователю":
        if len(query.split()) == 2:
            say("извините")
        else:
            name = query.split()[2]
            pyperclip.copy(name)
            pg.hotkey("ctrl", "v")
            pg.hotkey(["enter"])
            say("сооб")
            soob = True

    elif query.split()[0] == "поиск":
        say("заг")
        pg.click(829, 120)
        pyperclip.copy(" ".join(query.split()[1:]))
        pg.hotkey("ctrl", "v")
        pg.hotkey(["enter"])

    elif query.split()[0] == "смена":
        say("есть")
        pg.keyDown("alt")
        pg.press("tab")
        pg.keyUp("alt")

    elif query.split()[0] == "закрыть":
        say("есть")
        pg.hotkey("ctrl", "w")

    elif query.split()[0] == "добавить":
        say("есть")
        pg.hotkey("ctrl", "t")

    elif " ".join(query.split()[:2]) == "сверни окно":
        say("есть")
        win = gw.getActiveWindow()
        if win:
            win.minimize()

    elif " ".join(query.split()[:2]) == "добавить задачу":
        os.chdir(now)
        with open("Список дел.txt", "a") as file:
            file.write(" ".join(query.split()[2:]) + "\n")
        say("добав")

    else:
        if not soob:
            if not last:
                print("Я не знаю такой команды, Сэр. Пожалуйста повторите попытку.")
                # say("повтор")
                last = True

    if query != "конец работы":
        next_command = True

    if " ".join(query.split()[:2]) != "напиши пользователю":
        if soob:
            pyperclip.copy(query)
            pg.hotkey("ctrl", "v")
            pg.hotkey(["enter"])
            say("отпр")
            soob = False


if __name__ == "__main__":
    say("прив")
    time.sleep(1)
    main()
    while next_command:
        main()
    print("Досвидания, Сэр.")
    say("Досвидания, Сэр.")
