---
title: Markdown Guide (modified)
author: Open Source
date: '2018-08-30'
categories:
  - Example
tags:
  - Markdown
---

An h1 header
============

Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.
Unicode is supported. ☺



An h2 header
------------

Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the actual text starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }

As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

~~~
define foobar() {
    print "Welcome to flavor country!";
}
~~~

(which makes copying & pasting easier). You can optionally mark the
delimited block for Pandoc to syntax highlight it:

~~~python
import time
# Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
~~~



### An h3 header ###

Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Notice again how text always lines up on 4-space indents (including
that last line which continues item 3 above).

Here's a link to [a website](http://foo.bar), to a [local
doc](local-doc.html), and to a [section heading in the current
doc](#an-h2-header). Here's a footnote [^1].

[^1]: Footnote text goes here.

Tables can look like this:

size|material    |color
----|------------|------------
9   |leather     |brown
10  |hemp canvas |natural
11  |glass       |transparent

Table: Shoes, their sizes, and what they're made of

(The above is the caption for the table.)

A horizontal rule follows.

***

Here's a definition list:

apples
: Good for making applesauce.

oranges
: Citrus!

tomatoes
: There's no "e" in tomatoe.

(Put a blank line between each term/definition pair to spread
things out more.)

and images can be specified like so:

![example image](/images/partywizard.gif "An exemplary image")

Inline math equations go in like so: \\(\omega = d\phi / dt\\).
Display math should get its own line and be put in in
double-dollarsigns:

$$I = \int \rho R^{2} dV$$

And note that you can backslash-escape any punctuation characters
which you wish to be displayed literally, ex.: \`foo\`, \*bar\*, etc.

#### Images auto center:

![Party](http://emojis.slackmojis.com/emojis/images/1475875185/1223/party-dinosaur.gif?1475875185)

## To Develop a Remote monitoring tool
Task assigned:
- Configure a machine as a web server. Using laptop as your client, do the following:
- Scan the network and list the devices that are SNMP enabled (Nmap may be used)
- Query the SNMP enabled devices and store the responses in the client side.


#### Web server
- **web server's** primary function is to accept incoming requests from clients, such as web browsers, and respond with the requested resources, such as HTML pages, etc.
- **working model of web server**
    - Request: a browser(client) send http request to web server by specifiying the resouce it wants
    - Recieves req: receives the request and analyzes it to determine what resource is being requested.
    - Process the req: auth the client, retrieving from the storage, exec the server side dynamic scrip(js)
    - Response: web server sends the response back to the client with req resource or its error message it the code
    - Client receives response: receives the response in browser

  eg. apache, nginx

#### Setting up the web server 
_Arch linux: EndeavourOS with Plasma6 as DE_

- Started and enabled nginx server with systemctl for daemon use
`sudo syste![doc2.png](../../../../Pictures/Screenshots/doc2.png "doc2.png") by default it will be in ``/usr/share/nginx/html``
![example image](/images/doc1.png "An exemplary image")

- check the nginx works or not by using
    - `ip a` - get the ip address of the system from wlan0
    - `192.168.0.126` paste this in url of brower

![](../../../../Pictures/Screenshots/doc2.png)

#### To scan the network and look for SNMP enabled devices(_by using nmap_)


- installing nmap using pacman - `sudo pacman -S nmap`
- scanning the nmap `sudo nmap -sU -p 192.168.0.126/24`
  ![doc3.png](../../../../Pictures/Screenshots/doc3.png)
  prob because the -p flag shoud mention the port - as nmap uses udp port 161
- This fixes the problem `sudo nmap -sU -p 161 192.168.0.0/24`
-  `-sU` specifies a UDP scan
-  `-p 161` specifies the port number for SNMP
![doc4.png](../../../../Pictures/Screenshots/doc4.png)

- usually the state will be closed for snmp service
- to enable snmp in other system
- install snmp in other local system and edit the conf file for snmpd 
```path
sudo nano /etc/snmp/snmpd.conf
```
- add these below lines in the snmpd.conf and restart the systemctl service in the another machine(I used another machine as aanisha's lap and done all these configuration)
```bash
agentAddress udp:161
rocommunity public
```
![](../../../../Pictures/Screenshots/doc6.png)
after being changed and restarted the service, the port for the machine is open now as _highlighed above_ and now it is snmp enabled device.


### To Query SNMP-enabled devices and store responses on the client side

I'm missing something while querying via snmpget - which is the OID.
I also tried to fetch OID with smpwalk as mentioned in other community discussion forum of snmp, but everything came out as unreachabe or timeout

- also trying other tools like snmpwalk and snmptranslate
- I will figure it out soon, this part is taking some time to finish and will soon troubleshoot this and wind it up soon.


