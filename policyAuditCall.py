from policyAudit import Audit

# Example use of Pulicy Auditing. First you should run the "listofActivePolicies" to
# get the list of all active policies in your firewall configuration. 
# once you have the list, the output will show you what index = policy ID

# now that you have the index number, simply replace the blow (the index number in Audit() )
# ENSURE YOU CONFIGURED policyAudit.py with your FWs IP:Port and access token. 
# -- the output will create a csv in the directory you specified. 
# --- note the CSV is created in one row (currently working on a better output for the config)
# ---- until then, please read over the README.md file to clean up the output in the CSV (Excel)

policyCheck = Audit(7)

