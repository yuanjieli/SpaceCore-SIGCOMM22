## Figure 9: Signaling migration overhead of satellite and ground station in four constellations.

<div align=center><img src="./figure9.jpg" width=""></div>

### Overview
Figure 9 shows signaling migration overhead of satellite and ground station in four constellations.

This figure is to compare orbital cores in Figure 6 in LEO mega-constellations. Each LEO satellite must process $10^4$∼$10^5$ signaling messages/s (depending on satellite capacity, location, and constellations). This cost is worsened at the ground stations by one order of magnitude due to space-terrestrial asymmetry (except for Option 4). Without mobility functions in satellites (Figure 6a–6b), signaling storms arise from the stateful session establishment.

### Experimental Methodology
We analyze four options of orbital core from 3GPP standards and 5G satellites by progressively adding radio, session, mobility, and security functions to satellites (Figure 6). 

<div align=center><img src="./figure6.png" width="500"></div>

Rather than spread these functions to multiple satellites, we focus on consolidating them to each satellite that is coherent with today’s 5G satellites to save signaling costs.  We run what-if studies for each option by replaying datasets from terrestrial 5G (Table 2, collected by MobileInsight) and global mobile subscriptions in ground stations in [1] as home network and LEO mega-constellations in Table 1 using grid topology [2,3].

<table>
    <caption> Table 1: LEO satellite mega-constellations today </caption>
    <thread>
    <tr>
        <th></th>
        <th>Satellites per orbit 𝑛</th>
        <th>Total orbits 𝑚</th>
        <th>Total satellites 𝑛 · 𝑚</th>
        <th>Altitude 𝐻 (km)</th>
        <th>Inclination angle 𝜙</th>
        <th>Speed</td>
    </tr>
    </thread>
    <tbody>
    <tr>
        <td>Starlink</td>
        <td>22</td>
        <td>72</td>
        <td>1,584</td>
        <td>550</td>
        <td>53°</td>
        <td>7.6km/s</td>
    </tr>
    <tr>
        <td>OneWeb</td>
        <td>40</td>
        <td>18</td>
        <td>720</td>
        <td>1,200</td>
        <td>87.9°</td>
        <td>7.3km/s</td>
    </tr>
    <tr>
        <td>Kuiper</td>
        <td>34</td>
        <td>34</td>
        <td>1,156</td>
        <td>630</td>
        <td>51.9°</td>
        <td>7.5km/s</td>
    </tr>
    <tr>
        <td>Iridium</td>
        <td>11</td>
        <td>6</td>
        <td>66</td>
        <td>780</td>
        <td>86.4° </td>
        <td>7.4km/s</td>
    </tr>
    </tbody>
</table>

<table>
    <caption> Table 2: Overview of dataset from our experiments </caption>
<thead>
  <tr>
    <th></th>
    <th colspan="3"> Mobile satellites</th>
    <th colspan="3"> Terrestrial 5G</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td>Inmarsat Explorer 710</td>
    <td>Tiantong SC310</td>
    <td>Tiantong T900</td>
    <td>China Telecom</td>
    <td>China Unicom</td>
    <td>China Mobile</td>
  </tr>
  <tr>
    <td>L1/L2</td>
    <td>56,231</td>
    <td>1,744,094</td>
    <td>3,887,429</td>
    <td>3,828,083</td>
    <td>1,475,393</td>
    <td>8,405,587</td>
  </tr>
  <tr>
    <td>RRC<br></td>
    <td>40,800</td>
    <td>4,226</td>
    <td>1,340</td>
    <td>28,841</td>
    <td>14,833</td>
    <td>69,782</td>
  </tr>
  <tr>
    <td>MM</td>
    <td>57,264</td>
    <td>43,555</td>
    <td>12,626</td>
    <td>605</td>
    <td>970</td>
    <td>4,194</td>
  </tr>
  <tr>
    <td>SM</td>
    <td>53,868</td>
    <td>4,586</td>
    <td>1,670</td>
    <td>203</td>
    <td>338</td>
    <td>925</td>
  </tr>
   <tr>
    <td>Others</td>
    <td>762,957</td>
    <td>310,455</td>
    <td>376,671</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>Total</td>
    <td> 971,120 </td>
    <td>2,106,916</td>
    <td>4,279,736</td>
    <td>3,857,732</td>
    <td>1,491,534</td>
    <td>8,480,488</td>
  </tr>
</tbody>
</table>

### How to run the code

1. jupyter notebook
2. Open figure9.ipynb file and run notebook


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

### References

[1] Tesmanian. SpaceX Starlink Gateway Stations Found In The United States and Abroad. https://tinyurl.com/4m5uah43, 2021.

[2] Sydney Finkelstein and Shade H Sanford. Learning from corporate mistakes: The rise and fall of iridium. Organizational Dynamics, 29(2):138–148, 2000.

[3] Debopam Bhattacherjee and Ankit Singla. Network Topology Design at 27,000 km/hour. In ACM CoNEXT, 2019.

