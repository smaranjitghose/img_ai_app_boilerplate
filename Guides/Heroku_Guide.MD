<h1 align = "center">Heroku Guide</h1>

## Steps to Follow
1. Go to [Heroku's website](http://heroku.com/).
2. Log In. If you do not have an account please set it up. [Tip: _Using GitHub to setup account makes things easier + you can make use of GitHub Education Pack if you are a student_]
3. Open Your [Dashboard](https://dashboard.heroku.com/apps)
4. Click on Create New App.
4. Give an appropriate name and click `next`.
5. Change the `Deployment method` to `GitHub` and connect your account.
6. Now, search for the repository you made and modified using this template.
7. Connect it.
8. Choose the branch. (Initially, this would be the master branch and later you can have multiple branches to choose from if you are experimenting with prototypes of different models trained for the same task.)

9. Choose either automatic or manual deploy.

    __NOTE:__ Unless you have a CI like [CircleCI](https://circleci.com/) set up in your repository and are aware of how it works please go for `Manual Deploy` option.

10. Click on `Deploy Branch`.

Sit back and relax! Your entire app is being setup and will be served in a while.

## Some useful tips:
1. If you wish to check the size occupied by your files for the deploy in Heroku:  
    - Open your app dashboard

    - Click on `More` Option on the right of the Menu bar

    - Select `Run Console`

    - Paste the command:
        ```
        $ du -sh * | sort -hr
        ```
    - Press Enter.


2. You can add a `.slugignore` file (Similar to a `.gitignore` file we use for git to untrack files while we add/commit) to your application to tell the slug compiler to ignore any unnecessary files in your application, such as *static assets*.

3. To View Logs using CLI:
    ```
    $ heroku logs --tail
    ```

__NOTE:__ For the free tier, it is suggested that you use models that are small in size to avoid issues to the limited slug size Heroku Provides.

## References
1. [My slug size is too large. How can I make it smaller?](https://help.heroku.com/KUFMEES1/my-slug-size-is-too-large-how-can-i-make-it-smaller)
