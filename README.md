# fgt-policyAudit
use this tool to audit the number of policies in your firewall and then use the listed policies to index specific policies to observe in more detail. 


HOW TO USE THIS TOOL

1. Use the "listofActivePolicies.py" script to get a list of all your active FW policies. with their
    corresponding index number. The index number is needed to properly audit the policy in the next file
2. Use the policyAuditCall.py to use Audit() function from "policyAudit.py". Audit() function will take in one 
    argument (integer) that will index the list of Act Policies. The output is pull from Policies 
    and a certain policy in question (that you need more detail for auditing)

UPDATES NEED TO USE
----------------------
listofActivePolicies.py
1. update line 10 with your FWs IP:Port as well as create and place your access token at 
    the end of the string. 
2. update line 32 with the path you would like for your csv file. (where output details to be stored)

policyAudit.py
1. update line 9 with your FWs IP:Port as well as create and place your access token at
    the end of the string. 
2. update line 22 with the path you would like for your csv file. (where output details to be stored)

OUTPUT OF policyAduit.py
- the output stores in a CSV and the config is stored in one row. 
-- I am working on adjusting the output so it's clean without modification. However,
--- until then, you will need to modify the csv file
---- 1. insert column "A"
----- 2. copy column "B" Row 1
------ 3. select Column "A" and paste as "Transpose" (it will paste all Rows data under one column)
I am working on updating this, I will update code when I do adjust this. 