import glfw
from OpenGL.GL import *
import numpy as np
from PIL import Image

# Khởi tạo glfw
if not glfw.init():
    raise Exception("GLFW can't be initialized")

# Tạo cửa sổ OpenGL
window = glfw.create_window(800, 600, "OpenGL Screenshot", None, None)
glfw.make_context_current(window)

# Hàm chụp một vùng màn hình (region)
def capture_region(x, y, width, height):
    # Đọc dữ liệu pixel từ vùng chỉ định trong bộ đệm khung hình
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(x, y, width, height, GL_RGB, GL_UNSIGNED_BYTE)
    
    # Tạo hình ảnh từ dữ liệu pixel
    image = Image.frombytes("RGB", (width, height), pixels)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # Lật ảnh
    return image

# Vẽ gì đó vào màn hình để có hình ảnh trong buffer
glClearColor(0.2, 0.3, 0.3, 1)  # Đặt màu nền
glClear(GL_COLOR_BUFFER_BIT)

# Ghi lại vùng màn hình từ tọa độ (100, 100) với kích thước 300x300
screenshot = capture_region(100, 100, 500, 500)
screenshot.save("screenshot.png")  # Lưu ảnh chụp

# Đóng cửa sổ và dọn dẹp
glfw.terminate()