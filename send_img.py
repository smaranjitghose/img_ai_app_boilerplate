from firebase import Firebase

# The path on the cloud storage of Firebase is dependent as per our setup
def send_img(path_local, path_on_cloud = " "):
  '''
  Function to push the file into our Firebase storage
  '''
  # Configuration Information
  config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId":  "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId":  "",
    "measurementId": "",
  }
  firebase = Firebase(config)
  storage = firebase.storage()
  storage.child(path_on_cloud).put(path_local)
