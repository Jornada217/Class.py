from selenium import webdriver
import time


chromeOptions = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'C:\\Users\\joaopaulo\\PycharmProjects\\Learning_Projects'}
chromeOptions.add_experimental_option('prefs', prefs)
#chromeOptions.add_argument('headless')
#Set the driver's directory
chromeDriver = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/venv/Scripts/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromeDriver, options=chromeOptions)

url = 'http://geoconvert.mimas.ac.uk/index.html'
file = 'C:/Users/joaopaulo/PycharmProjects/Learning_Projects/GeoConvertTest.csv'
driver.get(url)
#Initiate Session
driver.find_element_by_xpath('//*[@id="help-content"]/p/a').click()
print('Session initiated...')
#Select Convert Data from One Geography to Another -> Next
driver.find_element_by_xpath('//*[@id="convertRadioButton"]').click()
driver.find_element_by_xpath('//*[@id="Next"]').click()
print('Convert Data from One Geography to Another Selected')
# Select Source Geography: Lower super output -> Next
driver.find_element_by_xpath('//*[@id="sourcegeog"]/option[5]').click()
driver.find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
print('Source Geography -> "Lower super output" Selected')
#Select Target Geography: Lower super output -> Next
driver.find_element_by_xpath('//*[@id="targetgeog"]/option[5]').click()
driver.find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
print('Target Geography -> "Lower super output" Selected')
#Select Fixer 2001 Census to Fixed 2011 Census -> Next
driver.find_element_by_xpath('//*[@id="helpFooter"]/form[1]/table/tbody/tr[3]/td[3]/label/input').click()
driver.find_element_by_xpath('//*[@id="Next"]').click()
print('Fixed 2001 Census -> Fixed 2011 Census Selected')
#Move to uploading the file page
driver.find_element_by_xpath('//*[@id="fileUploadButton"]').click()
print('Conversion parameters Confirmed')
#Adjusting input characteristics
    #The GeoConvertTest file is using comma separation and first row is a header.
driver.find_element_by_xpath('//*[@id="comma"]').click() #Comma separated
driver.find_element_by_xpath('//*[@id="yes"]').click() #First line is Header
uploadGeo = driver.find_element_by_id('uploadButton') #Choose file button
uploadGeo.send_keys(file)
driver.find_element_by_xpath('//*[@id="uploadinputfile"]').click() #Next button
#Check Column Delimiter Character or Header Row.
#For more information on Input File requirements: http://geoconvert.mimas.ac.uk/help/input_files.htm
#Confirmation message is expected -> Next
#conf_message = driver.find_element_by_xpath('//*[@id="maincontent"]/div[1]/p[1]/text()')
#print(conf_message)
print()

#File Upload Confirmation Screen.
driver.find_element_by_xpath('//*[@id="helpFooter"]/form[1]/p/input').click()
print('Input File successfully uploaded.')

#Results Screen, download files (Matched Rows + Converted Data)
# download_matched = driver.find_element_by_xpath('//*[@id="helpFooter"]/div[1]/p/a').click()
# download_converted = driver.find_element_by_xpath('//*[@id="helpFooter"]/div[2]/p/a').click()
driver.find_element_by_xpath('//*[@id="helpFooter"]/div[1]/p/a').click()
driver.find_element_by_xpath('//*[@id="helpFooter"]/div[2]/p/a').click()
print('Files Sucessfully Downloaded')

#Process is finished
# Start again xpath: //*[@id="helpFooter"]/form/p[2]/input
driver.find_element_by_xpath('//*[@id="helpFooter"]/form/p[2]/input').click()
print('Start again selected')
#OBS: When loop restarts, first screen is the Select GeoConvert Function.
    #Process skips the session start.

#Close Navigator
# time.sleep(5)
driver.close()