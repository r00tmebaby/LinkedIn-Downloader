import requests as r, re

newUrlList = []
startCategory = 1
page = 1
showMessage = True
maxCategory = 2000

def sorting(x):
  return list(dict.fromkeys(x))

while startCategory <= maxCategory:
    details = r.get(url=("https://www.lynda.com/ajax/category/%s/courses?page=%s" % (startCategory, page)))
    allUrls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', details.text)
    if showMessage:
        print("[*] Scraping courses from https://www.lynda.com/ajax/category/%s/courses?page=%s" % (startCategory, page))
        print("  - %s courses are added " % len(allUrls))
    if len(allUrls) > 2:
        for links in allUrls:
            if links[-2:] == 'l\\':
                newUrlList.append(links[:-1])
        page +=1
    else:
        startCategory +=1
        page = 1
    if startCategory == maxCategory:
        mylist = sorting(newUrlList)
        mylist.sort()
        for allcourses in mylist:
                open("LyndaCourseList.txt", "a+").write(allcourses + "\n")


