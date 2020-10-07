<h1 align = "center">Image Classification App Boilerplate</h1>

Have you been puzzled by tons of videos, blogs and other resources on the internet and don't know where and how to deploy your AI models?
<p align = "center"><img src = "https://media.giphy.com/media/8mndEBLsg9Whg2Sduv/giphy.gif" width = 30%></p>

Won't it be nice if you could have a template where you just insert your trained model files, edit some promo text and Voila, it's done?
<p align = "center"><img src = "https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif" width = 25%></p>

Well, look no further because this repository makes it as easy for you as it sounds!
<p align = "center"><img src = "https://media.giphy.com/media/ohMtDzrhrWgnK/giphy.gif" width = 25%></p>

## How to use this?
<p align = "center"><img src = "https://media.giphy.com/media/26AHPxxnSw1L9T1rW/giphy.gif" width = 50%></p>

__NOTE: For now, we are exclusively focused on image classification models built using tensorflow/pytorch. Later we would expand to models dealing with text and speech data as well as training using MXNet or a julia environment__

- I assume you have *Python(with Anaconda)* installed in your operating system and set to path. If not, please visit [this](https://docs.anaconda.com/anaconda/install/).

- Now, once that is done, please clone this repository for your local system and use this as the template repo on your GitHub.
- After cloning the repo, move inside the repo, using the command:

    `cd img_ai_app_boilerplate `

- Now, let's fetch our dependencies to run our app. [A python package called [StreamLit](https://docs.streamlit.io/en/stable/) is at  the heart of this app]

    `pip install -r requirements.txt`

- Now, let's put our model files in the app. Open the `model` sub-directory and paste your `Keras h5` model files there.

### Integrating your Model
1. Open VSCode or your favorite code editor/IDE.

    `code .` [Type this in the terminal to open VSCode if you already have it installed]

2. Now open the file [`img_classifier.py`](./img_classifier.py).
3. Search for the variable `labels` in the code and set them as per your training model.
    [say if you are doing Cats Vs Dogs classification, then `= {0: "Cats", 1: "Dogs"`]

    __NOTE: This is totally dependent on your model training__

4. Update `model` with the name of your model file.

    [say `model = tensorflow.keras.models.load_model('model/catsvsdogs.h5')`]
5. Save the changes.

### Making changes in frontend
Continuing with changes to the User Interface or the frontend of our app. Follow the steps mentioned below:
1. Open [`app.py`](./app.py).

2. Search for `st.title` and update the Title of the app as per your application's needs.

    [say `st.title('Our Cats vs Dogs Classifier')`]

3. Let's do the same for our *Page Title* and tweak our *SEO*. Search for `page_title` and update it.

    [say `page_title="Cats Vs Dogs",`]

4. If you have some affiliation or maybe the app is made completely by you (perhaps with a group of your friends/colleagues) as a pet project, you can reflect that in the app by searching for `st.subheader` and updating it

      [say ```st.subheader("By John Doe and Jane Doe")```]

#### Updating our CONTACT PAGE
 You can add your and/or your teammates' names, profile pictures, email and affiliation. You can do so by following the aforementioned steps.
1. Search for `display_team` and pass/update the following parameters:
    - **Name**
    - **path_to_image**
    - **Affiliation**
    - **email**

2. For adding multiple contributors, you can call the same function multiple times. For eg.:

    ```python
    display_team("John Doe","./assets/john_doe.png","Stanford University","contact@johndoe.com")
    display_team("Jane Doe","./assets/jane_doe.png","Harvard University","contact@janedoe.com")
    ```

### Storing the Images and User Feedback Online (OPTIONAL)
If you want to store your images and user feedbacks in a cloud database like [Firebase](https://firebase.google.com/), we have some arrangements for you! Follow the steps in [Firebase_Setup.MD](./Guides/Firebase_Setup.MD) to set it up.

 [__NOTE__:] If you are not using firebase please feel free to:
- Remove the `firebase_bro.py` file,

- Delete the following lines from the `app.py` file:
    - `import firebase_bro`.

    - `firebase_bro.send_img(image)` line inside the `Home` block of the if else condition.

    - `firebase_bro.send_feedback(first_name, last_name, user_email, feedback)` line inside the `Feedback` block of the if else condition.

- Also remove `firebase` and all the lines below the comment `For Handling firebase and pyrebase dependency issues` in the [*requirements.txt*](./requirements.txt) file.

__A FINAL NOTE: The current version of the app only supports jpg, png and jpeg images as input__

### Testing the app Locally
 Now, we are all set to test it!

Open the terminal/command prompt and type
```
$ streamlit run app.py
```
Give it a few seconds to start our local server, load Tensorflow and other cool stuff our app requires in order to function properly..

Upload Your Image, Click on Predict, Verify the working

__NOTE:__ If you face any difficulties please raise an issue and let me know

**Congrats! You now have your models deployed!**

## Deploying the App (OPTIONAL)
If you wish to share this as a prototype for others to try, please follow these steps:

1. Track, Commit and Push the changes to your GitHub repository that you initially made using this template repository
    ```
    $ git add .
    $ git commit -m "App v.0.0.1"
    $ git push origin master
    ```

__NOTE: You must be inside the folder containing the app to send the update your copy on GitHub__

Now as per your choice of hosting, please refer the following guides:

- [Heroku (Recommended for Beginners)](./Guides/Heroku_Guide.MD)
- [Google Cloud Platform](./Guides/GKE_Guide.MD)
- [Microsoft Azure](./Guides/Microsoft_Azure_Guide.MD)
- Amazon Web Services [Bean Stalk or EC2]
- Digital Ocean (__Coming Soon!__)
- Linode (__Coming Soon!__)
- Python Everywhere (__Coming Soon!__)



## Further Work 🏗

- [ ] Improve the UI of the app using custom HTML,CSS or REACT
- [ ] Make the App more descriptive
- [ ] Guide for Deployment to Digital Ocean
- [ ] Guide for Deployment to GCP
- [ ] Guide for Deployment to AWS
- [ ] Guide for Deployment to Azure
- [ ] Add Favicon option, Improve SEO
- [x] Add Multiple Pages
     - [x] Contact Page
     - [x] About Page
     - [x] Feedback Page
- [ ] Support for PyTorch models
- [ ] Support for MXNET models
- [ ] Support for saved_model TF format
- [ ] Add Animations
- [ ] Dark Mode
- [ ] Similar Efforts for a mobile app using TFLite + Flutter ( From building to serving)
- [ ] Experiment with TFJS
