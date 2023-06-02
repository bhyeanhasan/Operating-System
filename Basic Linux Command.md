
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


#### Copy file or folder
```
cp hello.c /home/noyon/Desktop/newfolder
```

#### Move file or folder
```
mv hello.c /home/noyon/Desktop/newfolder
```

#### Delete file 
```
rm newfolder
```

#### Make a folder
```
mkdir NewFolder
```

#### Create a file
```
touch helloworld.c
```

#### Rename a file
```
mv old_name new_name
```

#### View a file content without editing
```
cat helloworld.c
```

#### Edit a file (ctrl+o for save , ctrl+x for exit the file)
```
nano helloworld.c
```

#### Write in a file
```
echo "It will replace old text" > hello.c
echo "New line to be added at the end" >> hello.c
```

#### Write multiple line
```
$ cat << EOF > hello.c
> It will add multiple line one by one
> But it will replace previous text
> EOF

$ cat << EOF >> hello.c
> It will add multiple line one by one
> Lines will adedd at the end of the file
> EOF

$ nano hello.c
```


#### Search in text
```
grep "Hello" helloworld.c
```

#### unzip a file
```
unzip new.zip
```
