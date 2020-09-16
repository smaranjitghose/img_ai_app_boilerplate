# Heroku Tips that might be useful: 

- If you wish to check the size occupied by your files for the deploy in Heroku:  
  - Open your app dashboard
  - Click on ```More``` Option on the right of the Menu bar 
  - Select ```Run Console```
  - Paste the command: 
  ```du -sh * | sort -hr```
  - Press Enter
  
   [Source](https://help.heroku.com/KUFMEES1/my-slug-size-is-too-large-how-can-i-make-it-smaller)
  
- You can add a ```.slugignore``` file (similar to a ```.gitignore``` file we use for git to untrack files while we add/commi)to your application to tell the slug compiler
to ignore any unnecessary files in your application, such as static assets. 

[Source](https://help.heroku.com/KUFMEES1/my-slug-size-is-too-large-how-can-i-make-it-smaller)
  
- View Logs using CLI ```heroku logs --tail```
