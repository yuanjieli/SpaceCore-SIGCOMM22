## Figure 19:  Signaling migration overhead per satellite and per ground station in five solutions.

<div align=center><img src="./figure20.pdf" width=""></div>


### What is this figure about

Figure 20 shows signaling migration overhead without failures/attacks.
This figure is to compare  SpaceCore with four satellite solutions in LEO mega-constellations.
SpaceCore significantly reduces signaling overhead compared to the other four solutions. It reduces 122.2×, 17.5×, 40.3×, and 49.3×signaling costs for satellites compared to 5G NTN, SkyCore, Baoyun, and DPCM, respectively in Starlink where capability of satellite is 30,000 users. 

### Experimental Methodology

Our research is based on LEO mega-mega-constellations, so that we emulate signaling migration overhead in existing LEO mega-mega-constellations.

The overhead of signaling migration is related to the service capacity of a single satellite, so we examine the signaling overhead at different satellite service capacities

We analyze signaling interactions between entities in 5G refer to solution-specific signaling simplification principles.

### How to run the code

1.    jupyter notebook
2.    Open figure20.ipynb file and run notebook


### Data
The data can be found in the `data/` folder.


	|- data
		|- starlink_72_22
			|- opt_handover
				|- satellite
					|- distributed_solution_DPCM_state_2000_mobility.npy：This file shows signaling migration overhead in solution DPCM with capacity of 2000 during mobility management. Shape of this file is (99, 1584, 2), which contains byte migration overhead and signaling migration overhead during 99 sets of time slice switching, on 1584 satellites.
					|- distributed_solution_DPCM_state_2000_session.npy
					...
			|- distributed_new-end_SP_delay_hop.npy:llx
		|- kuiper
			|- opt_handover
				|- satellite
					|- distributed_solution_DPCM_state_2000_mobility.npy.npy
					...
			|- distributed_new-end_SP_delay_hop.npy
		...