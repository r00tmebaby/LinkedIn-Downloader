import PySimpleGUI as sg
from configparser import ConfigParser
import os, subprocess


configPath = "Storage.dll"
results = ""
try:
    open(configPath,"r")
except:
    with open(configPath, "a") as f:
        f.writelines("[mainConfig] \n\
login = True\n\
loginuser = \n\
loginpass =  \n\
downloadlist = \n\
savedirectory = \n\
[GoogleConfig]\n\
bragent = Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko\n\
extensions = True\n\
sandbox = True\n\
usrProfile = True\n\
window = True\n\
gpu = True\n\
                ")
        f.close()


config = ConfigParser()
config.read(configPath)

links = str(config.get("mainConfig", "downloadlist")).split(",")
for lin in links:
    results += lin + "\n"


brlist = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla / 5.0(compatible; bingbot / 2.0; +http://www.bing.com/bingbot.htm)",
    "AdsBot-Google (+http://www.google.com/adsbot.html)",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
]

config1 = [
[sg.T(text=" "*4 + " Login Options",size=(90,1), font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(10,10))],
               [sg.Text("Login", size=(14, 1), pad=(0, 5)), sg.Checkbox(text="", default=(config.getboolean("mainConfig", "login"))), ],
               [sg.Text("Username", size=(14, 1), pad=(0, 5)), sg.InputText(default_text=(config.get("mainConfig", "loginUser")))],
               [sg.Text("Password", size=(14, 1), pad=(0, 5)), sg.InputText(default_text=config.get("mainConfig", "loginPass"))],
]
config2 = [
               [sg.T(text=" "*4 + " Download Options",size=(90,1), font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(10,10))],
               #[sg.Text("Download List", size=(14, 1), pad=(0, 5)), sg.InputText(config.get("mainConfig", "coursesList"),background_color="#FFF", font=22), sg.FileBrowse(button_text="Select", size=(5,1))],
               [sg.Text("Courses List", size=(13,1)) ,
                sg.Multiline(tooltip="Add each course link in a row as follows:"
                                    "\nhttps://www.linkedin.com/learning/photoshop-cc-2015-new-features-3\nhttps://www.linkedin.com/learning/photoshop-cs6-image-optimization\n https://www.linkedin.com/learning/photoshop-cc-for-photographers-sharpening \n "
                                    ,font=("Helvetica", 7),autoscroll=True, enable_events=True, enter_submits=True,auto_size_text=True, size=(85, 5), key="key1", default_text=results,background_color="#FFF"), sg.Button("Apply")],
               [sg.Text("Save Directory", size=(14, 1), pad=(0, 5)), sg.InputText(config.get("mainConfig", "saveDirectory"),background_color="#FFF", size=(68,1)), sg.FolderBrowse(button_text="Select",size=(6,1))],
]

config3 = [
[sg.T(text=" "*4 + " Chrome Driver Options",size=(60,1), font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(10,10))],
    [sg.T("Browser Agents", size=(13,1))],
              [sg.DropDown(brlist, readonly=True,default_value=config.get("GoogleConfig","bragent"),pad=(5,5), size=(90,3))],
[sg.Checkbox(pad=(5,5),text="Extensions",tooltip="Enable/Disable browser extensions ",default=config.getboolean("GoogleConfig", "extensions"))],
[sg.Checkbox(pad=(5,5),text="Window", tooltip="Show browser window", default=config.getboolean("GoogleConfig", "extensions"))],
[sg.Checkbox(pad=(5,5),text="GPU",tooltip="Add/Remove browser GPU rendering", default=config.getboolean("GoogleConfig", "extensions"))],
[sg.Checkbox(pad=(5,5),text="Use Profile", tooltip=("Trying to use saved login credentials"),default=config.getboolean("GoogleConfig", "extensions"))],
[sg.Checkbox(pad=(5,5),text="Sandbox",tooltip="Using Sandbox",default=config.getboolean("GoogleConfig", "extensions"))]
]

