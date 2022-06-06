## Figure 7: CPU usages by core network functions

<div align=center><img src="./figure7a.pdf" width=""></div>
<div align=center><img src="./figure7b.pdf" width=""></div>

### What is this figure about
This figure shows massive signalling procedures will exhaust satellite hardware. We initiate procedures with varying number of users to evaluate 5G core(Open5GS) cost.
This exposes one of the drawbacks of all the functions deployed on the satellite.

In addition, we can also get the CPU utilization of each 5G core function.
This has implications for the deployment of lightweight core networks on satellites.

### Experimental Methodology

We use two real LEO hardware to run a lightweight 5G core network, Open5GS, to illustrate the consumption of CPU resources by the signaling process. Even for a lightweight core network, the CPU consumption is still very heavy.

Here are the details of this experiment:

+ Hardware: (1) Raspberry Pi 4 used by Baoyun 5G LEO satellite and; (2)
Precision 7920 Workstation with Xeon E5-2630 (20 cores, 2.2GHz), which is  similar to (weaker than) Hewlett Packard Enterprise EL 8000s (24 cores, 2.4GHz) used by OrbitsEdge in satellites.
+ OS: Ubuntu 18.04.
+ Software: [Open5GS](https://open5gs.org) and [UERANSIM](https://github.com/aligungr/UERANSIM).
+ Reproduction steps:
	1. Deploy all functions of Open5GS on hardware 1/2, and deploy UERANSIM on any hardware (different from the hardware where Open5GS is located).
	2. Establish connections between Open5GS and UERANSIM. The tutorial is available in the [main README.md](../../README.md).
	3. Write scripts to insert users in batches and trigger registration signaling processes.
	4. Use linux `top` command to monitor cpu utilization of each core function.
	5. Processing data, calculating the cpu utilization of each function with varying number of users.


### How to run the code
```
jupyter notebook
open figure7.ipynb file and run notebook
```

### Data
The following data files can be found in the `data/` subfolder:

	|- data
		|- raspberry-pi: CPU utilization of open5gs core functions using linux `top` command with Raspberry pi 4B. 
			|- 10.txt: The file name `xxx.txt` indicates `xxx` registration requests sent per second.
			|- 50.txt
			|-...
		|- work-station: CPU utilization of open5gs core functions using linux `top` command with Precision 7920 Workstation with Xeon E5-2630(20 cores, 2.2GHz). 
