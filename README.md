<h1> Just a quick login-demo! </h1>

This shows python script in action doing login!

1. Do this first <br>
<code> pip install -r requirements.txt</code>
2. Then run the main script and see the magic<br>
<code>python main.py </code><br>

<h2>Snapshot</h2>
<img src='https://github.com/user-attachments/assets/c92f359d-d031-41ae-9c19-6b5e3783c484' style='width: 600px'>


<h2> How It Works </h2>
<ol>
  <li>Reads credentials.json file -> Then stores those username and passwords</li>
  <li> Automatically downloads chromedriver & initializes it</li>
  <li>Opens First site -> Logs in with creds </li>
  <li>Verifies Login Success for first site</li>
  <li>Goes to the next site -> Logs in with creds</li>
  <li>Verifies Login Success for the second site</li>
  <li>Stores the snapshots for the both in -> "./reports/" directory</li>
