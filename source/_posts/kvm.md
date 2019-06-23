---
title: KVM
date: 2019-06-22 12:55:49
tags: ["linux"]
---

Yesterday, I somehow arrived at [Firecracker](https://firecracker-microvm.github.io/) and ended up reading it's design documents. Firecracker is a project by AWS which helps in creation + management of MicroVMS. This is of great interest to me, as I always wondered how AWS Lambda works and I have been interested in secure execution of code on servers for [a long long time](https://github.com/scriptnull/compilex/commit/1d3a3fef1f3dd209aa64a9f38b55034fd318734d#diff-04c6e90faac2675aa89e2176d2eec7d8). 

Firecracker's docs describe that it uses KVM (Kernel-based Virtual Machine) behind the scenes to operate. hmm, KVM huh? I have heard of it before as an alternative to QEMU, Virtual Box etc. Well, is it really the alternative? hmm not sure. Well then what exactly is it?

I consider this to be a good start of learning about various virtualization technologies and probably this will give me good idea about things like, "what is KVM?", "what are Containers?" etc.

So, here we go! A series of Wikipedia pages to read now :D 

(oh I forgot, I haven't used Firecracker or KVM practically yet. So I will see if I could give them a try during this time.)


## Hoping on

First line in [KVM Wikipedia page](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine) states

> Kernel-based Virtual Machine (KVM) is a virtualization module in the Linux kernel that allows the kernel to function as a hypervisor.

ok, wait here...

This arises more questions.

1. If it is the virtualization module in Linux Kernel, what other modules does the kernel have?
2. What is a Hypervisor?

## Kernel modules
After googling a bit, I arrived at this [awesome link](https://linux.die.net/lkmpg/x40.html) which teaches about kernel modules.

Basically it is where action is! You can add functionality to the kernel by loading modules to it instead of writing down all the code in the main kernel code. Having this modular approach avoids ending up with a monolithic kernel which has bigger size and complexity.

Ok, let us see what kernel modules are running in my pi. (`lsmod` is our friend)

```
pi@raspberrypi:~/vishnubharathi.codes $ lsmod 
Module                  Size  Used by
rfcomm                 49152  4
bnep                   20480  2
hci_uart               36864  1
btbcm                  16384  1 hci_uart
serdev                 20480  1 hci_uart
bluetooth             368640  29 hci_uart,bnep,btbcm,rfcomm
ecdh_generic           28672  1 bluetooth
fuse                  110592  3
joydev                 20480  0
hid_logitech_hidpp     36864  0
brcmfmac              307200  0
brcmutil               16384  1 brcmfmac
hid_logitech_dj        20480  0
cfg80211              573440  1 brcmfmac
rfkill                 28672  6 bluetooth,cfg80211
snd_bcm2835            32768  1
snd_pcm                98304  1 snd_bcm2835
snd_timer              32768  1 snd_pcm
snd                    69632  5 snd_timer,snd_bcm2835,snd_pcm
evdev                  24576  6
fixed                  16384  0
uio_pdrv_genirq        16384  0
uio                    20480  1 uio_pdrv_genirq
i2c_dev                16384  0
ip_tables              24576  0
x_tables               32768  1 ip_tables
ipv6                  425984  42
```

I could see `.ko` extension files is the artifact that is needed to load a module. So, if you are writing a kernel module you would end up building a `.ko` (kernel object) file. To load this, use the `insmod` command.

I played around a while to see all the available kernel objects that came with my installation and here is what I found.

```
pi@raspberrypi:/lib/modules/4.14.79-v7+/kernel $ ls | xargs -n1 
arch
crypto
drivers
fs
kernel
lib
mm
net
sound
```

The above directories are used to categorize the kernel modules and `fs` is a category, which I suppose is responsible for file systems.

```
fs
├── 9p
│   └── 9p.ko
├── binfmt_misc.ko
├── btrfs
│   └── btrfs.ko
├── cifs
│   └── cifs.ko
├── dlm
│   └── dlm.ko
├── ecryptfs
│   └── ecryptfs.ko
├── fuse
│   ├── cuse.ko
│   └── fuse.ko
├── gfs2
│   └── gfs2.ko
├── hfs
│   └── hfs.ko
├── hfsplus
│   └── hfsplus.ko
├── isofs
│   └── isofs.ko
├── jffs2
│   └── jffs2.ko
├── jfs
│   └── jfs.ko
├── nfs
│   ├── blocklayout
│   │   └── blocklayoutdriver.ko
│   └── flexfilelayout
│       └── nfs_layout_flexfiles.ko
├── nfsd
│   └── nfsd.ko
├── nilfs2
│   └── nilfs2.ko
├── nls
│   ├── nls_cp1250.ko
│   ├── nls_cp1251.ko
│   ├── nls_cp1255.ko
│   ├── nls_cp737.ko
│   ├── nls_cp775.ko
│   ├── nls_cp850.ko
│   ├── nls_cp852.ko
│   ├── nls_cp855.ko
│   ├── nls_cp857.ko
│   ├── nls_cp860.ko
│   ├── nls_cp861.ko
│   ├── nls_cp862.ko
│   ├── nls_cp863.ko
│   ├── nls_cp864.ko
│   ├── nls_cp865.ko
│   ├── nls_cp866.ko
│   ├── nls_cp869.ko
│   ├── nls_cp874.ko
│   ├── nls_cp932.ko
│   ├── nls_cp936.ko
│   ├── nls_cp949.ko
│   ├── nls_cp950.ko
│   ├── nls_euc-jp.ko
│   ├── nls_iso8859-13.ko
│   ├── nls_iso8859-14.ko
│   ├── nls_iso8859-15.ko
│   ├── nls_iso8859-1.ko
│   ├── nls_iso8859-2.ko
│   ├── nls_iso8859-3.ko
│   ├── nls_iso8859-4.ko
│   ├── nls_iso8859-5.ko
│   ├── nls_iso8859-6.ko
│   ├── nls_iso8859-7.ko
│   ├── nls_iso8859-9.ko
│   ├── nls_koi8-r.ko
│   ├── nls_koi8-ru.ko
│   ├── nls_koi8-u.ko
│   └── nls_utf8.ko
├── ntfs
│   └── ntfs.ko
├── ocfs2
│   ├── cluster
│   │   └── ocfs2_nodemanager.ko
│   ├── dlm
│   │   └── ocfs2_dlm.ko
│   ├── dlmfs
│   │   └── ocfs2_dlmfs.ko
│   ├── ocfs2.ko
│   ├── ocfs2_stackglue.ko
│   ├── ocfs2_stack_o2cb.ko
│   └── ocfs2_stack_user.ko
├── overlayfs
│   └── overlay.ko
├── quota
│   ├── quota_tree.ko
│   ├── quota_v1.ko
│   └── quota_v2.ko
├── reiserfs
│   └── reiserfs.ko
├── squashfs
│   └── squashfs.ko
├── ubifs
│   └── ubifs.ko
├── udf
│   └── udf.ko
└── xfs
    └── xfs.ko

30 directories, 73 files
```

Yeah! I could see some well know file system names. Does that mean a file system is just a kernel module and to write a file system, all I need to do is write down code and generate a `.ko` file and load it? (Strong guess from me is YES, but I will only know for sure if I attempt writing one or is someone who have attempted could tell me -- let me know if you know the answer for this!)

## Hypervisor

According to wikipedia, 

> A hypervisor or virtual machine monitor (VMM) is computer software, firmware or hardware that creates and runs virtual machines.  

I have heard of this word "hyper" in the Windows world like "Turn on Hyper-V". Well I turned it on, but without knowing what exactly it is. Now I have the answer. Hyper-V is the a hypervisor built into Windows (just like how KVM is for linux)


## Paravirtualization
While reading about KVM, I came across a concept named Paravirtualization. Here is the Wikipedia verses,

> A hypervisor provides the virtualization of the underlying computer system. In full virtualization, a guest operating system runs unmodified on a hypervisor. However, improved performance and efficiency is achieved by having the guest operating system communicate with the hypervisor. By allowing the guest operating system to indicate its intent to the hypervisor, each can cooperate to obtain better performance when running in a virtual machine. This type of communication is referred to as paravirtualization.

And there is a line in KVM Wikipedia that states about the support for paravirtualization in KVM

> KVM provides paravirtualization support for Linux, OpenBSD,[12] FreeBSD,[13] NetBSD,[14] Plan 9[15] and Windows guests using the VirtIO[16] API. This includes a paravirtual Ethernet card, disk I/O controller,[17] balloon device, and a VGA graphics interface using SPICE or VMware drivers.

This line is important, because it is helping me understand the practical sense of paravirtualization. Best example: when I had run VMs previously, I noticed that the VM could connect to the host operating system and access the internet via a network connection through the host. This means the Guest operating system is able to speak with the host operating system and communicate its intent. I think this kind of capability is called Paravirtualization.

## KVM Structure
![kvm-structure](https://upload.wikimedia.org/wikipedia/commons/4/40/Kernel-based_Virtual_Machine.svg)

## libvirt
I first encountered libvirt while checking out [Digital Ocean's libvirt Go package](https://github.com/digitalocean/go-libvirt). libvirt is an open-source API written in C (with bindings in other languages) to manage virtualization. Hypervisors will be using this library to actually create and manage virtual machines.

![libvirt](https://upload.wikimedia.org/wikipedia/commons/d/d0/Libvirt_support.svg)

## Time for action
I think I kind of went through some basic reading materials. Now I am going to try to create a virtual machine using the kvm interface.

I am on a raspberry pi and my lsmod already revealed that I don't have kvm kernel module loaded. KVM's support as per the official page is for CPUs running on Intel or AMD. So, I going to spin up a virtual machine in Digital Ocean to play around.

Doing an `lsmod` in my DO (Digital Ocean) box revealed that my `kvm.ko` and `kvm_intel.ko` are loaded.

```
root@dev:~# lsmod | grep kvm 
kvm_intel             212992  0
kvm                   598016  1 kvm_intel
irqbypass              16384  1 kvm
```

`libvirtd` seems to be an important component, because it is the daemon that exposes a socket for accessing libvirt API to manage VMs

```
root@dev:~# file /var/run/libvirt/libvirt-sock
/var/run/libvirt/libvirt-sock: socket
```

`virsh` is the command line client that connects to this socket and provides a CLI interface for managing the VMs

```
root@dev:~# virsh list --all 
 Id    Name                           State
----------------------------------------------------

```

Currently no VMs are present as per virsh.

Let us try creating one!

The process dealt with installing somepackes namely `virt-manager`, `libvirt-bin`, `libosinfo-bin`

After some strong belief on virsh and virt-install tools, I just successfully created a VM running alpinelinux3.8

![virsh-alpine](/images/virsh-alpine.png)

I used `virt-install` to create the VM

```
virt-install --memory=128 \
	--vcpus=1 \
	--cpu=host \
	--name=a38 \
	--cdrom=alpine-virt-3.8.0-x86_64.iso \
	--os-variant=alpinelinux3.8 \
	--disk size=5 
```

To manage this VM,

```
virsh list
virsh connect a38
virsh shutdown a38
virsh destroy a38
```

Before closing, I would like to check one more thing, "Where does the kvm kernel object sit?"

```
root@dev:/lib/modules/4.15.0-52-generic/kernel# find . -name kvm.ko
./arch/x86/kvm/kvm.ko
```

I also noticed this thing called `irqbypass.ko` which is being used by `kvm.ko` [...](https://lwn.net/Articles/653706/)
