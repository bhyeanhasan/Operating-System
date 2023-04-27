
### Open Terminal and run these commands
```
sudo apt update
sudo apt install build-essential
gcc --version
```
### If gcc is not installed run below
```
sudo apt install gcc
```

### Now create a c file (hello.c) in Desktop and put some code.Then compile and run the file using below command <br>

- **pwd >** তুমি কোন লোকেশনে আছো তা দেখাবে <br>
- **ls  >**  যেখানে আছো সেই ফোল্ডারে আর কি কি ফাইল অথবা ফোল্ডার আছে তা দেখাবে <br>
- **cd  >** এক ফোল্ডার থেকে আরেক ফোল্ডারে যেতে চাইলে, এখানে ডেস্কটপে যাওয়ার জন্য cd Desktop <br>
- **gcc -o hello hello.c - hello.c >** ফাইলটাকে রান করতে হলে আগে কম্পাইল করে নিতে হবে, আমরা এখানে hello নামে কম্পাইল করছি <br>
- **./hello >** কম্পাইল করা ফাইল রান করতে <br>
```
pwd
cd Desktop
ls
gcc -o hello hello.c
ls
./hello
```

Using terminal Create a C file, Write code , Compile and Run the code
```
$ touch hello.c
$ cat << EOF >> hello.c
> #include<stdio.h>
> int main()
> { 
> printf("Hello");
> }
> EOF
$ gcc -o hellorun hello.c
$ ./hellorun
```

