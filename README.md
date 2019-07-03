# LinkedIn-Downloader
LinkedIn DL  is a small GUI program coded with Python and based on my previous Lynda Download script.

<img src="https://i.imgur.com/SrpYArO.png"></img>

<b>What it does?</b></br>
LinkedIn GUI version is capable to download multiple courses from LinkedIn Learning by a given list.

<b>About the program</b></br>
 The program is based on SeleniumWebDriver library and is written in python and the code converted to executable. My idea was to make it easier for using since not everyone is familiar with python, consoles, libraries and so on, but anyone can run a simple exe file. So said, you do not need to have python or libraies installed on your pc to run the program, everything is built in the exe istelf. Of course the downside is that it can be only run on Windows operation system. Obviously this is not the best solution, not even the fastest but the target here is to have easy for using, free and functional program. So following production standarts (which I am not aware of anyway) does not make any sense here.
 

<b>How to use the program</b>


You have three tabs Login, Download and Browser


 - <b>Login Tab </b>
 </br>
 <img src="https://i.gyazo.com/60b606fede2e4e8c1327d56f5f140aee.png"></img>
 
  You have to fill the fields with your LinkedIn Learning username(email address) and password. If the Login is checked the program will try to login into LinkedIn with the given credentials. If for some reason the program does not login succesfully you can do it manualy and then re-run the program with "Use Profile" checkbox under the Browser tab checked and "Login" unchecked . The program will try to open LinkedIn with the saved in the broswer user profile credentials.
  <img src="https://i.gyazo.com/4aa664cd791f5291231e54ddb84ddf70.png"></img>
  
 - <b>Download Tab  <img src="https://i.gyazo.com/ac9eb0ab9289db6e3c1a5001c035ad42.png"></img>
  
  
  As shown in the image the first field is for the courses. Each course link must be placed in a row, one above another. No other separators like comas, semicolumns or one after another with space will be recognised. 
  The second field is for the directory which will be used to save all downloaded courses.
  
  
 - <b>Browser Tab  <img src="https://i.gyazo.com/60b606fede2e4e8c1327d56f5f140aee.png"></img></b></br>
  
  
  Here you can change the browser agent, this is in favour if you want to replace your original chrome browser agent with another, say mobile, safary or firefox etc. For the planned updates with built in proxy and vpn options this setting will become more usefull, for now is as a placeholder. It works now but does not make a lot of sence beacause you have to use another VPN service.
  
  The extra checkboxes are for the browser extensions, browser window (unselected checkbox will hide the browser window), GPU rendering, Using user profile, sandbox.   
  
<b>Completed:</b>
- Automatic Login to LinkedIn
- Enabling/Disabling Chrome extensions 
- Change Browser Agent
- Select Downloading Folder
- Add Courses List
- Working in Background and Windowed
- Option to save credentials from the browser, so after the first successful login if this option is selected the program will use the session.

<b>TODO Next:</b>
 - Proxy functionality and/or VPN
 - Improving the overall GUI look
 - Adding An Advanced Options Menu which will include specific sleep times to control the software behaviour more precisely
 - Capability to download Exercise Files (That was included in my LyndaDl script but not here)
 - Capability to download Transcripts 
 - Capability to separate the videos in chapters, so each chapter will have a particular folder with videos inside the course folder
 - Capability to choose the video quality before starting the program
 - Burning subtitles *in facts this functionality was implemented but I found difficulties to match the subtitles timings with the video precisely and had to remove it as became after all unreliable function. I am still looking to find a permanent solution.
 
 If you have any advice, recommendations or ideas for additional functionalities they are very welcome. 
 
 Should you find any bugs or problems, please let me know so I can fix them accordingly.
