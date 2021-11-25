import os
from selenium import webdriver
import time
from os import path
from os.path import sep, join

class geoconverter():

    def fjoin(self, *args, **kwargs):
        return join(*args, **kwargs).replace(sep, '/')

    def djoin(self, *args, **kwargs):
        return join(*args, **kwargs).replace(sep, '\\')

    def insert_file(self):
        file_src = join('data', 'src', 'GeoConvertTest.csv')
        file_path = path.abspath(file_src)
        file = self.fjoin(file_path)
        print(os.getcwd())
        print(file_src)
        print(file_path)
        print(file)
        return file
    #file = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/GeoConvertTest.csv'

    def autofill(self, passfile=None):
        self.step1() #directory source
        self.step2() #set chrome driver, URL
        self.step3() #Mimas Parameters
        self.step4(passfile) #Insert file
        self.step5() #Download and close

    def step1(self): #directory source
        dir_src = join('data', 'src')
        dir_path = path.abspath(dir_src)
        dir = self.djoin(dir_path)
        return dir

    def step2(self): #set chrome driver, URL
        url = 'http://geoconvert.mimas.ac.uk/index.html'
        chromeOptions = webdriver.ChromeOptions()
        #prefs = {'download.default_directory': 'C:\\Users\\joaopaulo\\PycharmProjects\\Learning_Projects'}
        prefs = {'download.default_directory': self.step1()}
        chromeOptions.add_experimental_option('prefs', prefs)
        chromeOptions.add_argument('headless')
        #Set the driver's directory
        chromeDriver = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/venv/Scripts/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromeDriver, options=chromeOptions)
        driver.get(url)
        return driver

    def step3(self): #Mimas Parameters
        #Initiate Session
        self.step2().find_element_by_xpath('//*[@id="help-content"]/p/a').click()
        print('Session initiated...')
        #Select Convert Data from One Geography to Another -> Next
        self.step2().find_element_by_xpath('//*[@id="convertRadioButton"]').click()
        self.step2().find_element_by_xpath('//*[@id="Next"]').click()
        print('Convert Data from One Geography to Another Selected')
        # Select Source Geography: Lower super output -> Next
        self.step2().find_element_by_xpath('//*[@id="sourcegeog"]/option[5]').click()
        self.step2().find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
        print('Source Geography -> "Lower super output" Selected')
        #Select Target Geography: Lower super output -> Next
        self.step2().find_element_by_xpath('//*[@id="targetgeog"]/option[5]').click()
        self.step2().find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
        print('Target Geography -> "Lower super output" Selected')
        #Select Fixer 2001 Census to Fixed 2011 Census -> Next
        self.step2().find_element_by_xpath('//*[@id="helpFooter"]/form[1]/table/tbody/tr[3]/td[3]/label/input').click()
        self.step2().find_element_by_xpath('//*[@id="Next"]').click()
        print('Fixed 2001 Census -> Fixed 2011 Census Selected')
        #Move to uploading the file page
        self.step2().find_element_by_xpath('//*[@id="fileUploadButton"]').click()
        print('Conversion parameters Confirmed')
        #Adjusting input characteristics

    def step4(self): #Insert file
            #The GeoConvertTest file is using comma separation and first row is a header.
        self.step2().find_element_by_xpath('//*[@id="comma"]').click() #Comma separated
        self.step2().find_element_by_xpath('//*[@id="yes"]').click() #First line is Header
        uploadGeo = self.step2().find_element_by_id('uploadButton') #Choose file button
        uploadGeo.send_keys(self.insert_file())
        self.step2().find_element_by_xpath('//*[@id="uploadinputfile"]').click() #Next button
        #Check Column Delimiter Character or Header Row.
        #For more information on Input File requirements: http://geoconvert.mimas.ac.uk/help/input_files.htm
        #Confirmation message is expected -> Next
        #conf_message = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/p[1]/text()')
        #print(conf_message)
        print()

        #File Upload Confirmation Screen.
        self.step2().find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
        print('Input File successfully uploaded.')

    def step5(self): #Download and close
        #Results Screen, download files (Matched Rows + Converted Data)
        download_matched = self.step2().find_element_by_xpath('//*[@id="helpFooter"]/div[1]/p/a').click()
        download_converted = self.step2().find_element_by_xpath('//*[@id="helpFooter"]/div[2]/p/a').click()
        print('Files Sucessfully Downloaded')

        #Process is finished
        # Start again xpath: //*[@id="helpFooter"]/form/p[2]/input
        self.step2().find_element_by_xpath('//*[@id="helpFooter"]/form/p[2]/input').click()
        print('Start again selected')
        #OBS: When loop restarts, first screen is the Select GeoConvert Function.
            #Process skips the session start.

        #Close Navigator
        # time.sleep(5)
        self.step2().close()
