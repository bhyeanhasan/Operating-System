
## Previous year question

#### Change desktop wallpaper
```
gsettings set org.gnome.desktop.background picture-uri file:///home/noyon/Desktop/wallpaper.jpg
```

## Basic Command

#### Directory related

``` 
goto a directory            $ cd Directory_Name
present working directory   $ pwd
list directory              $ ls
goto preivious directory    $ cd ..
goto home directory         $ cd
```


#### File Related
```
Make a folder               $ mkdir NewFolder
Create a file               $ touch helloworld.c
Copy file/folder            $ cp hello.c /home/noyon/Desktop/newfolder
Move file/folder            $ mv hello.c /home/noyon/Desktop/newfolder
Delete file/folder          $ rm file_name
Rename a file/folder        $ mv old_name new_name
View/Edit file content      $ nano helloworld.c
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
#### Command related help 


##### If you want to know what a command exactly do
```
$ man command_name

```
##### i.e. to show details of "ls" command
```
$ man ls
```
#### Approximate command search
##### i.e. if you forget the name of command to use for showing direcotry  
```
$ man -k directory
or
$ apropos directory
```
##### this will list all commands related to directory.


#### Fun part
```
$ sudo apt install sl
$ sl
$sudo apt install cowsay
$ cowsay aboyob16
```
#### Reboot & ShutDown
##### Reboot
```
$ sudo reboot
or
$ sudo shutdown -r now 
```
Note: 2nd command will perform a system shutdown in a proper way and then reboot the computer.
##### ShutDown
```
$ sudo poweroff
or
$ sudo shutdown -h now 
```
This will perform a system shutdown in a proper way. You can also specify a timer (in seconds), instead of the word "now", for example: 
```
$ shutdown -h -t 30
```
This will bring the computer down in 30 seconds.




