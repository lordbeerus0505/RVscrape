#import BeautifulSoup4
import webbrowser
import requests
import mechanicalsoup

def scrape(url,j):
    #webbrowser.open(url)
    res=requests.get(url)
    if j<10:
        j="00"+str(j)
    elif j<100:
       j="0"+str(j)
    #change branch / usn here
    usn="1RV16CS"+j
    #print(usn)
    #print(res.text)
    browser=mechanicalsoup.StatefulBrowser()
    browser.open(url)
    browser.select_form()
    browser["usn"]=usn
    count=0
    sum=0
    for i in res.text:
        count=count+1
        if i in '+':
            # print(res.text[count-3])
            # print(res.text[count+1])
            lhs=res.text[count-3]
            rhs=res.text[count+1]
            sum=int(lhs)+int(rhs)
            break
    #sum=str(sum)
    #print(sum)

    #hardcoded for now as requests creates a new instance of browser, fix in next update.

    browser["captcha"]='10'
    #browser.launch_browser()



    browser.submit_selected()



    string=browser.get_current_page().text
    #print(string)
    #print("Checking if matching")
    count=0
    if "SGPA" in string:
        browser.launch_browser()
        # for i in string:
        #     count=count+1
        #     if "SGPA" in i:
        #         print(string[count])

        #use this to display result on console
        #print(string)


        #Use this to stop after each output
        #input("Press any key to continue")
        return True













url='http://results.rvce.edu.in'

for j in range(1,200):
    for i in range(50):
        if scrape(url, j)==True:
            break
