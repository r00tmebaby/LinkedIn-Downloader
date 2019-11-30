# LinkedIn-Downloader
LinkedIn DL  is a small GUI program coded with Python and based on my previous Lynda Download script.

<img src="https://i.imgur.com/SrpYArO.png"></img><br>
<b>Video Tutorials</b></br>

Version 1.11 https://www.youtube.com/watch?v=n-qCC6SiKgc&feature=youtu.be</br>
Version 1.14 https://www.youtube.com/watch?v=6E2wi-oJVTE
<br><br>
<b>What it does?</b></br>
LinkedIn GUI version is capable to download multiple courses from LinkedIn Learning by a given list. It creates separate folder for each course and rename all downloaded vides with generated numbers to be able to be ordered lexicographically properly by your windows.

<b>More about the program</b></br>
 The program is based on SeleniumWebDriver library and is written in python and the code converted to executable. My idea was to make it easier for using since not everyone is familiar with python, consoles, libraries and so on, but anyone can run a simple exe file. So said, you do not need to have python or libraies installed on your pc to run the program, everything is built in the exe istelf. Of course the downside is that it can be only run on Windows operation system. Obviously this is not the best solution, not even the fastest but the target here is to have easy for using, free and functional program. 
 

<b>How to use the program</b>
You have five tabs Login, Download, Browser, Timings and About


 - <b>Login Tab </b></br>
  <img src="https://i.gyazo.com/bd85da3f61163956f8e234106e5aa6d2.png"></img>
 </br>
   You have to fill the fields with your LinkedIn Learning username(email address) and password. If the Login is checked the program        will try to login into LinkedIn with the given credentials. If for some reason the program does not login succesfully you can do        it manualy and then re-run the program with "Use Profile" checkbox under the Browser tab checked and "Login" unchecked. The program      will try to open LinkedIn with the saved in the broswer user profile credentials.
</br>
  
 - <b>Download Tab </b> </br>
<img src="https://i.gyazo.com/897e1fd6c42eb5f24dfa7a91b28d4679.png"></img></br>
  
   As shown in the image the first field is for the courses. Each course link must be placed in a row, one above another. No other          separators like comas, semicolumns or one after another with space will be recognised. 
   The second field is for the directory which will be used to save all downloaded courses.</br>
  
  
 - <b>Browser Tab </b></br>
 <img src="https://i.gyazo.com/e8b69412e3572f283c99ff418d146d0e.png"></img></br>
     Here you can change the browser agent, this is in favour if you want to replace your original chrome browser agent with another, say    mobile, safary or firefox etc.
   The extra checkboxes are for the browser extensions, browser window (unselected checkbox will hide the browser window), GPU              rendering, Using user profile, sandbox.  </br>
   
 - <b>Timings Tab</b></br>
 <img src="https://i.gyazo.com/ab261d35d66daebea23a9e47f5eca874.png"></img></br>
 Added an option to delay the login so you can use that time to manually login to linkedIn. This is very handy if you login to Linkedin via organisation portal. Once you login successfully, close the browser window and then restart the program. The program will search for the saved credentials and try to open LinkedIn directly without need to login (uncheck the login checkbox before starting the program).

  
<b>Completed:</b>
- Automatic Login to LinkedIn
- Enabling/Disabling Chrome extensions 
- Change Browser Agent
- Select Downloading Folder
- Add Courses List. Add every course line by line
- Working in Background and Windowed
- Option to save credentials from the browser, so after the first successful login if this option is selected the program will use the session.

</br>
<b>Version 1.16:</b>
<p>Added</p>
  + Download Subtitles</br>
  + Download Exercise Files</br>
  
 <p>Removed</p>
  - Apply Button (redundant option, now the program save the course list automatically)</br>
  - Browser Extension Options (all required are set by default)</br>
  - Removed loader.py file, now it works as a thread </br>
  
 <p>Improvements</p>
  - Stability</br>
  - GUI Look</br>
</br>

<b>Version 1.14:</b>
- Fixed an issue #10. Program stops working if "Quiz" is found instead of video file

<b>Version 1.13:</b>
- Added an option to delay options. 
- Added options to delay the overall downloading process precisely so you can control its behaviour
- Added macOS and Linux browser credentials support 
- Improved the overall GUI look 
- Password field is no longer in plain text but masked with stars
- Add an option to edit the user agent field and put your own

<b>Version 1.11:</b>
   - Fixed issue reported in #3 and #4. Downloading first video twice and skipping the last video
   - Fixed issue with an empty course download list, program runtime error.
   - Improved messages
   
<b>TODO Next:</b>
 - Improving the overall GUI look
 - Capability to download Exercise Files (That was included in my LyndaDl script but not here)
 - Capability to download Transcripts 
 - Capability to separate the videos in chapters, so each chapter will have a particular folder with videos inside the course folder
 - Capability to choose the video quality before starting the program
 - Burning subtitles *in facts this functionality was implemented but I found difficulties to match the subtitles timings with the video precisely and had to remove it as became after all unreliable function. I am still looking to find a permanent solution.
 
 If you have any advice, recommendations or ideas for additional functionalities they are very welcome. 
 
 Should you find any bugs or problems, please let me know so I can fix them accordingly.
