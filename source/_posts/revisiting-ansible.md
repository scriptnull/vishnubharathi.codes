---
title: "Revisiting Ansible"
date: 2018-06-05T19:46:53+05:30
draft: false
tags: ["devops", "ansible", "terraform"]
---

I used [ansible](https://www.ansible.com/) at [work](https://www.shippable.com/) few months back. Today, I faced a problem at [work](https://www.shippable.com/), trying to connect to a virtual machine on Google Cloud Platform created with ansible. I didn't feel surprised, when I was not able to be productive on it immediately, because I didn't learn ansible as much as I learnt [terraform](https://www.terraform.io/). I learnt both of them using the docs. If you ask me to do something dealing with multiple machines, I would probably prefer terraform over ansible. Reason for this would be

- I prefer HCL (HashiCorp Configuration Language) over YAML.
- The documentation of terraform and all the projects by [HashiCorp](https://www.hashicorp.com/) are pretty good at convincing me to do something in their way.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">lol. I was just writing a blog post and I got hit by this. 🎯<br><br>Thanks for bringing it to notice. 👀<br><br>BTW, I love <a href="https://twitter.com/HashiCorp?ref_src=twsrc%5Etfw">@HashiCorp</a> and all the stuff you guys do. 📰<br><br>Still thinking how I didn&#39;t notice this all these days 🤔</p>&mdash; Vishnu Bharathi (@scriptnull) <a href="https://twitter.com/scriptnull/status/1004022026682621954?ref_src=twsrc%5Etfw">June 5, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

But, ansible is a great tool (based on my first encounter with it and the amount of stuff they are doing) and I don't want to be missed out in the party. I really would like to figure out when to use ansible and when not to. The documentation probably has lot of things and is kind of scary for me. I had gone over a lot of things in there already few months back and I remember almost nothing. So, this time I am taking a different route - I just signed up for Linkedin Learning (Lynda) and started watching [Learning ansible course](https://www.linkedin.com/learning/learning-ansible). Proabably this could help me remember core concepts of ansible.

## Introduction
- Ansible is a task execution engine.
- It helps computer people run some tasks on remote computers or on the machine on which ansible is running.
- Configured using YAML - which could be source controlled and reused.
- Open Source Project: https://github.com/ansible/ansible and written in python.

## Installation
Python is a prerequisite and since I am trying this out on macOS, I am supposed to have pip installed for installing ansible.

```bash
# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user

# install ansible
pip install ansible --user
```

## No Agents required
This probably seems to be the super cool thing about Ansible. "There is no need for running agents on remote machines to manage them."

So if there is no agent installed on the machine, how does the machine receive the tasks to be executed?
It seems like ansible's default communication is via SSH.

![ansible overview](/images/ansible-overview.png)

## No State
Ansible does not result in a state file like terraform. This means the same ansible script could be run from any machine and it will understand the state of things in the runtime.

Let me do a small experiment for this. I will try to bring up a GCP machine with ansible by using one fresh machine as control node and use the same YAML in another new control node. I did this experiment by running a [runSh](http://docs.shippable.com/platform/workflow/job/runsh/#runsh) on [Shippable](https://shippable.com) with two different nodes.

wow! Ansible understands the state correctly and results in creating the node only once eventhough I ran it twice on the provisioning scripts twice from two different control nodes.

How does ansible perform this magic?
I discovered this at a later point of time. It is by using "dynamic inventories". (will discuss about it down below)

## What it needs?
- Inventory (I guess this is a collection of information about the hosts)
- State Directives (I have no clue what this is)
- Credentials (Secret stuff used to talk to cloud providers and machines)

## Inventory
Inventory is collection of hosts (IP Addresses/Host names). Sometimes they are grouped together into named groups. (example: webservers, dbservers etc.)

```
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```

Multiple inventories are supported. I am probably thinking we can define as much inventory files as we like and choose one when we run ansible.

Inventory could also variables. These variables could be used while executing a task in ansible and for controlling the behaviour of ansible (Eg: ansible_user=test). Variables could be grouped inside the `inventory/group_vars` folder.

```
[webservers:vars]
type="web"
port="80"

[dbservers:vars]
type="db"
port="5432"

[all:vars]
global="available for all hosts"
```

It seems like there are two types of inventory sources.

- __Static source__, where information is maintained in files.
- __Dynamic source__, where information is fetched from cloud providers like AWS, Google Cloud Platform etc.

This is exciting. I didn't know about dynamic inventory sources before. I am going to spend sometime reading about it [here](http://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html).

So, the reason why my GCE instance did not get provisioned is earlier is due to this reason. I was using a dynamic inventory which contacted the google cloud platform for the existing infrastructure and updated in my machine.

I learnt how to use a dynamic inventories by looking at [a sample that we wrote at work](https://github.com/devops-recipes/prov_gcp_gce_ansible).

Various [strategies](http://docs.ansible.com/ansible/latest/user_guide/playbooks_strategies.html) for executing on multiple machines are present like Linear (Default), Serial, Free. Do check them out as they are interesting and could give you control over how ansible runs commands on your target machines.

## Tasks
- Task: written in YAML and defines work to be done on the target machine.
- Task Data: the data sent to target host for execution (Eg: Database name could be task data)
- Task Control: used to control the flow of tasks like looping tasks.
- Task Return Data: Data returned back as result of executing a task on host.
- Modules: Each task contains a module which performs some operation. Check [here](http://docs.ansible.com/ansible/latest/modules/modules_by_category.html) for in-built modules.

## Playbook
- Collection of plays in YML. Each play is a collection of tasks.
- Execute a playbook using `ansible-playbook` command.

```yml
- name: Playbook for printing stuff
  hosts: localhost

  tasks:
    - name: use debug module
      debug:
        msg: "print debug message here"

    - name: use fail module
      fail:
        msg: "print error message here"
```

## ansible-doc
ansible-doc utility installs with ansible. It is useful for getting help and reading about ansible modules.

```bash
$ ansible-doc debug
```

## Terraform vs Ansible
This is the part I have been waiting for. Here is my conclusion.

> Use terraform, if provisioning is the only need.
>
> Use Ansible, if you are trying to manage already provisioned nodes.
>
> When you want to provision + manage, go with any/both of them depending on your workflow.

So it is never Terraform vs Ansible, it is Terraform + Ansible. They could really agument each other and to attain this at an organisation level products like [Shippable](https://www.shippable.com/) could help.

## More
I guess there are lot more to explore and learn from. I will probably hint some topics for future exploration.

- Plugins Vs Modules
- [Roles](https://docs.ansible.com/ansible/2.5/user_guide/playbooks_reuse_roles.html)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Ansible tower](https://www.ansible.com/products/tower)
