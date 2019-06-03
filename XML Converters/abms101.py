# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:16:28 2019

@author: Meed Ubarab
"""

#importing panda for csv and excel data reading
import pandas as pd

#importing datetime module for retrieving date of submission
from datetime import datetime

#report information
reportName = 'ABMS101'
reportDescription = 'Agent Recruitment'

#getting current date of submission
todaysDate = datetime.today().strftime('%d-%m-%Y')

#saving information for Contec Global
institutionName = 'Contec Global'
FICode = 100032

#saving IDType for BVN as 1
IDType = 1


#saving AgentBusiness as 11 (for others)
AgentBusiness = 11

#saving AgentType as 2 (for sole Age)
AgentType = 2

#setting AgentCode to empty as that is provided automatically once uploaded
AgentCode = ''


#checking if file exists
while True:
    try:
        #geting the data file
        fileName = input('Enter filename>>  ')
        
        
        #creating link to csv file on folder
        csvFile = fileName.upper()+'.csv'
        
        #setting for xml file creation
        newFilename = "%s.xml" % fileName.upper()
        
        
        #creating an empty xml file
        xmlFile = open(newFilename, 'w')
        df = pd.read_csv(csvFile, sep=',')
        break
    except:
        print("It looks like the file doesn't exist. Check and Try again")
        continue



#header script
header="""<?xml version="1.0" encoding="utf-8"?>
    <CALLREPORT>
      <HEADER>
        <CALLREPORT_ID>%s</CALLREPORT_ID>
        <CALLREPORT_DESC>%s</CALLREPORT_DESC>
        <INST_CODE>%s</INST_CODE>
        <INST_NAME>%s</INST_NAME>
        <AS_AT>%s</AS_AT>
      </HEADER>
      <BODY>""" % (reportName, reportDescription, FICode, institutionName, todaysDate)
      

#footer script
footer ="""</BODY>
      <FOOTER>
        <AUTH_SIGNATORY>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <POSITION>%s</POSITION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </AUTH_SIGNATORY>
        <AUTH_SIGNATORY>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <POSITION>%s</POSITION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </AUTH_SIGNATORY>
        <AUTH_SIGNATORY>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <POSITION>%s</POSITION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </AUTH_SIGNATORY>
        <CONTACT_DETAILS>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </CONTACT_DETAILS>
        <CONTACT_DETAILS>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </CONTACT_DETAILS>
        <CONTACT_DETAILS>
          <NAME>%s</NAME>
          <DESIGNATION>%s</DESIGNATION>
          <DATE>%s</DATE>
          <TEL_NO>%s</TEL_NO>
          <EXTN>%s</EXTN>
        </CONTACT_DETAILS>
        <DESC>%s</DESC>
        <PREPARED_BY>%s</PREPARED_BY>
        <AUTH_BY>%s</AUTH_BY>
        <MLR_OFFICER_CODE>%s</MLR_OFFICER_CODE>
        <HEAD_OFFICE_ADDRESS>%s</HEAD_OFFICE_ADDRESS>
        <TEL_NO>%s</TEL_NO>
        <DATE>%s</DATE>
        <CREDIT_OFFICER>%s</CREDIT_OFFICER>
        <BRANCH_MANAGER>%s</BRANCH_MANAGER>
        <PREPARED_DATE>%s</PREPARED_DATE>
        <CHECKED_BY>%s</CHECKED_BY>
        <CHECKED_DATE>%s</CHECKED_DATE>
      </FOOTER>
    </CALLREPORT>""" % ('Adeyemo Christiana', 'Sales Onboarding Executive', 'Registering', todaysDate, '09087347623',
     '07000669669', 'Ajibade Okubule', 
    'Sales Onboarding Coordinator', 'Verifier', todaysDate, '09087212770', '07000669669', 'Olusola Ramon', 'Complaince Officer', 'Activator', todaysDate, '07000669669', 
     '', 'Nitesh Burke', 'Head, Sales and Onboarding', todaysDate, '09087469710', '07000669669', 'Fabusua Isaac', 
     'Business Development Manager', todaysDate, '08076048868', '07000669669', 'Toyin Ronke Atanda', 'Customer Service Manager', todaysDate,
     '09087519451', '07000669669', 'Experience Follow-up', 'Umoru Meed Muhammed', 'Olusola Ramon', 
     '', '239/241, Ikorodu Road, Ilupeju, Lagos', '07000669669', todaysDate, 'Schowdary Sumeet',
     'Mahesh Nair', todaysDate, 'Olusola Ramon', todaysDate)


#body xml tag converter function
def convert_row(row): 
    return"""\n<RETURNITEM>
      <BatchID>%s</BatchID>
      <FICode>%s</FICode>
      <BusinessName>%s</BusinessName>
      <AgentCode>%s</AgentCode>
      <Gender>%s</Gender>
      <PhoneNumber1>%s</PhoneNumber1>
      <PhoneNumber2>%s</PhoneNumber2>
      <AgentAddress>%s</AgentAddress>
      <UniqueIdType>%s</UniqueIdType>
      <UniqueIdNumber>%s</UniqueIdNumber>
      <AgentBusiness>%s</AgentBusiness>
      <AgentType>%s</AgentType>
      <BusinessAddress>%s</BusinessAddress>
      <PhoneNumber>%s</PhoneNumber>
      <Email>%s</Email>
      <LGA>%s</LGA>
      <State>%s</State>
      <GPSCoordinatesX>%s</GPSCoordinatesX>
      <GPSCoordinatesY>%s</GPSCoordinatesY>
      <DateOfAppointment>%s</DateOfAppointment>
      <RecruitedBy>%s</RecruitedBy>
      <TransactionLimit>%s</TransactionLimit>
      <LandMarkDescription>%s</LandMarkDescription>
    </RETURNITEM>
  """ % (int(row.BatchID), FICode, row.BusinessName, AgentCode, row.Gender, '0'+str(int(row.PhoneNumber1)), '0'+str(int(row.PhoneNumber2)), 
row.AgentAddress, IDType, int(row.BVN), AgentBusiness, AgentType, row.BusinessAddress, '0'+str(int(row.PhoneNumber)), row.Email, row.LGA, row.State, row.GPSCoordinatesX, 
row.GPSCoordinatesY, row.DateOfRecruitment, row.RecruitedBy, 
int(row.TransactionLimit), row.LandMarkDescription)


#Body xml script
body = '\n'.join(df.apply(convert_row, axis=1))

#combining all parts together
xmlLines = header+body+footer


#creating the xml file
xmlFile.write(xmlLines)


print("File converted successfully")