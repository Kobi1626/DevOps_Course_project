# Import nesssary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import json
import db_connector

# Define color for print commands
CERROR = '\033[91m'
CSUCESS = '\033[92m'
CWARNING = '\033[93m'
CRESET = '\033[0m'
CINPUT = '\033[94m'


# Post request for inserting a new user to the DB
def post_request(user_id, user_name):
    response = requests.post('http://127.0.0.1:5000/users/' + str(user_id), json={"user_name": user_name})
    return response.content


# Get request for getting the user_name from the DB according to the user_id
def get_request(user_id):
    response = requests.get('http://127.0.0.1:5000/users/' + str(user_id))
    return response.content


def main():
    # Input by the user
    user_id = input(CINPUT + 'Please Insert a unique UserID: ' + CRESET)  # Receive user input for user_id
    if not user_id.isdigit():
        print(CERROR + 'UserID must be a number' + CRESET)
        exit()
    user_name = input(CINPUT + 'Please Insert a User Name: ' + CRESET)  # Receive user input for user_name
    post_res = post_request(user_id, user_name)  # run the post request

    # Getting the Username by userid and checking if it matched original input
    get_res = json.loads(get_request(user_id))
    if str(user_name) == get_res['user_name']:
        print(CSUCESS + "Data equals to the posted data" + CRESET)
    else:
        raise Exception(CERROR + "Test failed, an error has occured." + CRESET)

    # Chcecking the DB if the posted data is successfully stored
    db_result = db_connector.get_user_name_by_user_id(user_id)
    if db_result == user_name:
        print(CSUCESS + "Posted data is successfully stored inside DB" + CRESET)
    else:
        raise Exception(CERROR + "Test failed, an error has occured." + CRESET)

    # Runing Selenium chrome driver and check if it matched after user creation
    driver = webdriver.Chrome(service=Service("/Users/kobibensenyor/Downloads/chromedriver_mac_arm64"))
    driver.get('http://127.0.0.1:5001/users/get_user_data/' + str(user_id))
    user_element = driver.find_element(By.ID, "user")
    user_name_from_e = user_element.text
    if str(user_name_from_e) == str(user_name):
        print(CSUCESS + "The user name Matches ! \nValidation has been Passed." + CRESET)
    else:
        raise Exception(CERROR + "Test failed, an error has occured." + CRESET)
    print(CWARNING + "Closing selenium chrome driver...")
    driver.quit()
    driver.service.process.wait()
    print(CWARNING + "Closing selenium chrome driver..." + CSUCESS + "Done!" + CRESET)


if __name__ == "__main__":
    main()