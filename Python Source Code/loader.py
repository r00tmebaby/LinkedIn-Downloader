import urllib.request, ssl, urllib3, time, sys, random, os
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

configPath = "Storage.dll"
config = ConfigParser()
config.read(configPath)

class Main:

    def driver(self, browser_type=1, driver_path='chromedriver.exe'):
        if browser_type == 1:
            driver = webdriver.Chrome(driver_path, chrome_options=self.build_chrome_options())
        elif browser_type == 2:
            driver = webdriver.Firefox(driver_path)
        elif browser_type == 3:
            driver = webdriver.Safari(driver_path)
        elif browser_type == 4:
            driver = webdriver.Opera(driver_path)
        else:
            driver = webdriver.Chrome(driver_path)
        return driver

    # Static Method Download Download File
    ###################################################
    @staticmethod
    def download(url, names):
        urllib3.disable_warnings()

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        if urllib.request.urlretrieve(url, names):
            return True
        else:
            return False

    def build_chrome_options (self):

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
            options.add_argument("--user-data-dir=" + os.path.abspath(
                os.path.expanduser('~') + r"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"))

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

    # Static Method Download Download File
    ###################################################
    @staticmethod
    def download(url, names):
        urllib3.disable_warnings()

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        if urllib.request.urlretrieve(url, names):
            return True
        else:
            return False
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

    ##################################################
    #  Method checking whether the directory exists or not
    # @param  Directory Path String
    ###################################################
    def dir_exist(self, path):
        if Path(path).is_dir():
            return True
        else:
            return False



    def Downloader():

    
        main = Main()  # Calling Main Class
        sys.stdout.write(
            "\r%s%s###############################################\n"
            "#     LinkedIn Learning Downloading Script    #\n"
            "#     @author r00tmebaby  10/06/2019          #\n"
            "#     @version: GUI 0.1                       #\n"
            "#     Downloading with Pre-Specified List     #\n"
            "##############################################\n\n" % (
                main.bcolors.sd, main.bcolors.fc))
    
        sys.stdout.flush()
        driver = main.driver(1, "chromedriver.exe")

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
        for items_for_download in links:
            counter = 0
            temp_counter = 0
            sys.stdout.write('\n%s[%s*%s]%s Working on course %s' % (
                main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, items_for_download))
            sys.stdout.flush()
            time.sleep(random.randint(2, 5))
            driver.get(items_for_download)
            time.sleep(random.randint(2, 5))
            try:
                driver.find_element_by_class_name(
                    'course-body__info-tab-name-overview').click()
            except:
                time.sleep(1)
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
            time.sleep(0.2)
    
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
    
            driver.find_element_by_css_selector('.video-item__link.t-black.ember-view:nth-child(1)').click()
            course = driver.find_elements_by_css_selector('.video-item__link.t-black.ember-view')
    
            for eems in course:
    
                time.sleep(random.randint(3, 6))
                counter += 1
                try:
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "error-body__illustration")))
                except:
                    pass
                try:
                    eems.click()
                except:
                    time.sleep(1)
                    eems.click()
                try:
                    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.TAG_NAME, "video")))
                finally:
                    video = driver.find_element_by_tag_name('video')
                    url_temp = video.get_attribute('src')
                    video_name = driver.current_url.split("/")[5].replace("-", " ").split("?")[0].title()
                    time.sleep(0.2)
                    video_name = "%04d_%s_%s" % (counter, video_name, "-")
                    save_dir = config.get('mainConfig', 'saveDirectory') + r"\\" + course_name + r"\\" + video_name + ".mp4"
                    if not main.file_exist(save_dir):
                        time.sleep(0.5)
                        main.download(url_temp, save_dir)
                        main.show_progress_bar(url_temp, "\r" + "%s[%s*%s]%s %s" % (main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, video_name), save_dir)
                        total_counter += 1
                        temp_counter += 1
                    else:
                        sys.stdout.write("\n%s[%s-%s]%s%s%s File %s already exist. Skipped!" % (
                            main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc,
                            main.bcolors.sb, main.bcolors.fr, video_name + ".mp4"))
                        sys.stdout.flush()
    
    
                if counter == len(course):
                    courses_count += 1
                    sys.stdout.write(
                        "\n%s[%s+%s]%s%sYou have successfully downloaded course %s%s %swith %d videos. Downloaded %d courses and %d videos in total" % (
                            main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc,
                            main.bcolors.sd + main.bcolors.fc, main.bcolors.sb + main.bcolors.fc, course_name,
                            main.bcolors.sd + main.bcolors.fc, temp_counter, courses_count, total_counter)
                    )
                sys.stdout.flush()


Main.Downloader()