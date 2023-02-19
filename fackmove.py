# 一个用来帮自己假装移动的小程序，故事起源于公司要求电脑每隔大概十分钟就会锁屏
# 所以写一个小程序，打包成 exe 文件，添加到快捷方式，就可以让 鼠标 假装在屏幕的右下方，随便动动、点点，而不会锁屏，
# 按 Esc 键就可以结束这个 fakemove。

# 名字的起源：可以假装我还在，免得电脑锁屏
from pynput import keyboard
from threading import Thread
import pyautogui as p
import time
import random

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':    # 让键盘敲 退出键的 时候，更改 线程的状态，然后退出
            main.status = 'exit'
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'run'
    while True:
        i, j = random.randint(1430, 1460), random.randint(1030, 1060)
        p.moveTo(i, j, duration = 1)
        p.click(i+1, j+1)
        if main.status == 'exit':
            break
            Thread.end()

Thread(target = main).start()
Thread(target = exit_program).start()
            

