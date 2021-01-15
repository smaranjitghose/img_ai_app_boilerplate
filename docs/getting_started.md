# Fetching our template and setting it up:

<p align = "center"><img src = "https://media.giphy.com/media/Ln2dAW9oycjgmTpjX9/giphy.gif" width = 50%></p>

I assume you have *Python(with Anaconda)* installed in your operating system and set to path. If not, please visit [this](https://docs.anaconda.com/anaconda/install/). Using GIT along with Python is highly recommended for version control and deployment

- Open GitHub

- Log in with your credentials. [ Create an account if you have not done it already]

- Open the terminal/command prompt on your system

- Move to a suitable location where you want to keep the project files locally (Example: `cd Desktop/projects`)

- Clone [this](https://github.com/smaranjitghose/img_ai_app_boilerplate) repository.

```
git clone --depth 1 https://github.com/smaranjitghose/img_ai_app_boilerplate.git
```

- Navigate inside your cloned copy of the template

```
cd img_ai_app_boilerplate
```

- Now, let's fetch our dependencies to run our app. [A python package called [StreamLit](https://docs.streamlit.io/en/stable/) is at  the heart of this app]

```
 pip install -r requirements.txt
```

- In the next section, check out how integrate your model files inside the app. 

__NOTE: For now, we are exclusively focused on image classification models built using tensorflow/pytorch. Later we would expand to models dealing with text and speech data as well as training using MXNet or a julia environment__
