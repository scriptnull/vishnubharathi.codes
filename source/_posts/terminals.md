---
title: "Terminals"
date: 2018-08-16T23:50:05+05:30
draft: false
tags: ["linux", "software"]
---

IDEs helped me a lot during the early days of my programming journey (2011 - 2014) to build and run programs. I was addicted to few things like Turbo C++, Visual Studio, Eclipse, Android Studio etc. over those period. I spent enough time to memorize every cool shortcut in them and even the places where most frequently used options are present in the menu bars.

After sometime, I started learning this cool new technology that had been spreading like wildfire in the internet called node.js. To my surprise, this does not need GBs of memory to install fancy IDEs. It could be written from simple text editors like Sublime Text (which at that time was super cool) and could be run easily with a command in Command Prompt (Those were my Windows days!)

I was feeling super powerful by the way node.js ecosystem was supported by npm. You type this little command `npm install` on your terminal and BAM! You get really nice libraries that you could use while building applications in matter of minutes.

Ever since then, I was kind of preferring Terminal-based development over IDE-based development. Few years down the line, it is 2018 now and I don't use IDEs. I simply trust my code editors with minimal plugins and my terminal.

I think Terminals are one of the most powerful tools and I always wanted to learn about their internals.

Today, I read this blog post from Microsoft, ["Windows Command-Line: Introducing the Windows Pseudo Console (ConPTY)"](https://blogs.msdn.microsoft.com/commandline/2018/08/02/windows-command-line-introducing-the-windows-pseudo-console-conpty/) which intrigued me to understand about them more.

So, here I am, sitting with Chapter 62: Terminals in [The Linux Programming Interface](https://nostarch.com/tlpi).

## History

A small history lesson on Terminals that everyone tells.

So, Terminals were just CRT displays connected to big computers in early days (1980s). They are just capable of getting character inputs line by line and send the commands to the actual machine for processing. These terminals were connected via RS-232 ( Don't miss https://en.wikipedia.org/wiki/RS-232 ) They were also called as Teletypes (nowadays denoted by tty)

Then came general purpose computers which could run multiple applications and terminal was no more the only thing that was running on the displays, rather it became one of the things that are running alongside the applications present in the computer via a GUI.

The GUI applications that act as terminal are called Terminal Emulators. Examples include

- xterm

- hyper (the one I am using these days)

- Terminator (quitted after using it for few hours)

- Guake (I have seen many people love it due to a single key shortcut which brings and hides this emulator )

One of the interesting things I recently came across is [xterm.js](https://xtermjs.org/), which could be used to render a terminal emulator on a webpage. Example implementation include terminal emulators provided by cloud platforms like Google Cloud. I always wondered how Google Cloud is able to render terminal applications like vi on its web console.

## Terminal Driver

Terminals are controlled by terminal driver (a theory up until this point), which operates in two modes. This driver operates in two modes

__Canonical Mode__: Terminal input is read line by line. This is the defult input mode and you might have seen this while running commands in terminal.

__Non-Canonical Mode__: Terminal input is read character by character. Example: programs like vi, more, less etc. use this mode to get input.

The Terminal driver is the bridge between the terminal device and process running a program. It also interprets the special characters like CTRL+C and signals the process getting it to terminate. Terminal driver operates on two queues. I am curious to read the code of terminal driver at this point to actually see the presence of this data structure.

<center>
![terminal](/images/terminal.png)
</center>

## stty
stty is a command line program, can get and set options for a terminal device interface. By default, it outputs the attributes of the current terminal device on which it is accepting standard input.

```
$ stty -a
speed 38400 baud; rows 53; columns 200; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = M-^?; eol2 = M-^?; swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc ixany imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
```

`speed 38400 baud` is the speed of the terminal line speed (bits per second)

```
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = M-^?; eol2 = M-^?; swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V; discard = ^O;
```

The above options denote the key combination for sending special characters like interrupt character, suspend etc. This means that, these characters will be caught by the terminal driver in canonical mode and corresponding signals will be sent to the process listening, rather than the literal character itself. In case of non-canonical mode, the process will receive the literal character in the standard input.

![terminal-stty](/images/stty-intr.gif)

```
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc ixany imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke -flusho -extproc
```

The above seen options denote various terminal flags. `echo` means the echo flag is on and `-echo` means the echo flag is off.

```
$ stty -echo

# Turns off terminal echoing.
# Everything we type in stdin will be invisible in the terminal
# Helpful for inputting passwords in programs
```

Use `stty sane` to reset the attributes of the terminal.

---

That's it for now!
