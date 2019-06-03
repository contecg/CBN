# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:50:07 2019

@author: Meed Muh'd Ubarab
"""

#importing panda for csv and excel data reading
import pandas as pd

#importing datetime module for retrieving date of submission
from datetime import datetime

#report information
reportName = 'ABMS107'
reportDescription = 'SUSPICIOUS TRANSACTIONS RETURN'

#getting current date of submission
todaysDate = datetime.today().strftime('%d-%m-%Y')

#saving information for Contec Global
institutionName = 'Contec Global'
FICode = 100032


#checking if file exists
while True:
    try:
        #geting the data file
        fileName = input('Enter filename>>  ')
        
        
        #creating link to csv file on folder
        csvFile = fileName.upper()+'.csv'
        
        #setting for xml file creation
        newFilename = "%s.xml" % fileName
        
        
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
</CALLREPORT>"""


#body xml tag converter function
def convert_row(row): 
    return"""\n<RETURNITEM>
      <SN>%s</SN>
      <AgentCode>%s</AgentCode>
      <DescriptionOfTransaction>%s</DescriptionOfTransaction>
      <AmountInvolved>%s</AmountInvolved>
      <DateReported>%s</DateReported>
      <ActionTaken>%s</ActionTaken> 
      <Remark>%s</Remark> 
    </RETURNITEM>
  """ % (row.SN, row.AgentCode, row.Description, row.Amount, row.Date, row.Action, row.Remark)

#Body xml script
body = '\n'.join(df.apply(convert_row, axis=1))

#combining all parts together
xmlLines = header+body+footer


#creating the xml file
xmlFile.write(xmlLines)


print("File converted successfully")