import pyrebase

# Copy these from the intial setup of the project
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

# path_on_cloud = " "
# path_local = " "

def send_img(path_local, path_on_cloud):
  '''
  Pushing the file in the given local path to the path given for firebase cloud
  '''
  firebase = pyrebase.intialize_app(config)
  storage = firebase.storage()
  storage.child(path_on_cloud).put(path_local)
