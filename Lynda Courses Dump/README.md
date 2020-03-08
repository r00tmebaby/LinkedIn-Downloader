# Lynda Courses List Download

With this script you can download all lynda courses available for download either premium and/or free. This can be helpfull and safe your time by trolling around the website with seraching for the courses that you may need. Instead, you can dump the whole database and select the courses you are interested in for download.

</br>

The script is simple for usage some configurations are at the very top such as maximum possible category wich is set to 2000 by default but the categories may increase after they add new courses.The script does not save temporary lists but keep it in the memory to improve the speed which means that if you interupt it while it is still working a text file with courses wont be created, so bare that in mind.

</br>

<b>Config:</b></br>
startCategory = 1     -Starting category/course</br>
page = 1              -Starting page</br>
showMessage = True    -Should you want to see messages while the program works (slows down the whole proccess since python has to print it out)</br>
maxCategory = 2000    -Maximal possible categories</br>
