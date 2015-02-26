+# Name: stockAnalysis7.py
+# Version: 7
+# Author: Ty Lim
+# Date: August 30, 2014
+# Description: This program gather all COGS, SGA, Revenue information for a NASDAQ traded stock and
+# displays and makes all pertinent CVP calcualtions for that stock based on released financial data.
+# Notes:
+# 1. This application utilizes Google Finance to read in stock information.
+# 2. This application reads in financial data from a fixed position within the Google Finance generated html file.
+# Changes:
+# 1. Added ability to write to an html file.
+# 	a. Added file object to export data to html file.
+#	b. File being written to /tmp/stock.html
+
+import csv
+import sys
+from os import path
+import urllib2
+from bs4 import BeautifulSoup
+from urllib2 import urlopen
+import json
+
+class buildCSVFinancials:
+	def __init__(self,url,csvFile):
+		self.url = url
+
+	def writeCSV(self):
+		soup = BeautifulSoup(urlopen(self.url))
+		table = soup.find('table', attrs={ "class" : "gf-table rgt"})
+		headers = [header.text for header in table.find_all('td')]
+		rows = []
+
+		for row in table.find_all('td'):
+			rows.append([val.text.encode('utf8') for val in row.find_all('td')])
+
+		with open(csvFile, 'wb') as f:
+			writer = csv.writer(f)
+			writer.writerow(headers)
+			writer.writerows(row for row in rows if row)
+			
+
+class readCSV:
+	def __init__(self,csvFile):
+		self.csvFile = csvFile
+
+	def readCSVFile(self):
+		cr = csv.reader(open(self.csvFile,"rb"))
+		
+		for row in cr:
+			# Name value pair. This goes in the specific row position in the read html file. 
+			# These positions are fixed within the finance site. 
+			# Note: These will be different for other finance sites.
+
+			revenue_header=row[0]
+			rev_current_qtr=row[1]
+			rev_previous_qtr=row[2]
+			cogs_current_qtr=row[20]
+			cogs_previous_qtr=row[21]
+			sga_current_qtr=row[32]
+			sga_previous_qtr=row[33]
+
+			#replace comma with null
+			# Convert from string to integer. Remove all ','
+			rev_current_qtr = rev_current_qtr.replace(',','')
+			rev_current_qtr = rev_current_qtr.replace('.00','')
+			rev_current_qtr = float(rev_current_qtr)
+			
+			rev_previous_qtr = rev_previous_qtr.replace(',','')
+			rev_previous_qtr = rev_previous_qtr.replace('.00','')
+			rev_previous_qtr = float(rev_previous_qtr)
+			
+			cogs_current_qtr = cogs_current_qtr.replace(',','')
+			cogs_current_qtr = cogs_current_qtr.replace('.00','')
+			cogs_current_qtr = float(cogs_current_qtr)
+		
+			cogs_previous_qtr = cogs_previous_qtr.replace(',','')
+			cogs_previous_qtr = cogs_previous_qtr.replace('.00','')
+			cogs_previous_qtr = float(cogs_previous_qtr)
+
+			sga_current_qtr = sga_current_qtr.replace(',','')
+			sga_current_qtr = sga_current_qtr.replace('.00','')
+			sga_current_qtr = float(sga_current_qtr)
+		
+			sga_previous_qtr = sga_previous_qtr.replace(',','')
+			sga_previous_qtr = sga_previous_qtr.replace('.00','')
+			sga_previous_qtr = float(sga_previous_qtr)
+
+
+		#print revenue_header
+		#print current_qtr
+		#print previous_qtr
+		return rev_current_qtr, rev_previous_qtr,cogs_current_qtr,cogs_previous_qtr,sga_current_qtr,sga_previous_qtr
+
+class incomeAnaylsis:
+	def __init__(self, sales, cogs, sga):
+		self.sales 	= sales
+		self.cogs 	= cogs
+		self.sga	= sga
+		
+	def contributionMargin(self):
+		
+		#print self.sales
+		#type(self.sales)
+		CM = float(self.sales)-float(self.cogs)
+		return CM
+	
+	def contrinbutionMarginRatio(self):
+		CM = float(self.sales)-float(self.cogs)
+		CMR = float(CM/self.sales)
+		return CMR
+
+	def unitCM(self):
+		unitCM = self.sales/(float(self.sales)-float(self.cogs))
+		return unitCM
+
+	def profit(self):
+		CM = float(self.sales)-float(self.cogs)
+		CMR = float(CM/self.sales)
+		profit = CMR * self.sales - self.sga
+		return profit
+		
+	def fixedCosts(self):
+		CM = float(self.sales)-float(self.cogs)
+		CMR = float(CM/self.sales)
+		profit = CMR * self.sales - self.sga
+		fixedCosts = CMR * self.sales - profit  
+		return fixedCosts	
+
+	
+##### MAIN ######
+#stockSymbol = input("Enter a stock symbol: ")
+#Sublime BUG. Need to fix. For now, hardcode the stock symbol.
+stock = 'swks'
+URL = 'http://www.google.com/finance?q=NASDAQ%3A'+stock+'&fstype=ii&ei=LvYAVKCBCsSyiAKN7IGoCA'
+csvFile = '/tmp/output_file5.csv'
+buildCSVFinancialsObject = buildCSVFinancials(URL,csvFile)
+buildCSVFinancialsObject.writeCSV()
+readCSVObject = readCSV(csvFile)
+rev_current_qtr,rev_previous_qtr,cogs_current_qtr,cogs_previous_qtr,sga_current_qtr,sga_previous_qtr = readCSVObject.readCSVFile()
+incomeAnaylsisObjectCurrentQuarter = incomeAnaylsis(rev_current_qtr,cogs_current_qtr,sga_current_qtr)
+contributionMargin = incomeAnaylsisObjectCurrentQuarter.contributionMargin()
+contributionMarginRatio = incomeAnaylsisObjectCurrentQuarter.contrinbutionMarginRatio()
+unitCM = incomeAnaylsisObjectCurrentQuarter.unitCM()
+profit = incomeAnaylsisObjectCurrentQuarter.profit()
+fixedCosts = incomeAnaylsisObjectCurrentQuarter.fixedCosts()
+#print 'CM = '+ CM
+
+print 'STOCK SYMBOL: '+stock
+print ''
+print 'Revenue Current Quarter: '+str(rev_current_qtr)+'   '+'COGS Current Quarter: '+str(cogs_current_qtr)
+print 'Revenue Previous Quarter: '+str(rev_previous_qtr)+'  '+'COGS Previous Quarter: '+str(cogs_previous_qtr)
+print ''
+print 'SGA Current Quarter: '+str(sga_current_qtr)+'   '+'Contribution Margin: ' + str(contributionMargin)
+print 'SGA Previous Quarter: '+str(sga_previous_qtr)+'  '+'Unit CM: ' + str(unitCM)
+print ''
+print 'Contribution Margin Ratio: '+ str(contributionMarginRatio)
+print ''
+print 'Fixed Costs: '+ str(fixedCosts)
+print ''
+print 'Profit: '+str(profit)
+
+
+# Write to output output file
+
+f = open('/tmp/stock.html', 'w')
+# This is a test of whether or not the file has been opened.
+#print f 
+# Build this as an object. Seperate this out as a stand-alone, callable file.
+f.write('<HTML>\n')
+f.write('<H1>Cost-Volume-Profit Analysis</H1>')
+f.write('<BOLD><H1>STOCK SYMBOL: ' + stock + '</H1><BOLD><BR>')
+
+f.write('\n<BOLD>Revenue Current Quarter:</BOLD>  '+str(rev_current_qtr) + '\n<BR>')
+f.write('\n<BOLD>Revenue Previous Quarter:</BOLD>'+str(rev_previous_qtr) + '\n<BR>')
+f.write('\n<BOLD>COGS Current Quarter: </BOLD>'+str(cogs_current_qtr) + '\n<BR>')
+f.write('\n<BOLD>COGS Previous Quarter:</BOLD> '+str(cogs_previous_qtr) + '\n<BR>')
+
+f.write('\n<BR><BOLD>SGA Current Quarter: </BOLD>  '+str(sga_current_qtr) + '\n<BR>')
+f.write('\n<BOLD>SGA Previous Quarter: </BOLD> '+str(sga_previous_qtr) + '\n<BR>')
+
+
+f.write('\n<BOLD>Contribution Margin:</BOLD> '+str(contributionMargin) + '\n<BR>')
+f.write('\n<BR><BOLD>Unit CM:</BOLD>  '+str(unitCM) + '\n<BR>')
+f.write('\n<BOLD>Contribution Margin Ratio:</BOLD> '+str(contributionMarginRatio) + '\n<BR>')
+f.write('\n<BOLD>Fixed Costs:</BOLD> '+str(fixedCosts) + '\n<BR>')
+f.write('\n<BOLD>Profit:</BOLD> '+str(profit) + '\n<BR>')
+
+
+f.write('\n</HTML>')
+# Write HTML to stock.html
+# Close the file from writing.
+f.close()
+
+# Dump data inot JSON file for access in JAVASCRIPT.
+# This can be utilized for the mobile application as the reader for the 'viewer' mobile app.
+data = {'stock': stock, 'Revenue Current Quarter':rev_current_qtr, 'Revenue Previous Quarter':rev_previous_qtr,'COGS Current Quarter':cogs_current_qtr,'COGS Previous Quarter':cogs_previous_qtr}
+
+jSonDumpFile = open('/tmp/json_stock.json', 'w')
+json.dump(data, jSonDumpFile, ensure_ascii=False)
+