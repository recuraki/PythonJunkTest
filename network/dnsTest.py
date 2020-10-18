import dns

result = dns.resolver.query('google.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())

# Output: IP {your ip}