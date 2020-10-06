from firebase import Firebase

def feedback_db(user_email, feedback):
    # Setting the Firebase configurations of the App
    config = {
    "apiKey": "apiKey",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "projectId.appspot.com"
    }

    firebase = Firebase(config)

    # Initialising Firebase database
    db = firebase.database()

    # This will be stored in the database
    feedback_data = {
    "email" : user_email,
    "feedback" : feedback
    }

    # This command will make a category named user_feedback and push the data
    # inside that category
    db.child("user_feedback").push(feedback_data)
