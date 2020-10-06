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
1. Once you land on the Firebase Console, you need to go to the **settings**, which you can find on the **upper left corner** as a **cog wheel**.

2. Then click on `Project Settings`. Here you will find the configuration info you need in order to use the *[real-time database functionality](https://firebase.google.com/docs/database/)*.

3. We need the following values to fill in [`feedback_db.py`](../feedback_db.py):
    - **Web API key**
    - **Project ID**
    - **DatabaseName** - Same as Project ID

4. Once you update these details inside `config`, you have successfully set up Firebase in your app.

## Retrieving Data from the Realtime Database
1. Click on the `Realtime Database` Option on the left panel.

2. Once on the page, click on `Create Database` button.

3. When you click the button, there will be a prompt to set the Security rules. It is recommended to start in **locked mode** so as to ensure security of the data.

4. With this you have set up the **database successfully**. Now whenever a user writes a feedback, you can check it here in this database. Since this database stores data in terms of `JSON` files, you can also export the JSON file and use it in whichever way you like.
