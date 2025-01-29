# What is networking?

Exchange of random bytes of data between two computers either over the internet or over a LAN.

## How do we make this happen?

- A way to identify the source and destination computers.
- A way of maintaining data integrity.
- A way of routing data from one computer to another.
- Network is a hardware, and OS controls all the access to the hardware. So, if we need to communitate to the network we need to do it via the OS and its being done by an API called the **Sockets API**. It gives us a way to read and write data over the internet.

## Types of communication networks

### Circuit Switched

- Its old school and its not used anymore.
- How the communication works over here?
  - Consider a old school telephone operator
  - The call is made and it is connected to the operator.
  - The operator picks the call and connects the call physically to that location and the connection is made available between the two folks.
- Issues with Circuit Switched communication
  - Poor scalability.
  - If the distance is long, requires more operators there by leading to increased cost. Though it was overcame by sending electro magnetic signals.
  - Multiple people coulnd't use the same route at a single time and much more.

### Packet Switched

- The data is divided to many small packets and sent over the cables under the over ocean from souce to the destination.
- Once the packets reach the destination, they are merged together and they are delivered.
- Works much like a delivery of a package.
- Advantages
  - Doesn't require a dedicated circuit between every communication pair of computers as required by circuit switched networks.
  - Multiple computers can use the cable to send the individual packets at the same time.

## Client Server Architecture

- A _server_ is a program that listens for incoming connections and accepts them.
- Usually, the server listens for a request from a client and sends back a response to the client.

## Protocol

A set of rules which enables the program, the server and the client in this case to communicate with each other. Following are some of the protocols.

- TCP - used to transmit data reliably (trustworthy).
- UDP - used to transmit data quickly but unreliably.
- IP - used to route packets over the network from one computer to another.
- HTTP - used to get web pages and other web requests.
- Ethernet - used to send data over LAN.

## Network layers and abstraction

Here’s a quick overview of what happens when data goes out on the network. We’ll cover this in much more detail in the coming

- A user program says, “I want to send the bytes ‘GET / HTTP/1.1’ to that web server over there.” (Servers are identified by IP address and a port on the Internet–more on that later.)
- The OS takes the data and wraps it up in a header (that is, prepends some data) that provides error detection (and maybe ordering) information. The exact structure of this header would be defined by a protocol such as TCP or UDP.
- The OS takes all of that, and wraps it up in another header that helps with routing. This header would be defined by the IP protocol.
- The OS hands all that data to the network interface card (the NIC–the piece of hardware that’s responsible for networking).
- The NIC wraps all that data up into another header that’s defined by a protocol such as Ethernet that helps with delivery on the LAN.
- The NIC sends the entire, multiply wrapped data out over the wire, or over the air (with WiFi).

When the receiving computer gets the packet, the reverse process happens. Its NIC strips the Ethernet header, the OS makes sure the IP address is correct, figures out which program is listening on that port, and sends it the fully unwrapped data.
All these different layers that do all this wrapping are together called the protocol stack. (This is a different usage of the word “stack” than the stack abstract data type.)
This works well because each layer is responsible for different parts of the process, e.g. one layer handles data integrity, and another handles routing the packet over the network, and another handles the data itself that is being transmitted between the programs. And each layer doesn’t care about what the layers below it are doing with the data.
It’s that last concept that’s really important: when data is going over WiFi, the WiFi hardware doesn’t even care what the data is, if it’s Internet data or not, how integrity is assured (or not). All WiFi cares about is getting a big chunk of data transmitted over the air to another computer. When it arrives at the other computer, that computer will strip off the Ethernet stuff and look deeper in the packet, deciding what to do with it.
And since the layers don’t care what data is encapsulated below them, you can swap out protocols at various layers and still have the rest of them work. So if you’re writing a program at the top layer (where we tend to write them most commonly), you don’t care what’s happening at the layers below that. It’s Somebody Else’s Problem.
For example, you might be getting a web page with HTTP/TCP/IP/Ethernet, or you might be transmitting a file to another computer with TFTP/UDP/IP/Ethernet. IP and Ethernet work fine in both cases, because they are indifferent about the data they are sending.
There are many, many details omitted from this description, but we’re still in high-level overview land.

