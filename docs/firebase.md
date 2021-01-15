# D. Storing the Images📤 and User Feedback Online 

## Setting up Firebase

- Login in to **[Firebase](https://firebase.google.com/)**, using your *Gmail ID*.

- Click on the `Get Started` button which will, take you to your console.

## Creating a project

- Click on `Add project`. Once you do so, a 3 Step process will start.

- Enter the name of your project. (**Pro tip:** Keep the same name as the name of your App. It would make it easier to identify.)

- The next step is pretty self explanatory and you may/may not choose to enable google analytics.

    - If you choose to enable google analytics, then you will have to select or create a *Google Analytics account*.

    - If you choose not to, then a `Create project` button will appear instead of Continue.

- Once you click on `Create project`, you will land on Firebase Console.

## Setting up Storage

- Once you land on the Firebase Console, click on the `Create Web App` icon.

- Give the name of your web app and unless required, do not select the *Hosting* option and click `next`.

- Copy the code which appears and store in a `config.txt` file for later use.

- Click on `Continue to Console`.

- Once on Console, click on the `Storage` Option on the left panel and then click on `Get Started`.

- Click `Next` and then select a server closest to your location.

- Once the Storage is initiated, click on the `Rules` tab and change:
`allow read, write: if request.auth != null;` to `allow read, write;` in the code snippet which appears on the screen.

    **Note: This is only for testing purposes and in real life scenarios refrain from doing this.**

- This change basically allows us the upload and download the images without authenticating every time.

- With this you have set up the **Storage successfully**. You can manage your app's cloud server from here.

## Setting up Realtime Database

1. Click on the `Realtime Database` Option on the left panel.

2. Once on the page, click on `Create Database` button.

3. When you click the button, there will be a prompt to set the Security rules. It is recommended to start in **locked mode** so as to ensure security of the data.

4. With this you have set up the **Database successfully**. Now whenever a user writes a feedback, you can check it here in this database. Since this database stores data in terms of `JSON` files, you can also export the JSON file and use it in whichever way you like.

## Linking Firebase in the App

Since everything is set up in the Firebase Console, the only thing left to do is to link the services to your app. You can do it this way:

1. Open `firebase_bro.py`

2. Remember the `config.txt` file which we created earlier? Open it up and copy the contents of `firebaseConfig` into `config` variable inside `firebase_bro.py`.

3. Save the File.

*Voila! You have Successfully set up Firebase into your app!*


## Removing FIREBASE👋👋 

If you do not want to use firebase please feel free to:
 
- Remove the `firebase_bro.py` file from the current working directory

- Delete the following lines from the `app.py` file:
    - `import firebase_bro`.

    - `firebase_bro.send_img(image)` line inside the `Home` block of the if else condition.

    - `firebase_bro.send_feedback(first_name, last_name, user_email, feedback)` line inside the `Feedback` block of the if else condition.

- Also remove `firebase` and all the lines below the comment `For Handling firebase and pyrebase dependency issues` in the `requirements.txt`

__REMEMBER: The current version of the app only supports jpg, png and jpeg images as input__