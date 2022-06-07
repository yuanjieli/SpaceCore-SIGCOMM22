## Figure 9: Signaling migration overhead of satellite and ground station in four constellations.

<div align=center><img src="./figure9.jpg" width=""></div>

### What is this figure about
Figure 9 shows signaling migration overhead of satellite and ground station in four constellations.
This figure is to compare orbital cores in Figure 6 in LEO mega-constellations.
All options in Figure 6 suffer from exhaustive signaling storms. For different options in Figure 6, cause of signaling storms vary. 

### Experimental Methodology
Our research is based on LEO mega-mega-constellations, so that we emulate signaling migration overhead during mobility management and session setup in current LEO mega-mega-constellations.
3GPP has developed the most widely used 5G standard, so we analyze signaling interactions between entities in 5G refer to 3GPP specifications. What‘s more，We refer to the signaling migration in real trace collected by MobileInsight.

### How to run the code
```
jupyter notebook
Open figure9.ipynb file and run notebook
```

### Data
The data can be found in the `data/` folder.

	|- data
		|- gsl_mobility_signaling.npy:This file shows signaling migration overhead during mobility management in ground station-satellite-link.
		|- gsl_session_signaling.npy:This file shows signaling migration overhead during session setup in ground station-satellite-link.
		|- starlink_72_22
			|- opt_handover
				|- satellite
					|- distributedscenario_a_2000_mobility.npy：This file shows signaling migration overhead in scanario a with capacity of 2000 during mobility management. Shape of this file is (99, 1584, 2), which contains byte migration overhead and signaling migration overhead during 99 sets of time slice switching, on 1584 satellites.
					|- distributedscenario_a_2000_session.npy
					...
		|- kuiper
			|- opt_handover
				|- satellite
					|- distributedscenario_a_2000.npy
					...
		...