## Difference between Wired versus Wireless networks

- Computers are connected to a LAN either via a physical ethernet cable or a wifi access point.
- They both use Ethernet protocol for low level communication.

## Introducing The Sockets API

- In Unix, the sockets API gives processes a way to communicate with each other.
- Its is a blend of libray calls and system call which are nothing but the functions directly called by the OS.
- It supports a variety of methods of communication, and one of them is over the Internet.

## Client Connection Process

Following are the steps to connect to another computer using sockets.

- Ask the OS for a socket
  - Usually an integer called file descriptor, user to refer to this network connection.
- Perform a DNS lookup
  - DNS is a distributed database which helps to convert human readble name to IP addresses.
- Connect the socket to that IP address on a specific port.
  - Port 80 is the standart port used for servers that HTTP protocol.
- Send data and receive data.
- Close the connection.

## Server Listening Process

- Ask the OS for a socket
- Bind the socket to a port
  - A port number is assigned here so that the clients can connect to.
  - Program's that aren't run as admin cannot be bind to ports under 1024 since they are reserved.
  - Ports are per computer, two differenct computers can use the same port.
  - Clients are bound to port, as well.
- Listen for incoming connections
  - Let the OS know when there is an incoming connection.
- Accetp incoming connections
  - The server will sleep when you try to accept a new connection if none are pening, and wakes up when someone tries to connect.
  - The connection is made with the client, a new socket is returned specifically for that connection. It helps to handle multiple clients at once.
- Send data and receive data
  - The server recieves the request from the client and the sends back the response.
- Go back and accept another connection.

## Questions

- What role does bind() play on the server side?

  - The bind method helps to assign a port to the server.

- Would a client ever call bind()? (Might have to search this one on the Internet.)

  - On the client side, you would only use bind if you want to use a specific client-side port, which is rare. Usually on the client, you specify the IP address and port of the server machine, and the OS will pick which port you will use. Generally you don't care, but in some cases, there may be a firewall on the client that only allows outgoing connections on certain port. In that case, you will need to bind to a specific port before the connection attempt will work.

- Speculate on why accept() returns a new socket as opposed to just reusing the one we called listen() with.

- What would happen if the server didn’t loop to another accept() call? What would happen when a second client tried to connect?

- If one computer is using TCP port 3490, can another computer use port 3490?
  - Yes, since ports are per computer and hence two computers can use the same port.
- Speculate about why ports exist. What functionality do they make possible that plain IP addresses do not?
  - The port helps to identify to which process the received data should be sent to on the host.
  - A computer can have multiple simultaneous connections, all receiving data for different processes (mail, web, database, etc). How does the computer tell which data goes where? When the computer receives data, the port information allows it to give the data to the correct process. Eg, data with port 80 should go to the http process, data with port 25 should go to the mail processes and so on.

## Network definitions

### IP Address

- A 4 byte unique number used to identify your computer on the internet.

### Port

- Programs talk through ports, which are numbered 0-65535 and are associated with the TCP or UDP protocols.

### Transmission Control Protocol (TCP)

- Responsible for reliable and inorder data transmission.
- Make packet switched network feel more like a circuit switched network.
- TCP used port numbers to identify senders and receivers of a data.
- In sockets API, TCP sockets are called stream sockets.

### User Datagram Protocol (UDP)

- Lightweight sibling of TCP.
- Doesn't guarantee data will arrive, or that it will be in order, or that it won't be dublicated.
- If it arrives, it will be error free.
- In sockets API, UDP sockets are called datagram sockets.

### IPv6

- Since 4 bytes is enough to hold a unique address, the address size is increased to 16 bytes.

### Network Address Translation (NAT)

- Private subnets with non globally unique addresses that get translated to globally unique addresses as they pass through the router.
- Private subnets commonly starts witha addresses 192.168.x.x or 10.x.x.x.

### Router

- A specialized computer that forwards packets through the packet switching network. It inspects destination IP addresses to determine which route will get the packet closer to its goal.

### Internet Protocol

