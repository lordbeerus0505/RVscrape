#import BeautifulSoup4
import webbrowser
import requests
import mechanicalsoup
import Database

count1=0

def scrape(url,j):
    global count1
    #webbrowser.open(url)
    res=requests.get(url)
    if j<10:
        j="00"+str(j)
    elif j<100:
       j="0"+str(j)
    #change branch / usn here
    usn="1RV16CS"+str(j)
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

    #this has to be found by printing 'string' and finding location of name for any brqnch other than CSE
    """
        COMPUTER SCIENCE AND ENGINEERING -413
        ELECTRONICS AND COMMUNICATION ENGINEERING-413+9 and so on....
        INFORMATION SCIENCE AND ENGINEERING -416
    """
    entry=413 #change with with branch

    string=browser.get_current_page().text
    #print(string)


    if "SGPA" in string:
        #browser.launch_browser()


        # Alter '4' with the semester youre looking for
        end=string.find('4',entry)
        print(string[entry:end])
        x=string[entry:end]
        y=string[end+1:end+5]
        count1=count1+1

        posA="A"+str(count1)
        posB="B"+str(count1)
        print(posA)
        Database.database(posA,posB,x,y)

        #use this to display result on console
        #print(string)


        #Use this to stop after each output
        #input("Press any key to continue")

        return True







url='http://results.rvce.edu.in'
#upper bound depends on the department
for j in range(1,200):
    for i in range(50):
        if scrape(url, j)==True:
            break
