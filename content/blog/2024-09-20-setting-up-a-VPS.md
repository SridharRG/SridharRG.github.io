+++
title = "Setting up my VPS"

[taxonomies]
tags = ["linux", "computers"]

[extra]
toc = false 
+++
Finally after a year of tinkering with Linux I got myself a [Virtual Private Server](https://en.wikipedia.org/wiki/Virtual_private_server). In this blog post, I would like to list the things I have done after getting a server.

<div class="center">
<img src="/img/blogs/server.png" alt="neofetch output">
</div>

- **Connect to VPS with SSH** - The first step was to connect to the VPS securely using SSH to ensure encrypted communication.
- **Update package lists and Upgrade packages** - As with any Linux distro, the first essential business is to make sure the packages are upto date.
- **Change root password** - For added security, I updated the root password to something more complex immediately.
- **Create non-root user** - As a best practise to avoid using the root user for day to day operations, I created a new user with sudo privileges.
- **Login with SSH Key** - I setup SSH key based authentication ensuring the future logins doesn't require password for the new user.
- **Disable Password Login** - Once the SSH key is in place, I disabled the password login to prevent unauthorized access
- **Disable root login** - Disabling root login over SSH adds an extra layer of security, ensuring only non-root users can access the server.
- **Update Network and Firewall Policy** - I configured the firewall to allow only necessary services (SSH, HTTP/HTTPS, etc.), using ufw
- **Closed unused ports** - Closed the unused ports to minimize potential entry points for attackers.
- **Install essential tools** - Installed a few essential tools like git and tmux to make woking on the server convenient.


What's Running on the VPS?
Currently, Kafkaa is running on my VPS, hosted with Caddy as the web server. Caddy makes HTTPS setup incredibly simple, handling certificates automatically.  I’m excited about all the possibilities it opens up for self-hosting and further projects in the upcoming days.
 
