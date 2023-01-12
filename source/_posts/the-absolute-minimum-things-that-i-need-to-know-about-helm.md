---
title: The absolute minimum things that I need to know about Helm
date: 2023-01-13 01:27:30
tags: ["helm","kubernetes"]
---

I am learning about [helm](https://helm.sh/). It is a package manager for Kubernetes.

This documentation page provided me a good starting point: https://helm.sh/docs/topics/architecture/ and then I roamed around the docs gathering the below notes.

The latest helm version as of writing this notes is `v3.10.3`.

(If something is wrong, feel free to suggest a fix as a pull request [here](https://github.com/scriptnull/vishnubharathi.codes))

- basics
	- chart - kubernetes yaml definitions to run the app  
	- repository - collection of charts  
	- release - running instance of a chart. Two releases of same chart could be running at the same time in a kubernetes cluster (example: two redis instances used by different services)  
- helm repo add <name> <url>  
  - add a repo to use the charts inside it.
- helm repo update  
	- updates the list of charts available in the added repositories  
- versioning  
	- a chart seem to contain two versions  
		- chart version  
		- application version  
	- example: vault's chart and app versions  
	    
	  > NAME           	CHART VERSION	APP VERSION	DESCRIPTION  
	  hashicorp/vault	0.23.0       	1.12.1     	Official HashiCorp Vault Chart  

- helm search hub <query>  
	- searches for charts in artifact hub  
- helm search repo <query>  
	- searches for charts in locally added repositories  
- helm install <release_name> <chart>  
	- You can also use `helm install <chart> --generate-name` if you wish to generate a release name automatically (example: `redis-TIMESTAMP`)  
	- the order in which the kubernetes resources mentioned in the chart are installed is document at https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package  
	-  
	  > Helm does not wait until all of the resources are running before it exits. Many charts require Docker images that are over 600M in size, and may take a long time to install into the cluster.  

	- Use `helm status` to get the state of the install  
- helm show values <chart>  
	- You can customize the values that are configured in a chart before deploying a release  
	- This command will help you understand what values are available in a chart that could be modified  
- helm install -f values.yaml <release_name> <chart>  
	- the vaules in `values.yaml` file will override the config values  
- Other methods of installing charts  
	- A chart repository  
	- A local chart archive (`helm install foo foo-0.1.1.tgz`)  
	- An unpacked chart directory (`helm install foo path/to/foo`)  
	- A full URL (`helm install foo https://example.com/charts/foo-1.2.3.tgz`)  
- helm upgrade <release_name> <chart>  
	- > When a new version of a chart is released, or when you want to change the configuration of your release, you can use the helm upgrade command.  

- helm get values <release_name>  
	- Useful in getting the values used in a release  
- helm rollback <release_name> <revision>  
	- > The above rolls back our happy-panda to its very first release version. A release version is an incremental revision. Every time an install, upgrade, or rollback happens, the revision number is incremented by 1. The first revision number is always 1.  

- helm list  
	- Lists all the releases  
- helm history <release_name>  
	- Lists all the revisions for a release  
	- You can then use `helm get values <release_name> --revision NUMBER` to get the values used in a particular revision  
- Helpful options during install/upgrade/rollback  
	- --timeout  
		- A [Go duration](https://golang.org/pkg/time/#ParseDuration) value to wait for Kubernetes commands to complete. This defaults to `5m0s`.  
	- `--wait`: Waits until all Pods are in a ready state, PVCs are bound, Deployments have minimum (`Desired` minus `maxUnavailable`) Pods in ready state and Services have an IP address (and Ingress if a `LoadBalancer`) before marking the release as successful. It will wait for as long as the `--timeout` value. If timeout is reached, the release will be marked as `FAILED`  
- helm uninstall <release_name>  
	- use `--keep-history` if you wish to the uninstalled release to show up in `helm list --all`  
- helm create <name>  
	- for creating a new chart  
- helm package <folder_name>  
	- should output a `*.tgz` file (known as chart archive, I guess)  
