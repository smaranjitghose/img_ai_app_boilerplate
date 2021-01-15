<h1 align = "center">Image🖼 Classification App Boilerplate</h1>

Have you been puzzled by tons of videos, blogs and other resources on the internet and don't know where and how to deploy your AI models?
<p align = "center"><img src = "https://media.giphy.com/media/8mndEBLsg9Whg2Sduv/giphy.gif" width = 30%></p>

Won't it be nice if you could have a template where you just insert your trained model files, edit some promo text and Voila, it's done.
<p align = "center"><img src = "https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif" width = 25%></p>

Well, look no further because this repository makes it as easy for you as it sounds!
<p align = "center"><img src = "https://media.giphy.com/media/ohMtDzrhrWgnK/giphy.gif" width = 25%></p>

# How to use this project?🤔🤔:
<p align = "center"><img src = "https://media.giphy.com/media/Ln2dAW9oycjgmTpjX9/giphy.gif" width = 50%></p>

__NOTE: For now, we are exclusively focused on image classification models built using tensorflow/pytorch. Later we would expand to models dealing with text and speech data as well as training using MXNet or a julia environment__

- I assume you have *Python(with Anaconda)* installed in your operating system and set to path. If not, please visit [this](https://docs.anaconda.com/anaconda/install/). Using GIT along with Python is highly recommended for version control and deployment


## A. Fetching our template and setting it up:

<p align = "center"><img src = "https://media.giphy.com/media/3o72F7RrTPW6jymXew/giphy.gif" width = 50%></p>


1. Open GitHub

2. Log in with your credentials. [ Create an account if you have not done it already]

3. Open the terminal/command prompt on your system

4. Move to a suitable location where you want to keep the project files locally

Example: `cd Desktop/projects`

5. Clone [this](https://github.com/smaranjitghose/img_ai_app_boilerplate) repository.

```
git clone --depth 1 https://github.com/smaranjitghose/img_ai_app_boilerplate.git
```

6. Navigate inside your cloned copy of the template

```
cd img_ai_app_boilerplate
```

7. Now, let's fetch our dependencies to run our app. [A python package called [StreamLit](https://docs.streamlit.io/en/stable/) is at  the heart of this app]

```
 pip install -r requirements.txt
```

8. Now, let's put our model files inside the app. 


## B. Integrating our Trained Model:

<p align = "center"><img src = "https://media.giphy.com/media/9VfMSBNUmELTi/giphy.gif" width = 40%></p>



1. Open the `model` sub-directory 

```
cd model
start .
```

2. Paste your `Keras.h5` model files there

3. Shoot up your favorite code editor/IDE (I prefer VSCode).

    `code .` [Type this in the terminal to open VSCode if you already have it installed]

4. Now open the file [`img_classifier.py`](./img_classifier.py).

5. Search for the variable `labels` in the code and set its' value as per the labels of the dataset used for training your model.
    [say if you are doing Cats Vs Dogs classification, then `labels = {0: "Cats", 1: "Dogs"}` ]

    __NOTE: This is totally dependent on your model training__

6. Update the value of the variable `model` with the path of your model file.

    [say `model = tensorflow.keras.models.load_model('model/catsvsdogs.h5')`]
    
7. Save the changes.

## C. Frontend and Content Changes

<p align = "center"><img src = "https://media.giphy.com/media/3o72F2vvc71VgmlvgI/giphy.gif" width = 50%></p>

Continuing with changes to the User Interface or the frontend of our app please follow the steps mentioned below:

#### Home Page🏡

1. Open [`app.py`](./app.py).

2. Search for `st.title` and update the Title of the app as per your application's needs.

    [say `st.title('Our Cats vs Dogs Classifier')`]

3. Now search for variable `page_title` and update it with the same. This will tweak the *SEO*. 

    [say `page_title="Cats Vs Dogs",`]

4. If you have some affiliation or maybe the app is made completely by you (perhaps with a group of your friends/colleagues) as a pet project, you can reflect that in the app by searching for `st.subheader` and updating it

      [say ```st.subheader("By John Doe and Jane Doe")```]


__^^ Delete any or all code that you won't use from the above__

#### Contact Page🤳

1. Search for the function call `display_team("Your Awesome Name", "./assets/profile_pic.png","Your Awesome Affliation","hello@youareawesome.com"` and update the following parameters as per your own discretion:

    - **Name**
    - **path_to_image** (I would suggest storing the images inside `assets/images/`
    - **Affiliation**
    - **email**

2. For adding multiple members, you can call the same function multiple times. For example:

```
    display_team("John Doe","./assets/john_doe.png","Stanford University","contact@johndoe.com")
    display_team("Jane Doe","./assets/jane_doe.png","Harvard University","contact@janedoe.com")
```

## D. Storing the Images📤 and User Feedback Online 

#### Setting up Firebase

- Login in to **[Firebase](https://firebase.google.com/)**, using your *Gmail ID*.

- Click on the `Get Started` button which will, take you to your console.

#### Creating a project

- Click on `Add project`. Once you do so, a 3 Step process will start.

- Enter the name of your project. (**Pro tip:** Keep the same name as the name of your App. It would make it easier to identify.)

- The next step is pretty self explanatory and you may/may not choose to enable google analytics.

    - If you choose to enable google analytics, then you will have to select or create a *Google Analytics account*.

    - If you choose not to, then a `Create project` button will appear instead of Continue.

- Once you click on `Create project`, you will land on Firebase Console.

#### Setting up Storage

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

#### Setting up Realtime Database

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


#### Removing FIREBASE👋👋 

If you do not want to use firebase please feel free to:
 
- Remove the `firebase_bro.py` file from the current working directory

- Delete the following lines from the `app.py` file:
    - `import firebase_bro`.

    - `firebase_bro.send_img(image)` line inside the `Home` block of the if else condition.

    - `firebase_bro.send_feedback(first_name, last_name, user_email, feedback)` line inside the `Feedback` block of the if else condition.

- Also remove `firebase` and all the lines below the comment `For Handling firebase and pyrebase dependency issues` in the `requirements.txt`

__REMEMBER: The current version of the app only supports jpg, png and jpeg images as input__

## E. Testing🧪 the app Locally


<p align = "center"><img src = "https://media.giphy.com/media/3ohhworAhxSEHT3zDa/giphy.gif" width = 50%></p>

- Now, we are all set to test our prototype!

- Open the terminal/command prompt and type
```
$ streamlit run app.py
```

- Give it a few seconds to start on your local server, load Tensorflow and other cool stuff the app requires in order to function properly.

- Upload Your Image, Click on Predict, Verify the working

__NOTE:__ If you face any difficulties please raise an issue and let me know

**Congrats! You have successfully deployed your models**

<p align = "center"><img src = "https://media.giphy.com/media/3oz8xAFtqoOUUrsh7W/giphy.gif" width = 50%></p>

## F. Hosting the App 🚛 

<p align = "center"><img src = "https://media.giphy.com/media/L2HCO7avkR5H9MvS9Y/giphy.gif" width = 50%></p>

If you wish to share this as a prototype for others to try or showcase it to your friends and collegeues, please follow these steps:

#### Pushing the code to GitHub

1. Create a new github repository with an approriate name say my ``my_app`` ( DO NOT ADD LICENSE, README, CODE OF CONDUCT, GITIGNORE files at this moment)

**Depending upon your preference, you can make the repository private or public**

2. Open the Terminal/Command Prompt once again

3. Make new folder having the same name as the github repository name

```
mkdir my_app
```

4. Now let's copy all the files of the folder containing our prototype to this folder

```
cp -a ./img_ai_app_boilerplate/. ./my_app/
```

5. Navigate to the location of the above newly created directory

``
cd my_app
``

6.  After copying, please feel free to remove the documentation related files that are unnecessary for your prototype


```
rm -r Guides\
rm LICSENSE CODE_OF_CONDUCT.md CONTRIBUTING.md README.MD
rm -r assets\readme_assets\
```


7. Intiatilize the directory as a git repository

```
git init
```

8. Set remote to your repository on GitHub( Copy the link of the repository from the Address Bar)

```
git remote add origin https://github.com/your_github_username/my_app.git 
```


9. Track and commit the current changes

```
git add .
git commit -m "v.0.0.1"
```

10. Push the changes to your remote repository on GitHub

```
git push origin main
```

11. Once successsfull, close the terminal. 

12. Go to GitHub and locate the repository to check if the changes are reflected

13. Now Add your own custom:
    - README.MD file (To descibe your project in brief)
    - LICENSE file (This depends upon you. I prefer going with MIT License for my open source repositories)
    - CODE_OF_CONDUCT.MD ( GitHub already provides a template for this)
    - Short Repository Description on the right
    - Relevant Tags
    
    
#### Hosting using a cloud service ☁:    

Now as per your choice of hosting, please refer the following guides:

- [Heroku (Recommended for Beginners)](./Guides/Heroku_Guide.MD)
- [Google Cloud Platform](./Guides/GKE_Guide.MD)
- [Microsoft Azure](./Guides/Microsoft_Azure_Guide.MD)
- Amazon Web Services [Bean Stalk or EC2] (__Coming Soon!__)
- Digital Ocean (__Coming Soon!__)
- Linode (__Coming Soon!__)
- Python Everywhere (__Coming Soon!__)


# [Code of Conduct](./CODE_OF_CONDUCT.MD)
<p align="center"><img width=35% src="https://media.giphy.com/media/yc2T1xcXXRwpcAfFLm/giphy.gif"></p>

# [License](./LICENSE) 
<p align="center"><img width=35% src="https://media.giphy.com/media/2ijAt1xl4zQ3PGYr7A/giphy.gif"></p>


# Future Work 🏗

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


# If this project helped you, do give it a 🌟 on GitHub and share your work over LinkedIN and/or Twitter by tagging me!
