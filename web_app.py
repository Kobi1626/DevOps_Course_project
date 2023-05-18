from flask import Flask
import db_connector

HOSTNAME: str = '127.0.0.1'
PORT: int = 5001

app = Flask(__name__)
######## Retrieves the user name for the given user ID from the database and returns it in HTML format. ########
@app.route("/users/get_user_data/<user_id>", methods = ['GET']) # Define route for getting user data by user ID
def get_user_name(user_id):
    user_name = db_connector.get_user_name_by_user_id(int(user_id)) # Get the user name from the database
    if user_name != "user_id doesn't exist":
        return "<H1 id='user'>" + user_name + "</H1>" # Return the user name in HTML format if it exists
    else:
        return "<H1 id='error'>" + "UserID Not Found: " + user_id + "</H1>" # Return an error message in HTML format if user ID doesn't exist


#  ensures that the following code block runs only when the script is executed directly as the main program.
if __name__ == '__main__':
    app.run(host=HOSTNAME, debug=True, port=PORT)