from firebase import Firebase

# Setting up Firebase configurations
# To learn how to set it up, please go through Firebase_Setup.MD
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectID": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
}

firebase = Firebase(config)

def firebase_gettin():
  '''
  Authentication for Firebase
  '''
  auth = firebase.auth()

  email = "Enter your email here"
  password = "Enter your password"

  try:
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully Signed In")
  except:
    print("Invalid Credentials")

# The path on the cloud storage of Firebase is dependent as per our setup
def send_img(path_local, path_on_cloud = "images/test.jpg"):
  '''
  Function to push the file into our Firebase storage
  '''
  # Configuration Information
  storage = firebase.storage()
  storage.child(path_on_cloud).put(path_local)

def send_feedback(first_name,last_name,email_id,message):
  '''
  Function to push feedback data to firebase
  '''
  db = firebase.database()
  data = {"f_name":first_name,"l_name":last_name,"email":email_id,"msg" : message}
  db.child("people").push(data)
