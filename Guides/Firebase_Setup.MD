<h1 align = "center">Setting up Firebase</h1>

1. Login in to **[Firebase](https://firebase.google.com/)**, using your *Gmail ID*.

2. Click on the `Get Started` button which will, take you to your console.

## Creating a project
1. Click on `Add project`. Once you do so, a 3 Step process will start.

2. Enter the name of your project. (**Pro tip:** Keep the same name as the name of your App. It would make it easier to identify.)

3. The next step is pretty self explanatory and you may/may not choose to enable google analytics.
    - IF you choose to enable google analytics, then you will have to select or create a *Google Analytics account*.

    - If you choose not to, then a `Create project` button will appear instead of Continue.

4. Once you click on `Create project`, you will land on Firebase Console.

## Navigating through Firebase console
### Setting up Storage
1. Once you land on the Firebase Console, click on the `Create Web App` icon.

2. Give the name of your web app and unless required, do not select the *Hosting* option and click `next`.

3. Copy the code which appears and store in a `config.txt` file for later use.

4. Click on `Continue to Console`.

5. Once on Console, click on the `Storage` Option on the left panel and then click on `Get Started`.

6. Click `Next` and then select a server closest to your location.

7. Once the Storage is initiated, click on the `Rules` tab and change:

    `allow read, write: if request.auth != null;` to

    `allow read, write;`

    in the code snippet which appears on the screen.

    [**Note**: This is only for testing purposes and in real life scenarios refrain from doing this.]

7. This change basically allows us the upload and download the images without authenticating every time.

8. With this you have set up the **Storage successfully**. You can manage your app's cloud server from here.

### Setting up Realtime Database
1. Click on the `Realtime Database` Option on the left panel.

2. Once on the page, click on `Create Database` button.

3. When you click the button, there will be a prompt to set the Security rules. It is recommended to start in **locked mode** so as to ensure security of the data.

4. With this you have set up the **Database successfully**. Now whenever a user writes a feedback, you can check it here in this database. Since this database stores data in terms of `JSON` files, you can also export the JSON file and use it in whichever way you like.

## Linking Firebase in the App
Since everything is set up in the Firebase Console, the only thing left to do is to link the services to your app. You can do it this way:
1. Open [`firebase_bro.py`](../firebase_bro.py).

2. Remember the `config.txt` file which we created earlier? Open it up and copy the contents of `firebaseConfig` into `config` variable inside `firebase_bro.py`.

3. Save the File.

#### Voila! You have **Successfully** set up Firebase into your app!
