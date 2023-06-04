
### Open Terminal and run these commands

### To run java code, we need Java Runtime Environment. If Java Runtime is not installed run below command
For Ubuntu/Debian based systems:
```
sudo apt install default-jdk
```


### Using terminal Create a java file, Write code , Compile and Run the code
```
$ touch HelloWorld.java
$ nano HelloWorld.java
> class HelloWorld{  
>     public static void main(String args[]){  
>      System.out.println("Hello World"); 
>     }
> }
```
Note: The Java source code file name (ending with extension .java) should be the same as the public class name (in here HelloWorld) of the Java program source code. 
That is why we have named our source code file HelloWorld.java <br>
Now press ctrl+o for save & ctrl+x for exit
```
$ javac HelloWorld.java
$ java HelloWorld
```