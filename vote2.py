from selenium.webdriver.common.by import By
from data.emails_list import emails_list
from login import signin
import time
from base import driver

logout = "https://accounts.google.com/InteractiveLogin/signinchooser?elo=1&ifkv=ATuJsjxOy8idNsUjllS2iid6JZtfMl87x0eFWq6PuVvX44If-SJt_-G0NidsqFDXixn2ZvZhYNBbeQ&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
submit_class = "Y5sE8d"
#A_M
#H776009970M

def make_vote(driver, url, option_id, confirm_id, submit_class):
    # time.sleep(1)
    driver.get(url)
    # time.sleep(1)
    # print("############################")
    # driver.implicitly_wait(1)
    # try:
    #     confirm = driver.find_element(By.ID, confirm_id).click()
    # except:
    #     pass
    option = driver.find_element(By.ID, option_id).click()  # Example: by ID
    submit = driver.find_element(By.CLASS_NAME, submit_class).click()
    # driver.get(logout)




# url = "https://docs.google.com/forms/d/e/1FAIpQLSfDtwcYIaan4uavIQVLCEdf0kng7bbDi2SQ0Q5r3f22GtLB3w/viewform"
# option_id = "i5"
# confirm_id = "confirm"# "i5"
    # option_id = input(r"ادخل معرف الخيار الذي تريد التصويت له في الاستبيان : ") or "i11"
    # url = input("ادخل رابط الاستبيان: ") or "https://docs.google.com/forms/d/e/1FAIpQLSeG76WTYmnQ3Ih1SSuNh9eHw18_RFvb7DzMIH6GpE5ggikG-w/viewform"

def run_vote():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeG76WTYmnQ3Ih1SSuNh9eHw18_RFvb7DzMIH6GpE5ggikG-w/viewform"
    option_id = "i23"
    for i in range(10000000):
        try:
            make_vote(driver, url, option_id, "confirm_id", submit_class)
        except Exception as e:
            pass
    # driver.quit()
        
def run_vote_with_email():
    url = input("ادخل رابط الاستبيان: ") or "https://docs.google.com/forms/d/e/1FAIpQLSddSBJ3HASLWluOeig5yvz9VZ1J_qveux91mPD_lBVR0ANrUA/viewform"
    option_id = input(r"ادخل معرف الخيار الذي تريد التصويت له في الاستبيان : ") or "i11"
    confirm_id = input("ادخل معرف تأكيد ادخال الايميل ان وجد في الاستبيان: ") or "confirm"# "i5"
    erro_file = open('erro_file.txt', 'a')
    correct_file = open('correct_file.txt', 'a')
    signin(driver, emails_list[0])
    for i in range(len(emails_list)):
        try:
            signin(driver, emails_list[i])
            # time.sleep(5)
            # make_vote(driver, url, option_id, confirm_id, submit_class)
            correct_file.writelines(emails_list[i])
        except Exception as e:
            erro_file.writelines(emails_list[i])
    erro_file.close()
    correct_file.close()
    # driver.quit()
# run_vote_with_email()