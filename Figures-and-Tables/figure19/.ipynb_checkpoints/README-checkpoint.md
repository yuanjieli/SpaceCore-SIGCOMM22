## Figure 19: Leaked sensitive states in satellite attacks

<div align=center><img src="./figure19a.jpg" width=""></div>

<div align=center><img src="./figure19b.pdf" width=""></div>

### What is this figure about
Figure 19 shows the state leakages under satellite hijacking and man-in-the-middle passive listening of wireless inter-satellite links.
These figures are to illustrate the resiliency to satellite attacks of five solutions. 
Through comparison, we arrive at the following conclusions: SpaceCore is resilient to satellite hijacking due to its stateless nature. SpaceCore is also resilient to link failures and man-in-the-middle attacks since it localizes most state operations with few migrations.

### Experimental Methodology
Calculate state migration between satellites and state storage on satellites based on each solution's design philosophy and 3GPP specifications. The states  transmitted and stored by the satellites will be leaked as a result of satellite hijacking.The states transmitted by satellites will be  leaked if man-in-the-middle passive listening of wireless inter-satellite links occurs.

### How to run the code
```
jupyter notebook
Open figure19a.ipynb file and run notebook
Open figure19b.ipynb file and run notebook
```

### Data
The data can be found in the `data/` folder.

	|- data
		|-starlink
			|- distributed_old-new_SP_delay_hop.npy: This file shows the path between the old and new satellites during handover.
			|- distributed_old-end_SP_delay_hop.npy: This file shows the path between the old satellite and ground station.
			|- distributed_new-end_SP_delay_hop.npy
			|- starlink_ue_access_P_OPT.npy:This file shows the user's satellite access.
		|- starlink_per_user_ratio30000.npy: This file shows the real number of users represented by each user in starlink_ue_access_P_OPT.npy based on the satellite capacity.
		|- skycore_broadcast_SP_delay_hop: This file shows the states migration during broadcast of skycore.