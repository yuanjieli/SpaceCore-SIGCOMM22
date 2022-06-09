# A Case for Stateless Mobile Core Network Functions in Space

This repository collects the artifacts of the SIGCOMM'22 paper "A Case for Stateless Mobile Core Network Functions in Space."

## Overview
Is it worth and feasible to push mobile core network functions to low-earth-orbit (LEO) satellite mega-constellations? While this paradigm is being tested in space and promises new values, it also raises scalability, performance, and security concerns based on our study with datasets from operational satellites and 5G. A major challenge is today’s stateful mobile core, which suffers from signaling storms in satellites’ extreme mobility, intermittent failures in outer space, and attacks when unavoidably exposed to untrusted foreign locations. In [1], we make a case for a stateless mobile core in space. Our solution, SpaceCore, decouples states from orbital core functions, simplifies location states via geospatial addressing, eliminates unnecessary state migrations in satellite mobility by shifting to geospatial service areas, and localizes state retrievals with device-as-the-repository. Our evaluation with datasets from operational satellites and 5G shows SpaceCore’s 17.5× signaling reductions and resiliency to failures/attacks compared to existing solutions.

<div align=center><img src="./SpaceCore-overview.png" width="100%"></div>


## Repository structure

This repository includes the following contents:

	|- SpaceCore-SIGCOMM22
		|- Dataset
			|-Satellite terminal data: signaling datasets from operational satellites.
			|-Mobileinsight dataset:
		|- Figures-and-Tables: Source files of figures and tables in [1]
			|-Figure5b
			|-Figure7
			|-Table2
			|-...
		|- sigcomm22.pdf: The SIGCOMM'22 paper.
		|- SpaceCore-overview.png: SpaceCore overview.
		|- README.md: This file.
	
	
## Dataset


We use two datasets for the empirical study and evaluation (in `SpaceCore-SIGCOMM22/Dataset/`):

- **Satellite terminal dataset**: The dataset is collected from three satellite termainals: China Telecom Tiantong SC310, China Telecom Tiantong 
T900 and Inmarsat BGAN Explorer 710 in 04/2021–1/2022.  
- **Mobileinsight dataset**: @yimei.

<table>
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

## Figures and Tables

In `SpaceCore-SIGCOMM22/Figures-and-Tables/`, we release the traces used in [1]'s figures and tables, including

- `Figure5b`: Measurement registration signaling latency in Tiantong SC310 and Inmarsat Explorer 710.
- `Figure7`: CPU usages by core network functions.
- `Figure8`: Signaling latency(Initial/Mobility registrations and Session establishments) in two hardware by satellites.
- `Figure9`: Signaling migration overhead of satellite and ground station in 4 constellations.
- `Figure12`: Temporal dynamics of a fast-moving LEO satellite’s signaling overhead in Option 3(Figure 6c).
- `Figure13`: Satellite failures in Starlink and radio link failures in Tiantong T900.
- `Figure17`: Singnaling delay and satellite CPU usage of initial registration, session establishment and mobility registration (by LEO satellite mobility). 
- `Figure18`: SpaceCore’s local state processing costs.
- `Figure19`: Leaked sensitive states in satellite attacks.
- `Figure20`: Signaling migration overhead per satellite and per ground station in five solutions.
- `Table2`: Overview of dataset from the experiments.
- `Table4`: SpaceCore’s satellite signaling cost reduction.

Each table/figure has a `README.md` in its corresponding folder that details the experimental methodology and how to run the code.

## Dependencies

To run all code in this repository, please use `python3 + jupyter notebook` and install the following packages:

```
pip3 install matplotlib numpy statsmodels pandas scipy seaborn
```

<!-- ## Raw dataset access
Due to excessive data volume, we do not intend to release all raw data here and put a sample in the dataset folder. If you want more data, please send a request to yuanjiel@tsinghua.edu.cn.

The request should include the work department, the purpose of data usage, and the data content obtained. -->

## Citation

Please indicate the source-link when using it and cite our SIGCOMM paper [1].

## Contact

Please contact yuanjiel@tsinghua.edu.cn for any questions or technical support.

## References

[1] Yuanjie Li, Hewu Li, Wei Liu, Lixin Liu, Yimei Chen, Jianping Wu, Qian Wu, Jun Liu, Zeqi Lai. A Case for Stateless Mobile Core Network Functions in Space. To appear at ACM SIGCOMM 2022.

