# fgt-policyAudit
use this tool to audit the number of policies in your firewall and then use the listed policies to index specific policies to observe in more detail. 


HOW TO USE THIS TOOL

1. Use the "listofActivePolicies.py" script to get a list of all your active FW policies. with their
    corresponding index number. The index number is needed to properly audit the policy in the next file
2. Use the policyAuditCall.py to use Audit() function from "policyAudit.py". Audit() function will take in one 
    argument (integer) that will index the list of Act Policies. The output is pull from Policies 
    and a certain policy in question (that you need more detail for auditing)

UPDATES NEED TO USE
listofActivePolicies.py
1. update line 10 with your FWs IP:Port as well as create and place your access token at 
    the end of the string. 
2. update line 32 with the path you would like for your csv file. (where output details to be stored)

policyAudit.py
1. update line 9 with your FWs IP:Port as well as create and place your access token at
    the end of the string. 
2. update line 22 with the path you would like for your csv file. (where output details to be stored)

