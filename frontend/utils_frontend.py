import pyautogui

def coordinates_middle(window_width: int, window_height: int) -> tuple:
    screen_width, screen_height = pyautogui.size()
    if screen_height is None or screen_width is None:
        print("Error in getting window coordinates")
        raise ValueError
    middle_coordinates = (((screen_width - window_width) // 2),
                          ((screen_height - window_height) // 2)) # (x coords, y coords) to get middle screen
    return middle_coordinates
    