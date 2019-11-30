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


import urllib.request, ssl, urllib3, time, sys, os
from selenium import webdriver
from pathlib import Path
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import urllib.request, platform
import urllib.error, shutil

configPath = "Storage.dll"
config = ConfigParser()
config.read(configPath)


class Main:


    def driver(self,browser_type=1, driver_path='chromedriver.exe'):
        if browser_type == 1:
            driver = webdriver.Chrome(driver_path, options=self.build_chrome_options())
        elif browser_type == 2:
            driver = webdriver.Firefox(driver_path)
        elif browser_type == 3:
            driver = webdriver.Safari(driver_path)
        elif browser_type == 4:
            driver = webdriver.Opera(driver_path)
        else:
            driver = webdriver.Chrome(driver_path)
        return driver

    @staticmethod
    def remove(path):
        """ param <path> could either be relative or absolute. """
        if os.path.isfile(path):
            os.remove(path)  # remove the file
        elif os.path.isdir(path):
            shutil.rmtree(path)  # remove dir and all contains
        else:
            raise ValueError("file {} is not a file or dir.".format(path))



    @staticmethod
    def build_chrome_options ():

        options = webdriver.ChromeOptions()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        if config.getboolean("GoogleConfig", "extensions") == True:
           options.add_argument("--disable-extensions")
        if config.getboolean("GoogleConfig", "sandbox") == True:
           options.add_argument("--no-sandbox")
        if config.getboolean("GoogleConfig", "window") == False:
           options.add_argument("--headless")
        if config.getboolean("GoogleConfig", "gpu") == True:
           options.add_argument("--disable-gpu")
        if config.getboolean("GoogleConfig", "usrProfile"):
            if platform.system() == "Windows":
                add_default_chrome_path = os.path.expanduser('~')  + r"\AppData\Local\Google\Chrome\User Data\Default"
            elif platform.system() == "MacOS" :
                add_default_chrome_path = os.path.expanduser('~') + r"/Library/Application/Support/Google/Chrome/Default"
            elif platform.system() == "Linux" :
                add_default_chrome_path = os.path.expanduser(
                    '~') + r"/.config/google-chrome/default"
            else:
                add_default_chrome_path = ""
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

    def show_progress_bar(self, url, filename, output_path):
        with self.progress_bar(unit='B',smoothing=0.3, unit_scale=True,
                                 miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

    ##################################################
    #  Background and Font Colours
    # Reference => *Nasir Khan (r0ot h3x49)  - **https://github.com/r0oth3x49** ##*
    ###################################################
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

    ##################################################
    #  Method Waits wait time
    # @param  wait Integer
    ###################################################

    def waits(self, wait):
        self.driver().implicitly_wait(wait)

    ##################################################
    #  Method Maximizing Window
    # @param  m_window Boolean -> True by Default
    ###################################################

    def max_window(self, m_window=True):
        if m_window:
            self.driver().maximize_window()

    ##################################################
    #  Method Looking for file existence before downloading
    # @param  m_window Boolean -> True by Default
    ###################################################
    def file_exist(self, path):

        if Path(path).is_file():
            return True
        else:
            return False

    @staticmethod
    def is_bad_proxy(proxy):
        try:
            proxy_handler = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            req = urllib.request.Request('http://www.google.com')  # change the URL to test here
            sock = urllib.request.urlopen(req)
        except Exception as detail:
            return True
        return False

    ##################################################
    #  Method checking whether the directory exists or not
    # @param  Directory Path String
    ###################################################
    def dir_exist(self, path):
        if Path(path).is_dir():
            return True
        else:
            return False

    @staticmethod
    def downloader():

        main = Main()  # Calling Main Class
        sys.stdout.write(
            "\r%s%s###############################################\n"
            "#     LinkedIn Learning Download              #\n"
            "#     @author r00tme    28/10/2019          #\n"
            "#     @version: GUI 0.14                      #\n"
            "##############################################\n\n" % (
                main.bcolors.sd, main.bcolors.fc))

        sys.stdout.flush()
        driver = main.driver(1, "chromedriver.exe")
        time.sleep(config.getint("Timings", "logintime"))

        if config.getboolean('mainConfig', 'login'):
            sys.stdout.write('\n%s[%s*%s]%s Trying to login on LinkedIn' % (
                main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc))
            sys.stdout.flush()
            driver.get("https://www.linkedin.com/learning/login")
            action = ActionChains(driver)
            for i in range(4):
                time.sleep(.1)
                action.send_keys(Keys.TAB)
                time.sleep(.1)
                action.send_keys(config.get('mainConfig', 'loginUser'))
                time.sleep(.1)
                action.send_keys(Keys.TAB)
                time.sleep(.1)
                action.send_keys(config.get('mainConfig', 'loginPass'))
                time.sleep(.1)
                action.send_keys(Keys.ENTER)
                time.sleep(.1)
            action.perform()
    
        if not main.file_exist(configPath):
            sys.stdout.write('\n%s[%s*%s]%s The configuration file does not exist' % (
                main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc))
            sys.stdout.flush()
            sys.exit()
        courses_count = 0  # Courses Counter
        total_counter = 0  # Counting the total videos downloaded
        prefix = ""  # This prefix will be put on front of every course to mark its difficulty level

        links = str(config.get("mainConfig", "downloadlist")).split(",")
        link2 = filter(None, links)
        for items_for_download in link2:
            counter = 0
            temp_counter = 0
            time.sleep(config.getint("Timings", "loadingallvideos"))
            driver.get(items_for_download)
            sys.stdout.write('\n%s[%s*%s]%s Working on course %s' % (
                main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, items_for_download))
            sys.stdout.flush()
            time.sleep(config.getint("Timings", "loadingallvideos"))
            try:
                driver.find_element_by_class_name(
                    'course-body__info-tab-name-overview').click()
            except:
                time.sleep(config.getint("Timings", "extractcoursename"))
                try:
                    driver.find_element_by_class_name(
                        'course-body__info-tab-name-overview').click()
                except:
                    continue
            elementss = driver.find_element_by_class_name("course-info__difficulty").text

            if elementss == "Intermediate":
                prefix = "1-"
            elif elementss == "Advanced":
                prefix = "2-"
            else:
                prefix = "0-"

            course_name = (prefix + items_for_download.split("?")[0].split("/")[4].replace("-", " ").title()).rstrip()
            time.sleep(config.getint("Timings", "extractcoursename"))

            if not main.dir_exist(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name):
                os.makedirs(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name)
                sys.stdout.write('\n%s[%s*%s]%s Directory %s has been successfully created' % (
                    main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, course_name))
                sys.stdout.flush()
            elementss2 = driver.find_element_by_css_selector(
                '.course-info__details-section.course-info__divider').get_attribute('innerHTML')

            if not main.file_exist(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php") or \
                    os.stat(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php").st_size == 0:
                f = open(config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\info.php", "a+",
                         encoding="utf-8")
                f.write(elementss2)
            driver.find_element_by_css_selector(
                ".course-body__info-tab-name.course-body__info-tab-name-content.ember-view").click()
            time.sleep(config.getint("Timings", "extractcoursename"))
            course = driver.find_elements_by_css_selector('.video-item__link.t-black.ember-view')
            time.sleep(config.getint("Timings", "extractcoursename"))
            driver.find_element_by_css_selector('.video-item__link.t-black.ember-view').click()
            time.sleep(config.getint("Timings", "extractcoursename"))
            download_list = []

            while True:
                try:
                    WebDriverWait(driver, time.sleep(config.getint("Timings", "getvideolink"))).until(EC.element_to_be_clickable((By.CLASS_NAME, "error-body__illustration")))
                except:
                    pass
                try:
                   video = driver.find_element_by_tag_name('video')
                   url_temp = video.get_attribute('src')
                   video_name = driver.current_url.split("/")[5].replace("-", " ").split("?")[0].title()
                except:
                     continue


                save_dir_t = config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\\" + video_name + ".mp4"
                if not main.file_exist(save_dir_t) and  not (video_name in download_list):
                    time.sleep(config.getint("Timings", "downloaddelay"))
                    counter += 1
                    video_name = "%04d_%s_%s" % (counter, video_name, "-")
                    save_dir = config.get('mainConfig',
                                            'saveDirectory') + r"\\" + course_name + r"\\" + video_name + ".mp4"
                    main.show_progress_bar(url_temp, "\r" + "%s[%s*%s]%s %s" % (main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, video_name), save_dir)
                    driver.find_element_by_css_selector(".vjs-control.vjs-button.vjs-next-button").click()
                    total_counter += 1
                    download_list.append(video_name.split("_")[1])
                    temp_counter += 1
                    time.sleep(config.getint("Timings", "downloaddelay"))

                else:
                    Main.remove(save_dir_t)

                if counter == len(course):
                    courses_count += 1
                    sys.stdout.write(
                        "\n%s[%s+%s]%s%sYou have successfully downloaded course %s%s %swith %d videos. Downloaded %d courses and %d videos in total" % (
                            main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc,
                            main.bcolors.sd + main.bcolors.fc, main.bcolors.sb + main.bcolors.fc, course_name,
                            main.bcolors.sd + main.bcolors.fc, temp_counter, courses_count, total_counter)
                    )
                    break
                sys.stdout.flush()

Main.downloader()
