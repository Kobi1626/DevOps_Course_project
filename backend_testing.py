# Import nesssary modules
import json
import requests
import db_connector

# Define color for print commands
CERROR = '\033[91m'
CSUCESS = '\033[92m'
CWARNING = '\033[93m'
CRESET = '\033[0m'
CINPUT = '\033[94m'

#Post request for inserting a new user to the DB
def post_request(user_id,user_name):
        response = requests.post('http://127.0.0.1:5100/users/'+ str(user_id), json={"user_name": user_name})
        print(response.content)
        if str(response.status_code) == "200":
            print(CSUCESS + "PostRequest was successful, Status Code is 200" + CRESET)
        else:
            print(CERROR +"PostRequest was unsuccessful, Status Code is 500" + CRESET)

#Get request for getting the user_name from the DB according to the user_id
def get_request(user_id):
    response = requests.get('http://127.0.0.1:5100/users/'+ str(user_id))
    if str(response.status_code) == "200":
        print(CSUCESS + "GetRequest was successful, Status Code is 200" + CRESET)
    else:
        print(CERROR +"GetRequest was unsuccessful, Status Code is 500" + CRESET)
    return response.content

def main():
    user_id = "4"
    if not user_id.isdigit():
        print(CERROR + 'UserID must be a number' + CRESET)
        exit()
    user_name = "Kobi"
    post_request(user_id,user_name)
    # Getting the Username by userid and checking if it matched original input
    get_res = json.loads(get_request(user_id))
    if user_name == get_res['user_name']:
        print(CSUCESS + "Data equals to the posted data" + CRESET)
    else:
        print(CERROR + "Data doesn't equal to the posted data" + CRESET)

    #Chcecking the DB for the user found according to userid
    print(CWARNING +f"User Name found in DB according to the ID: " + db_connector.get_user_name_by_user_id(user_id) + CRESET)


if __name__ == "__main__":
    main()
