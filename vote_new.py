import time
import pyautogui
import os
os.environ['DISPLAY'] = ':0'

def vote2(option_x, option_y):
    pyautogui.moveTo(option_x, option_y, duration=0)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.keyDown('enter')
    time.sleep(1)
    try:
        repeat = pyautogui.locateOnScreen('img/repeat1.png', grayscale=True)
        pyautogui.press('tab') 
    except:
        time.sleep(5)
        try:
            repeat = pyautogui.locateOnScreen('img/repeat1.png', grayscale=True)
            pyautogui.press('tab') 
        except:
            time.sleep(5)
            pyautogui.press('tab') 
    pyautogui.press('enter')
    
    time.sleep(1)

def run_vote():
    time.sleep(3)
    title = pyautogui.getWindowsWithTitle("Chrome")[0].title
    option_x, option_y = pyautogui.position()
    for i in range(100):
        if pyautogui.getWindowsWithTitle("Chrome")[0].title != title:
            return
        vote2(option_x, option_y)

    

# import keyboard
# time.sleep(2)
# def get_data(option_x, option_y):
#     # # screenshot = pyautogui.screenshot("element.png")
#     # img_name = 'img/option.png'
#     # # if option_name:
#     # #     img_name = 'img/' + option_name
#     # option = pyautogui.locateOnScreen(img_name, grayscale=True)
#     # if option is None:
#     #     print("Element not found on the screen")
#     #     return
#     # option_x = option.left + (option.width // 2)
#     # option_y = option.top + (option.height // 2)
#     pyautogui.moveTo(option_x, option_y, duration=0)
#     submit = pyautogui.locateOnScreen('img/submit.png', grayscale=True)
#     if submit is None:
#         print("Element not found on the screen")
#         return
#     submit_x = submit.left + (submit.width // 2)
#     submit_y = submit.top + (submit.height // 2)
#     pyautogui.click()
#     pyautogui.moveTo(submit_x, submit_y, duration=0)
#     pyautogui.click()
#     time.sleep(2)
#     repeat = pyautogui.locateOnScreen('img/repeat.png', grayscale=True)
#     if repeat is None:
#         print("Element not found on the screen")
#         return
#     repeat_x = repeat.left + (repeat.width // 2)
#     repeat_y = repeat.top + (repeat.height // 2)
#     pyautogui.moveTo(repeat_x, repeat_y, duration=0)
#     pyautogui.click()
#     return option_x, option_y, submit_x, submit_y, repeat_x, repeat_y

# option_x, option_y, submit_x, submit_y, repeat_x, repeat_y = get_data()

# def click_element_by_text():
#     time.sleep(1)
#     # screenshot = pyautogui.screenshot("element.png")
#     pyautogui.moveTo(option_x, option_y, duration=0)
#     pyautogui.click()
#     pyautogui.moveTo(submit_x, submit_y, duration=0)
#     pyautogui.click()
#     time.sleep(1)
#     pyautogui.moveTo(repeat_x, repeat_y, duration=0)
#     pyautogui.click()


# def vote(option_x, option_y):
#     pyautogui.moveTo(option_x, option_y, duration=0)
#     pyautogui.doubleClick()
#     try:
#         submit = pyautogui.locateOnScreen('img/submit1.png', grayscale=True)
#     except:
#         x = open("img/submit1.png", 'r')
#         print("x", x.name)
#         submit = pyautogui.locateOnScreen('img/submit.png', grayscale=True)
#     if submit is None:return
#     submit_x = submit.left + (submit.width // 2)
#     submit_y = submit.top + (submit.height // 2)
#     pyautogui.moveTo(submit_x, submit_y, duration=0)
#     pyautogui.click()
  
#     time.sleep(4)
#     try:
#         repeat = pyautogui.locateOnScreen('img/repeat1.png', grayscale=True)
#     except:
#         repeat = pyautogui.locateOnScreen('img/repeat.png', grayscale=True)
#     if repeat is None:return
#     repeat_x = repeat.left + (repeat.width // 2)
#     repeat_y = repeat.top + (repeat.height // 2)
#     pyautogui.moveTo(repeat_x, repeat_y, duration=0)
#     pyautogui.click()


#     time.sleep(1)