- Responsible for identifying computers by IP address and using those address to route data to recipients through a variety of routers.

### Local Area Network (LAN)

- A network where all the computers are effectively directly connected, not via a router.

### Interface

- Physical networking hardware on a computer.
- A computer can have a number of interfaces, but most likely have two one for wired Ethernet interface and the other for wireless Ethernet interface.
- A router might have a large number of interfaces to be able to route packets to a large number of destinatins.
- Home router probably has two interfaces: one facing inward to your LAN and the other facing outward to the rest of the Internet.
- Each interface typically has one IP address and one MAC address.
- The OS names interfaces on your local machine, they might be something like wlan0 or eth2 or something else, depends of the hardware and the OS.

### Header

- Data that is prepended to some other data by a particular protocol, which contains appropriate information about that protocol.
- TCP header contains some error detection information, correction information and a source and destination port numbner.
- IP would include the source and the destination IP addresses.
- Ethernet would include the source and the destination MAC addresses.
- HTTP contains length of the data, the date modified and the status of the request.
- Analogous to adding a letter in an envelope.

### Network Adapter

- The hardware on the computer which does the network stuff, also called the network card.

### MAC address

- Ethernet interfaces have MAC addresses, which take the form aa:bb:cc:dd:ee:ff, where the fields are random one-byte hex numbers.
- They are 6 byte and must be unique on the LAN.
- When a network adapter is manufactured, it is given a unique MAC addresses that it keeps for life.

## Layered Network Model

- When data is sent over the internet, the data is encapsulated in different layers of protocols.
- These protocols are responsible for different things, e.g, describing data, preserving data integrity, routing, local delivery, etc.

## Layering of Protocols on Data

Let’s consider what happens with an HTTP request.

The web browser builds the HTTP request that looks like this:

GET / HTTP/1.1
Host: example.com
Connection: close
And that’s all the browser cares about. It doesn’t care about IP routing or TCP data integrity or Ethernet.

It just says “Send this data to that computer on port 80”.

The OS takes over and says, “OK, you asked me to send this over a stream-oriented socket, and I’m going to use the TCP protocol to do that and insure all the data arrives intact and in order.”

So the OS takes the HTTP data and wraps it in a TCP header which includes the port number.

And then the OS says, “And you wanted to send it to this remote computer whose IP address is 198.51.100.2, so we’ll use the IP protocol to do that.”

And it takes the entire TCP-HTTP data and wraps it up an an IP header. So now we have data that looks like this: IP-TCP-HTTP.

After that, the OS takes a look at its routing table and decides where to send the data next. Maybe the web server is on the LAN, conveniently. More likely, it’s somewhere else, so the data would be sent to the router for your house destined for the greater Internet.

In either case, it’s going to send the data to a server on the LAN, or to your outbound router, also on the LAN. So it’s going to a computer on the LAN.

And computers on the LAN have an Ethernet address (AKA MAC address–which stands for “Media Access Control”), so the sending OS looks up the MAC address that corresponds to the next destination IP address, whether that’s a local webserver or the outbound router. (This happens via a lookup in something called the ARP Cache, but we’ll get to that part of the story another time.)

And it wraps the whole IP-TCP-HTTP packet in an Ethernet header, so it becomes Ethernet-IP-TCP-HTTP. The web request is still in there, buried under layers of protocols!

And finally, the data goes out on the wire (even if it’s WiFi, we still say “on the wire”).

The computer with the destination MAC address, listening carefully, sees the Ethernet packet on the wire and reads it in. (Ethernet packets are called Ethernet frames.)

It strips off the Ethernet header, exposing the IP header below it. It looks at the destination IP address.

If the inspecting computer is a server and it has that IP address, its OS strips off the IP header and looks deeper. (If it doesn’t have that IP address, something’s wrong and it discards the packet.)

It looks at the TCP header and does all the TCP magic needed to make sure the data isn’t corrupted. If it is, it replies back with the magic TCP incantations, saying, “Hey, I need you to send that data again, please.”

Note that the web browser or server never knows about this TCP conversation that’s happening. It’s all behind the scenes. For all it can see, the data is just magically arriving intact and in order.

