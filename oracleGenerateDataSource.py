#!/usr/bin/python

# Script Name: oracleDataSourceCreate.py
# Author: Ty Lim
# Date: 06/30/2016
# Description: This is a simple script that will allow for a standard creation of an Oracle data source entry in WebSphere Liberty.

"""
Sample Usage and Output:

./oracleGenerateDataSource.py
Application Name: appname
JNDI Name: jdbc/test
DB Server Name: dbserver
DB Port: 1521
DB Name: dbname
User: user
Password: thisismypassw0rd
{xor}Kzc2LDYsMiYvPiwsKG8tOw==

--------- CUT BELOW THIS LINE ---------

<!-- Data source entry for appname-->
<dataSource jndiName="jdbc/test" type="javax.sql.DataSource">
	<jdbcDriver libraryRef="oracleLib"/>
	<properties.oracle URL="jdbc:oracle:thin:@dbserver:1521:dbname" databaseName="dbname" driverType="thin" password="{xor}Kzc2LDYsMiYvPiwsKG8tOw==" portNumber="1521" serverName="dbserver" user="user"/>
</dataSource>
<!-- End Data source entry for appname-->

--------- CUT ABOVE THIS LINE ---------


"""

import subprocess



def inputOracleParam():
	"""Input all the required Oracle Parameters 
	for the XML stub.
	"""
	
	# Input Appication Name
	appName=raw_input('Application Name: ')
	# Input JNDI
	jndi=raw_input('JNDI Name: ')
	# Input Server 
	server = raw_input('DB Server Name: ')
	# Input Port
	port = raw_input('DB Port: ')
	# Input DB Name
	db = raw_input('DB Name: ')
	# Input user
	user = raw_input('User: ')
	# Input Password
	password = raw_input('Password: ')

	return appName, jndi, server, port, db, user, password

def createXML(appName, jndi, server, port, db, user, password):

	comment1="<!-- Data source entry for " + appName + "-->\n"
	ds1="<dataSource jndiName=\"" + jndi + "\" type=\"javax.sql.DataSource\">\n"
	ds2="\t<jdbcDriver libraryRef=\"oracleLib\"/>\n"
	ds3="\t<properties.oracle URL=\"jdbc:oracle:thin:@" + server + ":" + port + ":" + db + "\" databaseName=\"" + db + "\" driverType=\"thin\" password=\""+ password +"\" portNumber=\""+ port +"\" serverName=\""+ server +"\" user=\""+ user +"\"/>\n"
	ds4="</dataSource>\n"
	comment2="<!-- End Data source entry for " + appName + "-->\n"

	return comment1+ds1+ds2+ds3+ds4+comment2

def generateOutput(datasource):

	print "--------- CUT BELOW THIS LINE ---------\n"
	print datasource
	print "--------- CUT ABOVE THIS LINE ---------\n"

def encodePassword(password):

	# Path to securityUtility
	#secUtilityPath="/opt/IBM/WebSphere/Liberty/bin/securityUtility "
	secUtilityPath="/Users/neoty/Projects/WAS_Liberty/16.0.0.2/wlp/bin/securityUtility "
	secUtilityParam1="encode "
	secUtilityParam2=" --notrim"
	cmd=secUtilityPath+secUtilityParam1+password+secUtilityParam2
	encodedPassword = subprocess.check_output(cmd, shell=True)
	print encodedPassword

	return encodedPassword.rstrip("\n")

def main():
	appName, jndi, server, port, db, user, password = inputOracleParam()
	encodedPassword = encodePassword(password)
	#datasource = createXML(appName, jndi, server, port, db, user, password)
	# 	Uncomment the following line once you test on a liberty server.
	datasource = createXML(appName, jndi, server, port, db, user, encodedPassword)
	generateOutput(datasource)

if __name__ == '__main__':
	main()



# For Reference Use:
#  <dataSource jndiName="" type="javax.sql.DataSource">
#        <jdbcDriver libraryRef="oracleLib"/>
#       <properties.oracle URL="jdbc:oracle:thin:@<server>:<port>:<dbname>" databaseName="" driverType="thin" password="" portNumber="" serverName="" user=""/>
#    </dataSource>

