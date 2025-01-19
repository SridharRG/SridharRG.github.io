+++
title = "Tools that I came across recently"

[taxonomies]
tags = ["foss", "linux"]

[extra]
toc = false 
+++

#### httrack
---
When I was randomly scrolling in Reddit, i came across a guy asking about how to backup sites and its content in Data hoarder sub reddit. There is came across this free software tool called [httrack](https://www.httrack.com/) which take a backup of all the content in the webpage. I Tried scrapping Prasanna's blog page and the mirror started and scraped the complete file.

#### rclone
---
The another tool which i found is rclone from the same r/data hoarders. This rclone is easy and simple backup solution which can be used to store cloud backup solutions. It offers many features like encryption, auth and many more. This has config for all the cloud providers and I used my institution Google drive to backup all my data which inlcudes my laptop files and home pc files. I got a backstab from my instituion is that they offer 2tb backup for their mail-ids and after i used 91gb of data in the drive they restricted it to 50gb limit. Now i Cant send or receive mails or anything

#### My backup solution
---

I also get to know about the Backup soluiton which everyone talk about. There is something called 3-2-1 backup method or statergy 

- maintain 3 different copies of data, which include one main cope and 2 other redudant copies
- Use 2 different types of media storage, mostly people use one physical storage backup. Physical storage like pendrive or HDD/ssd
- keep one set of backup data off-site

#### rsync
---

When i need to copy a file from my laptop to homeserver, i use this rsync. I just created a folder in my pc and also in my homeserver. Whenever I just want to send some file, i send via rsync and also wrote an alias in my `.zshrc` as i have static ip configured for my homeserver in my router

```bash
rsync -avz ~/Desktop/homeserver-rsync heimdal@192.168.1.3:/home/heimdal/wong-rsync
```

##### Changelog

- 2024-10-05 Updated rsync