The reason is that they’re on a higher layer of the network. They don’t have to worry about routing or anything. The lower layers take care of it.

If everything’s good with TCP, that header gets stripped and the OS is left with the HTTP data. It wakes up the process (the web server) that was waiting to read it, and gives it the HTTP data.

But what if the destination Ethernet address was an intermediate router?

The router strips off the Ethernet frame as always.

The router looks at the destination IP address. It consults its routing table and decides to which interface to forward the packet.

It sends it out to that interface, which wraps it up in another Ethernet frame and sends it to the next router in line.

(Or maybe it’s not Ethernet! Ethernet is a protocol, and there are other low-level protocols in use with fiber optic lines and so on. This is part of the beauty of these layers of abstraction–you can switch protocols partway through transmission and the HTTP data above it is completely unaware that any such thing has happened.)

## The Internet Layer Model

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Layer</th>
<th scope="col" class="org-left">Responsibility</th>
<th scope="col" class="org-left">Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Application</td>
<td class="org-left">Structured application data</td>
<td class="org-left">HTTP, FTP, TFTP, Telnet, SSH, SMTP, POP, IMAP</td>
</tr>

<tr>
<td class="org-left">Transport</td>
<td class="org-left">Data integrity, packet splitting, reassembly</td>
<td class="org-left">TCP, UDP</td>
</tr>

<tr>
<td class="org-left">Internet</td>
<td class="org-left">Routing</td>
<td class="org-left">IP, IP6, ICMP</td>
</tr>

<tr>
<td class="org-left">Link</td>
<td class="org-left">Physical, signal on wires</td>
<td class="org-left">Ethernet, PPP, token ring</td>
</tr>
</tbody>
</table>

- All programs that implement HTTP, FTP or SMTP can use TCP or UPD to transmit data.
- All data that's transmitted with TCP or UDP can use IP, IP6 for routing.
- All data that used IP, IP6 for routing can use Ethernet or PPP for going over the wire.
- When the data is being transmitted through the layers, the protocols add their own headers on top of everything else so far.
- Since there are other networks that aren't the Internet, there is a general model call the OSI model.

## The ISO OSI Network Layer Model

- International Organization for Standardization Open Systems Interconnect model.
- OSI model is like the Internet model, but more granular.
- The Internet model maps to the OSI model, like so, with a single layer of the Internet model mapping to multiple layers of the OSI model.

| ISO OSI Layer | Internet Layer |
| ------------- | -------------- |
| Application   | Application    |
| Presentation  | Application    |
| Session       | Application    |
| Transport     | Transport      |
| Network       | Network        |
| Data link     | Link           |
| Physical      | Link           |

## Protocols

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
<thead>
<tr>
<th scope="col" class="org-left">ISO OSI Layer</th>
<th scope="col" class="org-left">Responsibility</th>
<th scope="col" class="org-left">Protocols</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Application</td>
<td class="org-left">Structured application data</td>
<td class="org-left">HTTP, FTP, TFTP, Telnet, SMTP, POP, IMAP</td>
</tr>

<tr>
<td class="org-left">Presentation</td>
<td class="org-left">Encoding, Translation, Encryption, Compression</td>
<td class="org-left">MIME, SSL/TLS, XDR</td>
</tr>

<tr>
<td class="org-left">Session</td>
<td class="org-left">Suspending, terminating, restarting sessions between computers</td>
<td class="org-left">Sockets, TCP</td>
</tr>

<tr>
<td class="org-left">Transport</td>
<td class="org-left">Data Integrity, packet splitting and re assemply</td>
<td class="org-left">TCP, UDP</td>
</tr>

<tr>
<td class="org-left">Network</td>
<td class="org-left">Routing</td>
<td class="org-left">IP, IPv6, ICMP</td>
</tr>

<tr>
<td class="org-left">Data link</td>
<td class="org-left">Encapsulation into frames</td>
<td class="org-left">Ethernet, PPP, SLIP</td>
</tr>

