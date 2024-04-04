
import whois

#uncomment to list details of multiple sites
#sites = ["example1.com", "example2.com", "example3.com", "example4.com", "example5.com"]
#companies = [whois.whois(s).org for s in sites]
#print(companies)

#uncomment for emails 
#emails = [whois.whois(s).emails for s in sites]

#print(emails)

res = whois.whois("example.com") #enter website here

print(res)
#uncomment and adjust to specify values to return
#print(res.emails) 

