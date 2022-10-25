from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # opens google.
web.get('https://www.careersafeonline.com/')

loginButton = web.find_element(By.CLASS_NAME, "sppb-btn.sppb-btn-success.button-text")
loginButton.click()
username = web.find_elements(By.CLASS_NAME, "form-login")[0]
password = web.find_elements(By.CLASS_NAME, "form-login")[1]
signInButton = web.find_element(By.CLASS_NAME, "signIn-button")


username.send_keys("cheeriosmilky4@gmail.com")
password.send_keys("000C3CAa1cheerios")

signInButton.click()
time.sleep(1)

courseButton = web.find_element(By.LINK_TEXT, "Continue")
courseButton.click()
time.sleep(1)

oshaLinks = [
    "Introduction to OSHA","Walking/Working Surfaces","Emergency Action Plans and Fire Protection","Avoiding Electrocution Hazards","Personal Protective Equipment",
    "Hazard Communication", "Materials Handling, Storage, Use, and Disposal", "Machine Guarding", "Industrial Hygiene", "Bloodborne Pathogens", "Ergonomics", "Safe Driving Practices",
    "Preventing Workplace Violence", "Safety & Health Programs"
]

for i in range(len(oshaLinks)):
    welcomeToOsha = web.find_element(By.LINK_TEXT, oshaLinks[i])
    welcomeToOsha.click()
    time.sleep(2)
    welcomeCon = web.find_element(By.ID, "topic-details__launch-topic-btn")
    welcomeCon.click()
    time.sleep(2)
    timeText = web.find_element(By.ID, "main-content__topic-completed-time").text
    timeComp = timeText[22:]
    if timeComp.find("h") != -1:
        amtOfHours = timeComp.index("h")
        if amtOfHours > 1:
            # print(str(amtOfHours) + "Amt of hours was greater than one")
            hours = timeComp[0] + timeComp[1]
            intHours = int(hours)
            if intHours > 0:
                web.back()
        elif amtOfHours == 1:
            print(int(timeComp[0]))
            if int(timeComp[0]) > 0:
                web.back()
                print("It was less then neccesary time.")
            else:
                # web.back()
                amtOfMinutes = timeComp[timeComp.index("m")-2:timeComp.index("m")]
                intAmtOfMinutes = int(amtOfMinutes)
                if intAmtOfMinutes >= 60:
                    web.back()
                elif intAmtOfMinutes < 60:
                    match i:
                        case 0:
                            break
                        case 1:
                            break
                        case 2:
                            for i in range(76):
                                case2 = web.find_element(By.ID, "pagegroup-5493")
                                case2.click()
                                time.sleep(47)
                                web.back()
                        case 3:
                            case3 = web.find_element(By.ID, "pagegroup-5502")
                            case3.click()
                            for i in range(50):
                                time.sleep(26)
                                secondLink = web.find_element(By.LINK_TEXT, "Introduction to Electrocution Hazards in the Workplace")
                                secondLink.click()
                                time.sleep(67)
                                web.back()

                        case 4:
                            case4 = web.find_element(By.ID, "pagegroup-5509")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 5:
                            case4 = web.find_element(By.ID, "pagegroup-5519")
                            case4.click()
                            for i in range(80):
                                time.sleep(25)
                                web.refresh()
                        case 6:
                            case4 = web.find_element(By.ID, "pagegroup-5529")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 7:
                            case4 = web.find_element(By.ID, "pagegroup-5536")
                            case4.click()
                            for i in range(80):
                                time.sleep(76)
                                web.refresh()
                        case 8:
                            case4 = web.find_element(By.ID, "pagegroup-5542")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 9:
                            case4 = web.find_element(By.ID, "pagegroup-5550")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 10:
                            case4 = web.find_element(By.ID, "pagegroup-5557")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 11:
                            case4 = web.find_element(By.ID, "pagegroup-5565")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 12:
                            case4 = web.find_element(By.ID, "pagegroup-5573")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                        case 13: 
                            case4 = web.find_element(By.ID, "pagegroup-5581")
                            case4.click()
                            for i in range(60):
                                time.sleep(51)
                                web.refresh()
                # print(intAmtOfMinutes)

    # if timeText == 0:
    #     break
    # break

# welcomeToOsha.click()
time.sleep(5)


# welcomeCon = web.find_element(By.ID, "topic-details__launch-topic-btn")
# welcomeCon.click()
# time.sleep(5)

oshaStand = web.find_element(By.ID, "pagegroup-5485")
oshaStand.click()
time.sleep(5)

while(True):
    # video1 = web.find_elements(By.CLASS_NAME, "navPageLink")[0]
    # standard = web.find_element(By.LINK_TEXT, "Examples of OSHA Standards")
    time.sleep(35)
    text1 = web.find_element(By.LINK_TEXT, "Introduction")
    text1.click()
    time.sleep(60)
    text2 = web.find_element(By.LINK_TEXT,"Fall Hazard Prevention Methods")
    text2.click()
    time.sleep(60)
    web.back()
    web.back()
    time.sleep(35)
    # video1.click()

# time.sleep(500)