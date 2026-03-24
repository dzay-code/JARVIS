import speech_recognition
import time
import pyautogui as pg
import os
import pyperclip
import webbrowser

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1
next_command = None
last = False


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Не понял что вы сказали, Сэр."


def music(*name):
    need = ""
    for el in name:
        need += el + " "
    pyperclip.copy(need)
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


def soft(*name):
    need = ""
    for el in name:
        need += el + " "
    pyperclip.copy(need)
    pg.hotkey("winleft")
    time.sleep(0.5)
    pg.hotkey("ctrl", "v")
    pg.hotkey(["enter"])
    time.sleep(0.5)

    print("Есть, Сэр.")


def website(*name):
    need = ""
    for el in name:
        need += el + " "
    pyperclip.copy(need)
    pg.hotkey("winleft")
    pg.typewrite("chrome\n")
    pg.hotkey(["enter"])
    time.sleep(1)
    pg.hotkey("ctrl", "v")
    pg.hotkey("enter")

    print("Да, Сэр.")


def main():
    global next_command
    global last

    query = listen_command()

    if " ".join(query.split()[:2]) == "открой сайт":
        website(*query.split()[2:])

    elif query.split()[0] == "открой" and query.split()[1] != "сайт" and query.split()[1] != "youtube" and query.split()[1] != "папку":
        soft(*query.split()[1:])

    elif " ".join(query.split()[:2]) == "включи песню":
        music(*query.split()[2:])

    elif query == "сделай скриншот":
        pg.screenshot("screenshot.png")
        need = "\\"
        way = str(os.getcwd()) + need[0] + "screenshot.png"
        os.startfile(way)
        print("Скриншот сделан, Сэр.")

    elif query == "конец работы":
        next_command = False

    elif query == "открой youtube":
        webbrowser.open_new_tab("www.youtube.com\n")

    elif query == "выключи компьютер":
        os.system("shutdown /s /t 1")

    elif query == "перезагрузи компьютер":
        os.system("shutdown /r /t 1")

    elif " ".join(query.split()[:2]) == "создай папку":
        name = " ".join(query.split()[2:])
        try:
            os.mkdir(name)
            print(f"Папка '{name}' создана, Сэр.")

        except FileExistsError:
            print(f"Папка '{name}' уже существует, Сэр.")

        except FileNotFoundError:
            print("Извините, не расслышал, Сэр.")

    elif " ".join(query.split()[:2]) == "удали папку":
        name = " ".join(query.split()[2:])
        try:
            os.rmdir(" ".join(query.split()[2:]))
            print(f"Папка '{name}' удалена, Сэр.")

        except FileNotFoundError:
            print("Извините, не расслышал, Сэр.")

    elif " ".join(query.split()[:2]) == "открой папку":
        if " ".join(query.split()[2:]) != "":
            os.startfile(" ".join(query.split()[2:]))
        else:
            print("Извините, не расслышал, Сэр.")

    elif " ".join(query.split()[:3]) == "измени имя папки":
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

        except FileNotFoundError:
            print("Извините, не расслышал, Сэр.")

    else:
        if not last:
            print("Я не знаю такой команды, Сэр. Пожалуйста повторите попытку.")
            last = True

    if query != "конец работы":
        next_command = True


if __name__ == "__main__":
    main()
    while next_command:
        main()
    print("Досвидания, Сэр.")
