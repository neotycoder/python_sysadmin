#!/bin/sh
# Author: Ty Lim
# Date: 02-23-2015
# Description: Simple little shell bash shell script to scrape info on a site that's either using Google Analytics, or utilizing Dyn DNS.

function readUrl(){
read -p "Enter a URL: " url

}

function searchDns() {
dnsSearch=`whois $url | grep 'Name Server:' | grep -i dynect.net`
if [  "${dnsSearch}" ]; then 
	echo "Using Dyn: Yes"
else
	echo "Using Dyn: No"
fi

}

function searchCurl() {
result=`curl -s $url | grep -F ".google-analytics.com/ga.js"`
result2=`curl -s $url | grep -F "ga.async = true"`
if [[ -n "$result" ]]; then
	if [[ -n "$result2" ]]; then
		echo "Using GA: Yes"
	fi
else
	echo "Using GA: No"

fi

}


function main(){

readUrl
searchCurl $url
searchDns $url

}
#########  MAIN #######
main
