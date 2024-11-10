from PIL import ImageGrab

blue_area = "#123"
border_area = ""

class Color:
    def get_object_name(color = None):
        case = {
            "#123456":""
        }
        return case.get(color,None)


    def check_color_in_region(target_color="#123456", region=(0, 0, 100, 100)):
        # Chụp ảnh màn hình vùng chữ nhật được xác định bởi tham số `region`
        screenshot = ImageGrab.grab(bbox=region)  # bbox=(x1, y1, x2, y2)

        # Duyệt qua từng pixel trong vùng ảnh chụp
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                # Lấy mã màu RGB của pixel
                pixel_color = screenshot.getpixel((x, y))
                # Chuyển mã màu RGB sang dạng hex để so sánh
                hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color).lower()

                # Kiểm tra nếu pixel có mã màu là màu mong muốn
                if hex_color == target_color:
                    print("Tìm thấy màu {} trong vùng chỉ định.".format(target_color))
                    return True  # Trả về True nếu tìm thấy màu
        print("Không tìm thấy màu {} trong vùng chỉ định.".format(target_color))
        return False
