import dns
import dns.resolver
import ipaddress

def ipaddrToAsInfo(s):
    queryAddr = "{0}.{1}.{2}.{3}.origin.asn.cymru.com"
    queryAs = "AS{0}.asn.cymru.com"
    try:
        s = s.split("/")[0]
        ip = ipaddress.IPv4Address(s)
        s = str(ip)
        sarry = s.split(".")
        q = queryAddr.format(*sarry[::-1])
        try:
            answer = dns.resolver.resolve(q, "TXT")
        except dns.resolver.NXDOMAIN:
            return None
        if len(answer) == 0:
            raise EnvironmentError
        addrInfo = str(answer[0])[1:-1].split("|")
        addrInfo = list(map(lambda x: x.strip(), addrInfo))
        asnum = addrInfo[0]

        q = queryAs.format(asnum)
        try:
            answer = dns.resolver.resolve(q, "TXT")
        except dns.resolver.NXDOMAIN:
            return None
        if len(answer) == 0:
            raise EnvironmentError
        asInfo = str(answer[0])[1:-1].split("|")
        asInfo = list(map(lambda x: x.strip(), asInfo))
        asname = asInfo[4].split(" ")[0]
        return [asnum, asname]

    except ValueError:
        return False

# ['2500', 'WIDE-BB']
print(ipaddrToAsInfo("203.178.143.1"))
# None
print(ipaddrToAsInfo("0.0.0.0"))

