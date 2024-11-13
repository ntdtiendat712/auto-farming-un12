from PIL import ImageGrab,Image
import numpy as np
import pyautogui
import math
import logging
import time
import mss

def find_point_C(A, B, length=0):
    # Tọa độ điểm A và B
    xA, yA = A
    xB, yB = B
    
    # Tính vector từ B đến A
    vector_BA = (xA - xB, yA - yB)
    
    # Xoay vector_BA 90 độ theo chiều kim đồng hồ để có vector BC
    vector_BC = (vector_BA[1], -vector_BA[0])
    
    # Tính độ dài của vector_BC
    norm_BC = np.sqrt(vector_BC[0]**2 + vector_BC[1]**2)
    
    # Chuẩn hóa vector_BC để có độ dài đúng bằng `length` (5 đơn vị)
    unit_vector_BC = (vector_BC[0] / norm_BC * length, vector_BC[1] / norm_BC * length)
    
    # Tính tọa độ điểm C
    xC = xB + unit_vector_BC[0]
    yC = yB + unit_vector_BC[1]
    
    return int(xC), int(yC)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def euclidean_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
def find_closest_point(points, A, B):
    min_distance = float('inf')
    closest_point = None
    
    # Duyệt qua tất cả các điểm trong mảng
    for point in points:
        # Tính tổng khoảng cách từ điểm đến A và B
        distance = euclidean_distance(point, A) + euclidean_distance(point, B)
        
        # Nếu khoảng cách nhỏ hơn khoảng cách min_distance, cập nhật lại
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    
    return closest_point

BORDER_COLOR = "#bfb6a4"

def getPointPosition():
  print(pyautogui.position())
  return
  with mss.mss() as sct:

    # for i, monitor in enumerate(sct.monitors[1:], start=0):  
    #       width = monitor['width']
    #       height = monitor['height']
    #       print(f"Monitor {i}: {width}x{height}")

    square_size=1000
   
    monitor = sct.monitors[0]
    screen_width = monitor["width"]
    screen_height = monitor["height"]
    print(f"screen_width:{screen_width} screen_height:{screen_height}")
    left = (screen_width - square_size) // 2
    top = (screen_height - square_size) // 2

    center_x = screen_width//2
    center_y = screen_height//2

    monitor_part = {"left": left, "top": top, "width": square_size, "height": square_size}
    print(monitor_part)
    screenshot = sct.grab(monitor_part)  # Chụp màn hình chính (hoặc thay đổi màn hình nếu cần)
    print(f"screenshot.size{screenshot.size}")
    screenshot_np = np.array(Image.frombytes("RGB", screenshot.size, screenshot.rgb))
    matches = np.all(screenshot_np == hex_to_rgb(BORDER_COLOR), axis=-1)
    coordinates = np.argwhere(matches)
    print(coordinates)
    borders = [[x + left, y + top] for x, y in coordinates]
    print(borders)
    for x, y in borders:
        pyautogui.moveTo(997, 383)   # Di chuyển chuột tới tọa độ (x, y)
        time.sleep(0.005)    
    print(f"len:{len(borders)}")
    if len(borders) < 1:
      return
    mouse_x, mouse_y = pyautogui.position()
    print(f"{len(borders)} {center_x},{center_y} {mouse_x},{mouse_y}")
    closest_point = find_closest_point(borders,[center_x,center_y],[mouse_x,mouse_y])
    print(f"closest_point:{closest_point}")

    if len(borders) < 1:
      return
    Cx,Cy = find_point_C([center_x,center_y],closest_point)
    print(f"xy:   {Cx}:{Cy}")
    # pyautogui.moveTo(1211, 1231)
    pyautogui.moveTo(int(closest_point[0]), int(closest_point[1]))
  return 


