# Pushing the code to GitHub 🚛 

<p align = "center"><img src = "https://media.giphy.com/media/L2HCO7avkR5H9MvS9Y/giphy.gif" width = 50%></p>


- Create a new github repository with an approriate name say my ``my_app`` ( DO NOT ADD LICENSE, README, CODE OF CONDUCT, GITIGNORE files at this moment)

**Depending upon your preference, you can make the repository private or public**

- Open the Terminal/Command Prompt once again

- Make new folder having the same name as the github repository name

```
mkdir my_app
```

- Now let's copy all the files of the folder containing our prototype to this folder

```
cp -a ./img_ai_app_boilerplate/. ./my_app/
```

- Navigate to the location of the above newly created directory

``
cd my_app
``

- After copying, please feel free to remove the documentation related files that are unnecessary for your prototype


```
rm -r Guides\
rm LICSENSE CODE_OF_CONDUCT.md CONTRIBUTING.md README.MD
rm -r assets\readme_assets\
```


- Intiatilize the directory as a git repository

```
git init
```

- Set remote to your repository on GitHub( Copy the link of the repository from the Address Bar)

```
git remote add origin https://github.com/your_github_username/my_app.git 
```


- Track and commit the current changes

```
git add .
git commit -m "v.0.0.1"
```

- Push the changes to your remote repository on GitHub

```
git push origin main
```

- Once successsful, close the terminal. 

- Go to GitHub and locate the repository to check if the changes are reflected

- Now add your own custom:
    - README.MD file (To describe your project in brief)
    - LICENSE file (This depends upon you. I prefer going with MIT License for my open source repositories)
    - CODE_OF_CONDUCT.MD ( GitHub already provides a template for this)
    - Short Repository Description on the right
    - Relevant Tags

