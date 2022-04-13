print("MANDAVA HARIPRASAD")
import sharepy
from sharepy import connect
from sharepy import SharePointSession
import logging
SPUrl = "https://trainingmy844.sharepoint.com"
username = 'UserSharePOint@trainingmy844.onmicrosoft.com'
password = 'SharePoint@123'
site = "https://trainingmy844.sharepoint.com/sites/ForHackathon?market=en-US"
s = sharepy.connect(SPUrl, username, password)
# Create header for the http request
my_headers = {
    'accept': 'application/json;odata=verbose',
    'content-type': 'application/json;odata=verbose',
    'odata': 'verbose',
    'X-RequestForceAuthentication': 'true'
}
if not hasattr(s, 'cookie'):
    print("authentication failed!");
    quit()
else:
    # This will return a Requests response object. See the requests documentation for details. s.get() returns Requests response object
    r = s.getfile(site, filename='DASHBOARD.xlsx')
    print(r.status_code)
print(r.raw)
print("Script Complete")