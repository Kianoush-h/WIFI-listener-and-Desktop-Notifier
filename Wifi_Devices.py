
# from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.firefox.options import Options
from selenium import webdriver 
from win10toast import ToastNotifier 
import time


toaster = ToastNotifier() 

options = Options()
options.add_argument("--headless") 
driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')


url = 'http://192.168.2.1/'
driver.get(url) 
print('Modem page is opened')
time.sleep(10)
try:
    a = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div[2]/label')
    a.click()
    print('Advance mode')
    
    time.sleep(3)
    delay = 15 * 1
    now = time.time()
    old = now
    
    while now < old + delay:
        
        if now + 5 >= old + delay:
            old  = time.time()
            
            a = driver.find_element_by_class_name('dm-list-ul')
            a = a.text.split('\n')
            print('Devices are exported')    
            
            devices = []
            for i in a:
                if 'IP:' in i or 'MAC:' in i:
                    pass
                else:
                    devices = devices + [i]
                    
            devices = set(devices)    
            print(devices)
            
            result = ''
            for i in devices:
                result = result + i + ' **** '
            toaster.show_toast("Current devices on your WIFI", result, duration = 5, icon_path="icon.ico", threaded=True) 
        now  = time.time()

except:
    driver.quit()
    print('Error')
    















