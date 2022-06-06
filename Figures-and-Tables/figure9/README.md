### What is this figure about

Figure 9 shows signaling migration overhead of satellite and ground station in four constellations.

This figure is to compare orbital cores in Figure 6 in LEO mega-constellations.

All options in Figure 6 suffer from exhaustive signaling storms. For different options in Figure 6, cause of signaling storms vary. 

### Reproduction steps with our data

1.    jupyter notebook
2.   Open figure9.ipynb file and run notebook

### Reproduction steps without our data

stk data—handover —signaling migration（llx）

session（MI data ）—signaling interaction—signaling migration

### Why we do it like this

+ Experimental Methodology
  + Our research is based on LEO mega-mega-constellations, so that we emulate signaling migration overhead in existing LEO mega-mega-constellations.

+ Data Processing
 	+ 3GPP has developed the most widely used 5G standard, so we analyze signaling interactions between entities in 5G refer to 3GPP specifications.
 	+ We refer to the signaling migration in real trace collected by MobileInsight. 

### Data
The data can be found in the `data/` folder.


	|- data
		|- pairs.npy:Describe the pairing relationship between UE and GS.
		|- starlink_72_22
			|- opt_handover
				|- satellite
					|- distributedscenario_a_2000.npy
					|- distributedscenario_a_2000.npy
			|- distributed_new-end_SP_delay_hop.npy:llx
		|- kuiper
			|- opt_handover
				|- satellite
					|- distributedscenario_a_2000.npy
			|- distributed_new-end_SP_delay_hop.npy
			

