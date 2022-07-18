
import requests, json

import json

# Pull Policies from FGT via API stores in variable
# ---- INSERT YOUR FWs INTERNAL IP(AND PORT). API CALL SHOULD REMAIN THE SAME. 
# ---- INSERT YOUR ACCESS TOKEN AT THE END OF THIS VARIABLE STRING
# ---- EXAMPLE: AFGSINASFDONSAFINOISANGNJGGJGJ
fgtPolicies = "https://YOUR IP:YOUR PORT/api/v2/cmdb/firewall/policy/?format=policyid|action&access_token=INSERT YOUR ACCESS TOKEN"

#requests.packages.urllib3.disable_warnings()
# Get return from API data and place into variable so we can use
# verify False is to ignore SSL verification
data = requests.get(fgtPolicies, verify=False)

# turn data returned from API (in data variable) into JSON 
# this is needed because the data is returned as strings otherwise
jsonData = json.loads(data.text)


# getting a number of items in list
# we will use this to perform a while loop later
counting = len(jsonData['results'])

# Empty List to store Policy IDs
policyList = []

# create CSV
# ---- REPLACE YOUR PATH WITH A PATH ON YOUR NETWORK TO STORE THE CSV
# ---- EXAMPLE: C:/Users/tom/Documents/code/fgtPolicies.csv
policiesConfigured = open("C:/REPLACE/WITH/YOUR/PATH/file.csv", mode="w")



# loop through and label index number for policy ID
# counting 


# While loop to pull items from nested Dictionary
while counting > 0:
    # Count down to end While loop when items are no longer in dict
    counting = counting - 1
    # index nested Dictionary
    policyNumbers = jsonData['results'][counting]['policyid']
    # add Int into empty list (PolicyList)
    policyList.append(policyNumbers)





# interate over Policy List and write into CSV

    for e in policyList:
        # we can't concantenate over a Int to string
        # turns INT into STRING
        intoString = str(e)
        # each String in Policy List adds Policy ID in front of the String
        output = f"Index Number: {counting} - policy ID: {intoString}"
        # writes output (Policy ID: ID#) to CSV

    # Sort Policy List
    organized = sorted(policyList, reverse= True)
    policiesConfigured.write((f"{output}\n"))
    # Closes CSV (saves)
policiesConfigured.close()


