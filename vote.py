from selenium.webdriver.common.by import By
# import time
from base import get_driver

logout = "https://accounts.google.com/InteractiveLogin/signinchooser?elo=1&ifkv=ATuJsjxOy8idNsUjllS2iid6JZtfMl87x0eFWq6PuVvX44If-SJt_-G0NidsqFDXixn2ZvZhYNBbeQ&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
submit_class = "Y5sE8d"
#A_M
#H776009970M

def make_vote(driver, url, option, confirm_id, submit_class):
    driver.get(url)
    option_vote = driver.find_element(By.XPATH, f"//*[@aria-label='{option}']").click()  # Example: by ID
    # option_vote = driver.find_element_by_xpath(f"//*[@aria-label='{option}']")
    submit = driver.find_element(By.CLASS_NAME, submit_class).click()
    # aria-label
def run_vote(url="https://docs.google.com/forms/d/e/1FAIpQLSeG76WTYmnQ3Ih1SSuNh9eHw18_RFvb7DzMIH6GpE5ggikG-w/viewform", option="i23"):
    driver = get_driver()
    for i in range(10000000):
        try:
            make_vote(driver, url, option, "confirm_id", submit_class)
        except Exception as e:
            pass
    driver.quit()

# run_vote()