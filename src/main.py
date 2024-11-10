from modules import GameEngine;
import time

game = GameEngine()

def loop(func,loop_count=5):
    while True:

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

loop(main,5)