layout = [[sg.TabGroup([[sg.Tab('Login', config1),sg.Tab('Download', config2),sg.Tab('Browser', config3)]])],
           [sg.Button('Start', button_color=('#FFF', '#444'),size=(15,1), auto_size_button=False),sg.Button('Stop', button_color=('#FFF', '#444'), size=(15,1), auto_size_button=False),sg.Button('Restart', button_color=('#FFF', '#444'), size=(15,1), auto_size_button=False)],
          ]

window = sg.Window('LinkedIn Downloader GUI v0.11   26/07/2019', icon="",
                   auto_size_text=False,
                   auto_size_buttons=True,
                   background_color="#d4d0c8",
                   default_element_size=(46,1),
                   use_default_focus=True,
                   text_justification="left"
                   ).Layout(layout).Finalize()

window.Element('Start').Update(disabled=False)
window.Element('Stop').Update(disabled=True)
window.Element('Restart').Update(disabled=True)

valueList = ""
while True:
    event, values = window.Read(timeout=0)
    if event is None or event == "Exit":
          break
    if event is not sg.TIMEOUT_KEY:

        config.set('mainConfig', 'loginuser', str(values[1]).strip())
        config.set('mainConfig', 'loginpass', str(values[2]).strip())
        config.set('GoogleConfig', 'bragent', str(values[4]))
        if type(values[0]) == bool:
            config.set('mainConfig', 'login', str(values[0]))

        if type(values[4]) == bool:
            config.set('GoogleConfig', 'extensions', str(values[5]))

        if type(values[5]) == bool:
            config.set('GoogleConfig', 'window', str(values[6]))
        if type(values[6]) == bool:
            config.set('GoogleConfig', 'gpu', str(values[7]))
        if type(values[7]) == bool:
            config.set('GoogleConfig', 'usrProfile', str(values[8]))
        if type(values[8]) == bool:
            config.set('GoogleConfig', 'sandbox', str(values[9]))




        if os.path.isdir(values[3]):
            config.set('mainConfig', 'savedirectory', str(values[3]))

        if event == "Apply":
            config.set('mainConfig', 'downloadlist', ",".join(str(values["key1"]).split()) + ",")
            sg.Popup("Download list is updated")

        with open(configPath, "w+") as f:
            config.write(f)

        if event == "Start":
            os.system('taskkill /f /im chrome.exe')
            os.system('taskkill /f /im program.exe')
            os.system('taskkill /f /im chromedriver.exe')
            if not os.path.isfile("chromedriver.exe"):
                  sg.Popup("Chrome Driver is missing, please download it from here http://chromedriver.chromium.org/.\n            The program can not be started without it", button_type=3,auto_close_duration=1, auto_close=True)
            else:
                if config.get("mainConfig", "downloadlist") != "" and config.get("mainConfig", "savedirectory") != "":
                    window.Element('Start').Update(disabled=True)
                    window.Element('Stop').Update(disabled=False)
                    window.Element('Restart').Update(disabled=False)
                    subprocess.Popen("python loader.py")
                else:
                    sg.Popup("Please specify download folder and at least one course url")
        elif event == "Stop":
            window.Element('Start').Update(disabled=False)
            window.Element('Stop').Update(disabled=True)
            window.Element('Restart').Update(disabled=True)
            os.system('taskkill /f /im chrome.exe')
            os.system('taskkill /f /im program.exe')
            os.system('taskkill /f /im chromedriver.exe')

        elif event == "Restart":
            window.Element('Start').Update(disabled=True)
            window.Element('Stop').Update(disabled=False)
            window.Element('Restart').Update(disabled=False)
            os.system('taskkill /f /im chrome.exe')
            os.system('taskkill /f /im program.exe')
            os.system('taskkill /f /im chromedriver.exe')
            subprocess.Popen("python loader.py")


