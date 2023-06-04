
### Open Terminal and run these commands

### To run C++ code, we need GNU C++ compiler called g++. If g++ is not installed run below command
```
sudo apt install g++
```

### Using terminal Create a C++ file, Write code , Compile and Run the code
```
$ touch hello.cpp
$ cat << EOF >> hello.cpp
> #include <bits/stdc++.h>
> using namespace std;
> int main()
> { 
> cout<<"Hello Wordl\n"<<endl;
> }
> EOF
$ g++ -o hellorun hello.cpp
$ ./hellorun
```