<tr>
<td class="org-left">Physical</td>
<td class="org-left">Physical, signals of wires</td>
<td class="org-left">Ethernet physical layer, DSL, ISDN</td>
</tr>
</tbody>
</table>

## Questions

- When a router sees an IP address, how does it know where to forward it?
- If an IPv4 address is 4 bytes, roughly how many different computers can that represent in total, assuming each computer has a unique IP address?
- Same question, except for IPv6 and its 16-byte addresses?
- Bonus question for stats nerds: The odds of winning the super lotto jackpot are approximately 300 million to 1. What are the odds of randomly picking my pre-selected 16-byte (128-bit) number?
- Speculate on why IP is above TCP in the layered model. Why does the TCP header go on before the IP header and not the other way around?
- If UDP is unreliable and TCP is reliable, speculate on why one might ever use UDP.

## The Internet Protocol

- Protocol responsible for routing packets of data around the Internet, analogous to how the post office is responsible for routing letters aroung the mail network.
- _Host_ is just an another name for a computer.
- There are two versions of IP: version 4 (4 bytes) and version 6 (16 bytes).

## Subnets

- Every IP address is split into two portions
- The initial bits of the IP identify the individual networks.
- The trailing bits identify the individual hosts on that network.
- These individual networks are called _subnets_ and the number of hosts they can support depend on how many bits they're reserved for identifying the hosts on that subnet.

## Example

As a contrived non-Internet example, let’s look at an 8-bit “address”, and we’ll say the first 6 bits are the network number and the last 2 bits are the host number.

So an address like this:

00010111
is split into two parts (because we said the first 6 bits were the network number):

Network Host
--&#x2013;&#x2014; -&#x2014;
000101 11
So this is network 5 (101 binary), host 3 (11 binary).

The network part always comes before the host part.

Note that if there are only two “host” bits, there can only be 4 hosts on the network, numbered 0, 1, 2, and 3 (or 00, 01, 10, and 11 in binary).

And with IP, it would actually only be two hosts, because hosts with all zero bits or all one bits are reserved.

## Additional IP layer protocols

- ICMP: Internet Control Message Protocol, a mechanism for communicating IP notes to talk about IP control metadata with one another.
- IPSec: Internet Protocol Security, encryption and authentication functionality.

## Private Networks

There are private networks hidden behind routers that do not have globally unique IP addresses on their machines. (Though they do have unique addresses within the LAN itself.)

This is made possible through the magic of a mechanism called NAT (Network Address Translation). But this is a story for the future.

For now, let’s just pretend all our addresses are globally unique.

## Static versus Dynamic IP addr and DHCP

If you have clients hitting your website, or you have a server that you want to SSH into repeatedly, you’ll need a static IP. This means you get a globally-unique IP address assigned to you and it never changes.

This is like having a house number that never changes. If you need people to be able to find your house repeatedly, this needs to be the case.

But since there are a limited number of IPv4 addresses, static IPs cost more money. Often an ISP will have a block of IPs on a subnet that they dynamically allocate on-demand.

This means when you reboot your broadband modem, it might end up with a different public-facing IP address when it comes back to life. (Unless you’ve paid for a static IP.)

Indeed, when you connect your laptop to WiFi, you also typically get a dynamic IP address. Your computer connects to the LAN and broadcasts a packet saying, “Hey, I’m here! Can anyone tell me my IP address? Pretty please with sugar on top?”

And this is OK because people aren’t generally trying to connect to servers on your laptop. It’s usually the laptop that’s connecting to other servers.

How does it work? On one of the servers on the LAN is a program that is listening for such requests, which conform to DHCP (the Dynamic Host Configuration Protocol). The DHCP server keeps track of which IP addresses on the subnet are already allocated for use, and which are free. It allocates a free one and sends back a DHCP response that has your laptop’s new IP address, as well as other data about the LAN your computer needs (like subnet mask, etc.).

If you have WiFi at home, you very likely already have a DHCP server. Most routers come from your ISP with DHCP already set up, which is how your laptop gets its IP address on your LAN.

## IP4 and IP6

[Refer documentation](https://beej.us/guide/bgnet0/html/#the-internet-protocol-version-4)
