from modules import GameEngine
import time
import logging
import keyboard

import mss

sct = mss.mss()

logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s",datefmt="%H:%M:%S")

with open("app.log", "w"):
    pass

game = GameEngine(sct=sct)

def loop(func,loop_count=5):
    count = 0
    global sct
    while True:
        if keyboard.is_pressed("F6"):
            sct.close()
            break
        count += 1
        logging.info(f"This is an info message: {count}")

        loop_time = 1/loop_count

        start_time = time.time()  # Lấy thời gian bắt đầu vòng lặp

        func()

        # Tính thời gian đã trôi qua
        elapsed_time = time.time() - start_time

        # Đảm bảo vòng lặp chỉ mất 300ms, nếu ít hơn thì chờ thêm
        if elapsed_time < loop_time:
            time.sleep(loop_time - elapsed_time)

def main():
    
    if game.state == "base":
        game.go_to_escort_point()
        game.move_to_battlefield()
    else:
        game.action()

loop(main,3)

