---
title: "Terminals"
date: 2018-08-16T23:50:05+05:30
draft: true

---



IDEs helped me a lot during the early days of my programming journey (2011 - 2014) to build and run programs. I was addicted to few things like Turbo C++, Visual Studio, Eclipse, Android Studio etc. over those period. I spent enough time to memorize every cool shortcut in them and even the places where most frequently used options are present in the menu bars.

After sometime, I started learning this cool new technology that had been spreading like wildfire in the internet called node.js. To my suprise, this does not need GBs of memory to install fancy IDEs. It could be written from simple text editors like Sublime Text (which at that time was super cool) and could be run easily with a command in Command Prompt (Those were my Windows days!)

I was feeling super powerful by the way node.js ecosystem was supported by npm. You type this little command `npm install` on your terminal and BAM! You get really nice libraries that you could use while building applications in matter of minutes.

Eversince then, I was kind of preferring Terminal-based development over IDE-based development. Few years down the line, it is 2018 now and I don't use IDEs. I simply trust my code editors with minimal plugins and my terminal.

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

One of the interesting things I recently came across is [xterm.js](https://xtermjs.org/), which shows the state of terminals at this point of time.

## Modes

Terminals are controlled by terminal driver (a theory up until this point), which operates in two modes. This driver operates in two modes

__Canonical Mode__: Terminal input is read line by line. This is the defult input mode and you might have seen this while running commands in terminal.

__Non-Canonical Mode__: Terminal input is read character by character. Example: programs like vi, more, less etc. use this mode to get input.

The Terminal driver also interprets the special characters like CTRL+C and signals the program getting it to terminate.

## Limits

Terminal driver operates on two queues. I am curious to read the code of terminal driver at this point to actually see the presence of this data structure. But here is a 


