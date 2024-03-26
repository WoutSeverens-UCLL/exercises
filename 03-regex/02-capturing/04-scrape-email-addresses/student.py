# Write your code here
import re 

def scrape_email_addresses(string):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+', string)