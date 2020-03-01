# LinkedIn-Downloader
LinkedIn DL  is a small GUI program coded with Python and based on my previous Lynda Download script.
<image src="https://i.gyazo.com/6a863b99d7f27552c6408d49994f865e.png"><br>
<img src="https://i.imgur.com/SrpYArO.png"></img><br>
<b>Video Tutorials</b></br>

Latest Executable Version 0.16.4 </br>
Version 0.14 https://www.youtube.com/watch?v=6E2wi-oJVTE</br>
Version 0.11 https://www.youtube.com/watch?v=n-qCC6SiKgc&feature=youtu.be</br>

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
- Change Browser Agent
- Select Downloading Folder
- Download Subtitles
- Download Excercise Files
- Add Courses List. Add every course line by line
- Working in Background and Windowed mode
- Option to save credentials from the browser, so after the first successful login if this option is selected the program will use the session.

</br>
<b>Version 0.16.4 is executable only:</b></br>
   + Fixed excercise checkbox (on/off) does not work properly</br>
   + Adding a json file containing all available course information for that can be used for an additional developments</br>
   - Removed Login menu completelly as I found it redundant and very time consuming to maintain it working. Linked in always change the login style so most stable way remains manual login</br>
   * An attempt to fix the subtitles. Unfortunatelly still not working in all ocasions. Will have to spend some more time for reverse-engineering to analyse the issue deeply and find a fix.</br>
 
</br>
</br>
<b>Version 0.16 is executable only:</b><br>
  + Download Subtitles</br>
  + Download Exercise Files</br> 
  + Reworked Download Algorithm to improve stability</br>
  + Improved Login (addapted to the new linkedin login)</br>
  + Improved GUI</br>
  - Removed Apply Button (redundant option, now the program save the course list automatically)</br>
  - Removed Browser Extension Options (all required are set by default)</br>
  - Removed loader.py file, now it works as a thread </br>  
</br>

<b>Version 0.14:</b>
- Fixed an issue #10. Program stops working if "Quiz" is found instead of video file

<b>Version 0.13:</b><br>
- Added an option to delay options. 
- Added options to delay the overall downloading process precisely so you can control its behaviour
- Added macOS and Linux browser credentials support 
- Improved the overall GUI look 
- Password field is no longer in plain text but masked with stars
- Add an option to edit the user agent field and put your own

<b>Version 0.11:</b>
   - Fixed issue reported in #3 and #4. Downloading first video twice and skipping the last video
   - Fixed issue with an empty course download list, program runtime error.
   - Improved messages
   
<b>TODO Next:</b>
  <b> No future updates are planed</b>
 
