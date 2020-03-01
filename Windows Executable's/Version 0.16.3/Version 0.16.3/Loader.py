"""MIT License

Copyright (c) 2019 Zdravko Georgiev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """
from selenium import webdriver
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import urllib.request, time, sys, os,urllib.request, platform , \
    webbrowser,urllib.error, shutil,threading, PySimpleGUI as sg, requests,json

configPath = "data.txt"

if not os.path.isfile(configPath):
    with open(configPath, "a") as f:
        f.writelines \
            ("""
[mainConfig]
downloadlist = 
exercise = True
subtitles = True
savedirectory = 

[GoogleConfig]
bragent = AdsBot-Google (+http://www.google.com/adsbot.html)
hidewindow = True

[Timings]
logintime = 0
loadingallvideos = 5
extractcoursename = 2
getvideolink = 2
downloaddelay = 3

""")
        f.close()

results = ""
config = ConfigParser()
config.read(configPath)

links = str(config.get("mainConfig", "downloadlist")).strip().split("\n")

default_button_color  = '#FFF', '#444'

for lin in links:
    results += lin + "\n"


def build_chrome_options ():

    options = webdriver.ChromeOptions()
    options.accept_untrusted_certs = True
    options.assume_untrusted_cert_issuer = True
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    add_default_chrome_path = ""
    if platform.system() == "Windows":
        add_default_chrome_path = os.path.expanduser('~')  + r"\AppData\Local\Google\Chrome\User Data\Default"
    elif platform.system() == "MacOS" :
        add_default_chrome_path = os.path.expanduser('~') + r"/Library/Application/Support/Google/Chrome/Default"
    elif platform.system() == "Linux" :
        add_default_chrome_path = os.path.expanduser(
            '~') + r"/.config/google-chrome/default"


    options.add_argument("--user-data-dir=" + os.path.abspath(add_default_chrome_path))

    options.add_argument(
        '--user-agent=' + config.get("GoogleConfig","bragent"))
    options.add_argument("--disable-impl-side-painting")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-seccomp-filter-sandbox")
    options.add_argument("--disable-breakpad")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-cast")
    options.add_argument("--disable-cast-streaming-hw-encoding")
    options.add_argument("--disable-cloud-import")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-ipv6")
    options.add_argument("--allow-http-screen-capture")
    options.add_experimental_option("prefs", {
        "download.default_directory": "c:/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    return options
    ##################################################


##################################################
#  Progress bar Class tqdm
###################################################
class progress_bar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def show_progress_bar(url, filename, output_path, type=0, sessions = {}):
    with progress_bar(unit='B',smoothing=0.3, unit_scale=True,
                      miniters=1, desc=filename) as t:
        if type == 0:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)
        else:
            r = requests.get(url, cookies=sessions, stream=True)
            with open(os.path.join(output_path,filename), 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)

class bcolors:
    if os.name == "posix":
        init(autoreset=True)
        # colors foreground text:
        fc = "\033[0;96m"
        fg = "\033[0;92m"
        fw = "\033[0;97m"
        fr = "\033[0;91m"
        fb = "\033[0;94m"
        fy = "\033[0;33m"
        fm = "\033[0;35m"

        # colors background text:
        bc = "\033[46m"
        bg = "\033[42m"
        bw = "\033[47m"
        br = "\033[41m"
        bb = "\033[44m"
        by = "\033[43m"
        bm = "\033[45m"

        # colors style text:
        sd = Style.DIM
        sn = Style.NORMAL
        sb = Style.BRIGHT
    else:
        init(autoreset=True)
        # colors foreground text:
        fc = Fore.CYAN
        fg = Fore.GREEN
        fw = Fore.WHITE
        fr = Fore.RED
        fb = Fore.BLUE
        fy = Fore.YELLOW
        fm = Fore.MAGENTA

        # colors background text:
        bc = Back.CYAN
        bg = Back.GREEN
        bw = Back.WHITE
        br = Back.RED
        bb = Back.BLUE
        by = Fore.YELLOW
        bm = Fore.MAGENTA

        # colors style text:
        sd = Style.DIM
        sn = Style.NORMAL
        sb = Style.BRIGHT


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


config2 = [
    [sg.T("Download Options",size=(500, 1), auto_size_text=True,justification='center', font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(5, 5))],
    [sg.Multiline(tooltip="Add each course link in a row as follows:"
                          "\nhttps://www.linkedin.com/learning/photoshop-cc-2015-new-features-3\nhttps://www.linkedin.com/learning/photoshop-cs6-image-optimization\n https://www.linkedin.com/learning/photoshop-cc-for-photographers-sharpening \n ",
                  font=("Helvetica", 7),
                  autoscroll=True,
                  enable_events=True,
                  enter_submits=True,
                  auto_size_text=True,
                  size=(650,15),
                  default_text=results.strip() + "\n",
                  background_color="#FFF")],
    [sg.Text("Exercise Files", size=(10, 1), pad=(0, 5)),
     sg.Checkbox("",default=config.getboolean("mainConfig", "exercise"), background_color="#FFF"),
     sg.Text(" "* 3, pad=(0, 5)),
     sg.Text("Subtitles", pad=(0, 5)),
     sg.Checkbox("",default=config.getboolean("mainConfig", "subtitles"), background_color="#FFF")

     ],

    [sg.Text("Save Directory", size=(14, 1), pad=(0, 5)),
     sg.InputText(config.get("mainConfig", "saveDirectory"),background_color="#FFF", size=(30,1)),
     sg.FolderBrowse(button_text="Select", button_color=default_button_color, size=(15,1))],
]

config3 = [
    [sg.T("Chrome Driver Options",size=(500, 1),auto_size_text=True,justification='center', font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(5, 5))],
    [sg.T("Browser Agents", size=(13,1))],
    [sg.DropDown(brlist,default_value=config.get("GoogleConfig","bragent"),pad=(5,5), size=(70,10))],
    [sg.Checkbox("Hide Window",default=config.getboolean("GoogleConfig","hidewindow"),pad=(5,5))],
]

config4 = [
    [sg.T("Delay Settings",size=(500, 1),auto_size_text=True,justification='center', font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(5, 5))],
    [sg.T(pad=(5,5),text="Manual Login Delay",size=(20, 1)),
     sg.InputText(size=(5,1), default_text=(config.getint("Timings", "logintime")))],
    [sg.T(pad=(5,5),text="Get Video List Delay",size=(20, 1)),
     sg.InputText(size=(5,1), default_text=(config.getint("Timings", "loadingallvideos")))],
    [sg.T(pad=(5,5),text="Get Course Name Delay",size=(20, 1)),
     sg.InputText(size=(5,1), default_text=(config.getint("Timings", "extractcoursename"))),
     ],
    [sg.T(pad=(5,5),text="Get Video Links Delay",size=(20, 1)),
     sg.InputText(size=(5,1), default_text=(config.getint("Timings", "getvideolink")))],
    [sg.T(pad=(5,5),text="Download Delay",size=(20, 1)),
     sg.InputText(size=(5,1), default_text=(config.getint("Timings", "downloaddelay")))],
]


config5 = [
    [sg.Frame("",layout=(
        [sg.T("LinkedIn Downloader", size=(500, 1), auto_size_text=True, justification='center',
              font=("Arial", 10), background_color="#888", text_color="#FFF", pad=(5, 5))],
        [sg.T("Author: @r00tme", justification='center')],
        [sg.T("Version: GUI 0.16.1", justification='center')],
        [sg.T("Release Date: 29/02/2020", justification='center')],
        [sg.Button(button_text="Bug Report", button_color=default_button_color, size=(10, 1),
                   key="_open_git_link_")]

    ), element_justification="center")]

]

layout = [[sg.TabGroup([[
    sg.Tab('Download', config2),
    sg.Tab('Browser', config3),
    sg.Tab('Timings', config4),
    sg.Tab('About', config5)
]])],
    [
        sg.Button('Start', button_color=default_button_color, size=(15,1), auto_size_button=False),
        sg.Button('Stop', button_color=default_button_color, size=(15,1), auto_size_button=False),
    ]
]

window = sg.Window('LinkedIn Downloader GUI v0.16.3', icon="icon.ico",
                   auto_size_text=True,
                   auto_size_buttons=True,
                   background_color="#d4d0c8",
                   use_default_focus=True,
                   text_justification="left",
                   size=(600,350),
                   debugger_enabled=False,
                   element_justification="left",
                   ).Layout(layout).Finalize()

window.Element('Start').Update(disabled=False)
window.Element('Stop').Update(disabled=True)

valueList = ""

def the_gui():
    while True:
        event, values = window.Read(timeout=100)
        if event is None or event == "Exit":
            break

        if event == "_open_git_link_":
            webbrowser.open('https://github.com/r00tmebaby', new=2)

        if event is not sg.TIMEOUT_KEY:
            counter = 0
            twiliosec = config.sections()

            for sections in twiliosec:
                twilioset = list(config[sections])

                for sets in twilioset:
                    config.set(sections, sets, str(values[counter]))
                    counter += 1

            with open(configPath, "w+") as f:
                config.write(f)

            if event == "Start":
                if not os.path.isfile("chromedriver.exe"):
                    sg.Popup("Chrome Driver is missing, please download it from here http://chromedriver.chromium.org/.\n            The program can not be started without it", button_type=3,auto_close_duration=1, auto_close=True)
                else:
                    event, values = window.Read(timeout=0)
                    if event is None or event == "Exit":
                        break
                    if config.get("mainConfig", "downloadlist") != "" and config.get("mainConfig", "savedirectory") != "":
                        window.Element('Start').Update(disabled=True)
                        window.Element('Stop').Update(disabled=False)
                        threading.Thread(target=downloader).start()

                    else:
                        sg.Popup("Please specify download folder and at least one course url")
            elif event == "Stop":
                os.system('taskkill /f /im chrome.exe')
                os.system('taskkill /f /im chromedriver.exe')

                window.Element('Start').Update(disabled=False)
                window.Element('Stop').Update(disabled=True)

def DownloadFile(url,sessions):
    local_filename = url.split('?')[0]
    file_name = local_filename.split("/")
    file_name1 = file_name[len(file_name) -1]
    r = requests.get(url,cookies=sessions,stream=True)
    with open(file_name1, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return

def downloader():

    driver = webdriver.Chrome("chromedriver.exe", options=build_chrome_options())

    if config.getboolean("GoogleConfig", "hidewindow"):
        driver.set_window_position(-2000, 0)

    sys.stdout.write(

        "\r%s%s###############################################\n"
        "#     LinkedIn Learning Download              #\n"
        "#     @author r00tme    01/03/2020            #\n"
        "#     @version: GUI 0.16.4                    #\n"
        "##############################################\n\n" % (
            bcolors.sd, bcolors.fc))

    sys.stdout.flush()
    if config.getint("Timings", "logintime") > 0:
        driver.get("https://www.linkedin.com/learning-login/?redirect=https%3A%2F%2F")
        time.sleep(config.getint("Timings", "logintime"))

    if not os.path.isfile(configPath):
        sys.stdout.write('\n%s[%s*%s]%s The configuration file does not exist' % (
            bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc))
        sys.stdout.flush()
        sys.exit()

    courses_count = 0
    total_counter = 0

    for items_for_download in links:

        driver.get(items_for_download)

        time.sleep(config.getint("Timings", "loadingallvideos"))
        time.sleep(4)
        driver.find_element_by_css_selector(
            ".course-body__info-tab-name.course-body__info-tab-name-content.ember-view").click()

        counter = 0
        temp_counter = 0

        sys.stdout.write('\n%s[%s*%s]%s Working on course %s' % (
            bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc, items_for_download))
        sys.stdout.flush()

        time.sleep(config.getint("Timings","loadingallvideos"))

        driver.find_element_by_class_name(
            'course-body__info-tab-name-overview').click()


        elementss = driver.find_element_by_class_name("course-info__difficulty").text

        if elementss == "Intermediate":
            prefix = "1-"
        elif elementss == "Advanced":
            prefix = "2-"
        else:
            prefix = "0-"

        course_name = (prefix + items_for_download.split("?")[0].split("/")[4].replace("-", " ").title()).rstrip()

        if not os.path.isdir(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name):
            os.makedirs(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name)
            sys.stdout.write('\n%s[%s*%s]%s Directory %s has been successfully created' % (
                bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc, course_name))
            sys.stdout.flush()
        else:
            sys.stdout.write('\n%s[%s*%s]%s Directory %s already exists' % (
                bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc, course_name))
            sys.stdout.flush()

        time.sleep(1)

        elementss2 = driver.find_element_by_css_selector(
            '.course-info__details-section.course-info__divider').get_attribute('innerHTML')


        if not os.path.isfile(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php") or \
                os.stat(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php").st_size == 0:
            f = open(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php", "a+",
                     encoding="utf-8")
            f.write(elementss2)

        time.sleep(config.getint("Timings", "extractcoursename"))

        all_cookies = driver.get_cookies()
        cookies = {}

        for s_cookie in all_cookies:
            cookies[s_cookie["name"]] = s_cookie["value"]

        if config.getboolean('mainConfig', 'exercise'):
            try:
                driver.find_element_by_class_name("course-body__info-tab-name-exercise-files").click()
                for each_file in driver.find_elements_by_class_name("exercise-file__link"):
                    filename = each_file.get_attribute("href").split("?")[0].split("/")[7]
                    excersize_file = "Downloadig excersise file : %s" % filename
                    show_progress_bar(each_file.get_attribute("href"),
                                      "%s[%s*%s]%s %s" % (
                                          bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fm, excersize_file),
                                      os.path.join(config.get('mainConfig', 'saveDirectory'), course_name,
                                                   filename),
                                      sessions=cookies)
            except:
                sys.stdout.write(
                    "\n%s[%s+%s]%s%s Excercise files were not found" % (bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc,bcolors.sd)
                )

        driver.find_element_by_class_name(
            "course-body__info-tab-name-content").click()
        driver.find_element_by_class_name(
            "course-body__info-tab-name-content").click()

        time.sleep(1)
        video_id = 0
        for k in driver.find_elements_by_class_name("video-item__link"):
            k.click()
            time.sleep(config.getint("Timings", "downloaddelay"))
            try:
                WebDriverWait(driver, time.sleep(config.getint("Timings", "getvideolink"))).until(
                    EC.presence_of_element_located((By.TAG_NAME, "video")))
            except:
                pass

            video_src = driver.find_element_by_tag_name("video").get_attribute("src")

            video_name = driver.current_url.split("/")[5].replace("-", " ").split("?")[0].title()
            course_id = video_src.split("/")[5]

            if counter > 0:
              video_id +=1
            else:
                video_id = json.loads(requests.get(
                    'https://www.lynda.com/ajax/player?courseId=' + course_id + '&type=course').text)['Chapters'][0]['Videos'][counter]['ID']
                fk = open(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\CourseInfo.json", "a+",
                          encoding="utf-8")
                datas= requests.get("https://www.lynda.com/ajax/player/?courseid=%s&type=course" % course_id).json()
                fk.write(json.dumps(datas, indent=4, sort_keys=True))

            video_name = "%04d_%s" % (counter, video_name)
            counter += 1
            time.sleep(0.5)

            save_dir = config.get('mainConfig',
                                  'saveDirectory') + r"\\" + course_name + r"\\" + video_name + ".mp4"
            show_progress_bar(video_src, "\r%s[%s*%s]%s %s" % (bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc, video_name), save_dir)


            if config.getboolean("mainConfig","subtitles"):
                videoSrt = 'https://www.lynda.com/ajax/player/transcript/?courseID=%s&videoID=%s' % (course_id, video_id)

                time.sleep(0.5)
                show_progress_bar(videoSrt, "\r%s[%s*%s]%s %s" % (
                    bcolors.bm,
                    bcolors.fc,
                    bcolors.fm,
                    bcolors.fw,
                    video_name + ".srt"),
                                  os.path.join(config.get('mainConfig', 'saveDirectory'),course_name , video_name + ".srt"),
                                 sessions=cookies)

            total_counter += 1
            temp_counter += 1
            if counter == len(driver.find_elements_by_css_selector(".video-item__link.t-black.ember-view")):
                courses_count += 1
                sys.stdout.write(
                    "\n%s[%s+%s]%s%sYou have successfully downloaded course %s%s %swith %d videos. Downloaded %d courses and %d videos in total\n" % (
                        bcolors.bm, bcolors.fc, bcolors.fm, bcolors.fc,
                        bcolors.sd + bcolors.fc, bcolors.sb + bcolors.fg, course_name,
                        bcolors.sd + bcolors.fc, temp_counter, courses_count, total_counter)
                )
                break
            sys.stdout.flush()

if __name__ == '__main__':
    the_gui()
