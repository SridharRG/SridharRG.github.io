+++
title = "Notes for Networking Session"

[taxonomies]
tags = ["linux", "dns"]

[extra]
toc = false 
+++

### *_Domain Name_*
---

It is an identification string that defines a realm of administrative autonomy, authority, or control within the Internet.

DNS currently has ~300 million DNS registrations. Both query and reply messages follow the same message format. Both always include Name, Type, Class tuples — Class is usually IN. Names cannot be wildcarded but type and class can

How do we resolve domain names to IP addresses? Resolves starting from the root and makes it way down the network hierarchy

   1. Root (13 of these worldwide)
   2. Top-level Domains (e.g. .com, .net, .org, etc.)
   3. Second-level Domains (e.g. UBC)
   4. Subdomains (e.g. www)
   5. Individual machines
   6. Local DNS Servers (not actually a part of the hierarchy, just caches data)

Authoritative DNS server is the server with the actual jurisdiction of the domain name you are looking for. The authoritative server of cisco.must.ac.ug is cisco server under must(Malabar University). I use this for learning networks with cisco materials [They have this fking nice directory which will give us a clear idea about networks](https://cisco.must.ac.ug/cisco/)


### Types of queries

1. Recursive Query — if the name server doesn’t know the answer, it asks a downstream server (recursively) for the answer on your behalf.
2. Iterative Query — if the name server doesn’t know the answer, it tells you where to look at next, you do all the querying

### DNS servers store resource records (RRs) Types:

1. A (address records)

    - name: hostname
    - value: IPv4 address

2. NS (name server)

    - name: domain
    - value: name of DNS server for domain

3. MX (mail exchanger)

    - name: domain of email address
    - value: name of mail server

4. AAAA (addressx4 record)

    - name: hostname
    - value: IPv6 address

5. CNAME (canonical name)

    - name: alias
    - value: canonical name (e.g. foo.com)

6. TXT (just plain text)

    - name: domain
    - value: plain text in the format of attribute=value. The TXT record was originally intended as a place for human-readable notes but now often used for domain ownership verification.

links to proceed with:
- https://www.quora.com/How-do-I-set-up-my-own-DNS-server
- https://opensource.com/article/17/4/build-your-own-name-server
- https://meshnet.nordvpn.com/how-to/security/how-to-set-up-your-own-dns-server
- https://www.howtogeek.com/devops/how-to-run-your-own-dns-server-on-your-local-network/
- https://www.pcmag.com/how-to/how-and-why-to-change-your-dns-server
- https://www.ninjaone.com/blog/how-to-configure-a-dns-server/
- https://meshnet.nordvpn.com/how-to/security/protect-network-with-adguard-home

Also read about *dnsmasq* -  a free software tool
- https://stevessmarthomeguide.com/home-network-dns-dnsmasq/
- https://wiki.archlinux.org/title/Dnsmasq

#### privacy guide for dns
- https://www.privacyguides.org/en/advanced/dns-overview/

#### dns lookup tool
- https://dns-lookup.jvns.ca/
- [documentation](https://dnslink.dev/)

### note
- I brought my custom domain for sotc in namecheap with github students developers pack.