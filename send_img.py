import pyrebase

# Configuration Information
config = {
"apiKey" :                   , 
"authDomain" :        ,
"databaseURL" :      ,
"projectId":         , 
"storageBucket" :     , 
"messagingSenderId" :  ,
"appId" :   ,
"measurementId" : ,
}
# The path on the cloud storage of Firebase is dependent as per our setup
def send_img(path_local, path_on_cloud = " "):
  '''
  Function to push the file into our Firebase storage
  '''
  firebase = pyrebase.intialize_app(config)
  storage = firebase.storage()
  storage.child(path_on_cloud).put(path_local)
