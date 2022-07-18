import requests
import json

def Audit(policyID):
    pID = policyID
    # ---- INSERT YOUR FWs INTERNAL IP(AND PORT). API CALL SHOULD REMAIN THE SAME.
    # ---- INSERT YOUR ACCESS TOKEN AT THE END OF THIS VARIABLE STRING
    # ---- EXAMPLE: AFGSINASFDONSAFINOISANGNJGGJGJ
    allData = f"https://YOUR IP:YOUR PORT/api/v2/cmdb/firewall/policy?vdom=root&access_token=INSERT YOUR ACCESS TOKEN"
    #requests.packages.urllib3.disable_warnings()
    # Get return from API data and place into variable so we can use
    # verify False is to ignore SSL verification
    data = requests.get(allData, verify=False)
    # turn data returned from API (in data variable) into JSON 
    # this is needed because the data is returned as strings otherwise
    jsonData = json.loads(data.text)

    # create file to store audit info
    # create CSV
    # ---- REPLACE YOUR PATH WITH A PATH ON YOUR NETWORK TO STORE THE CSV
    # ---- EXAMPLE: C:/Users/tom/Documents/code/fgtPolicies.csv
    policyRequested = open("C:/REPLACE/WITH/YOUR/PATH/file.csv", mode="w")
    #print(pID)
    output = f"{jsonData['results'][pID]}"
    # Creating CSV, writing output into CSV 
    policyRequested.write((f"{output}\n"))
    # closing CSV after Writing
    policyRequested.close()
