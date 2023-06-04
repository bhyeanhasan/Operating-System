
## Previous year question

#### Change desktop wallpaper
```
gsettings set org.gnome.desktop.background picture-uri file:///home/noyon/Desktop/wallpaper.jpg
```

## Basic Command

#### Ubuntu Shortcut

``` 
Open Terminal            $ ctrl + alt + T
Close Terminal           $ ctrl + D
clear the terminal       $ clear
```

#### Directory related

``` 
goto a directory            $ cd Directory_Name
present working directory   $ pwd
list directory              $ ls
goto preivious directory    $ cd ..
goto home directory         $ cd
goto root directory         $ cd /
```


#### File Related
```
Make a folder                            $ mkdir NewFolder
Create a file                            $ touch helloworld.c
Copy file/folder                         $ cp hello.c /home/noyon/Desktop/newfolder
Move file/folder                         $ mv hello.c /home/noyon/Desktop/newfolder
Delete file                              $ rm file_name
Delete folder with sub-folder/files      $ rm -r dir_name
Rename a file/folder                     $ mv old_name new_name
View/Edit file content                   $ nano helloworld.c
                                           (ctrl+o for save , ctrl+x for exit the file)
```

#### Query Related
```
Find a file                 $ find /home -name notes.txt
Search in a file            $ grep "Hello" helloworld.c
Show first 10 lines         $ head filename.txt
Show last 10 lines          $ tail filename.txt
All the running processes   $ top
History                     $ history
pc Uptime                   $ uptime
runing OS info              $ uname -a

```

#### Reboot & ShutDown
```
Reboot                      $ sudo reboot
ShutDown                    $ sudo poweroff
Reboot after 30 sec         $ shutdown -r -t 30
ShutDown after 30 sec       $ shutdown -h -t 30
```


#### Command related help 

##### 
```
If you want to know what a command exactly do           $ man command_name
Such as want to know what 'ls' command exactly do       $ man ls

If you forget the any command                           $ man -k 'any'
Such as forget the 'directory' command                  $ man -k directory
```

#### Date and Time
```
Show date & time status    $ timedatectl
Auto time sync off         $ timedatectl set-ntp 0
Change time & date         $ timedatectl set-time "YYYY-MM-DD HH:MM:SS"
Auto time sync on          $ timedatectl set-ntp 1
Set the time zone          $ timedatectl set-timezone 'Asia/Kolkata'
```
#### Security
```
Change current user's password      $ passwd
(it's 'passwd' not password)
to Change root password             $ sudo passwd

#### Fun part
```
$ sudo apt install sl
$ sl
$ sudo apt install cowsay
$ cowsay aboyob16
$ yes I Love You
```
#### Network related
```
Find the route of an ip/host    $ traceroute pstu.ac.bd
ICMP Ping                       $ ping pstu.ac.bd
IP info                         $ ifconfig -a
SSH connection                  $ ssh username@hostname
network scan                    $ nmap ip
```
