## Table 2: Overview of dataset from our experiments

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

### Overview
This table shows the statistics of our signaling datasets from operational satellites and terrestrial 5G.

### Experimental methodology
We classify the data collected from mobile satellites and terrestrial 5G into the layers in the table according to the standards.

### How to run the code
```
jupyter notebook
Open table2.ipynb file and run notebook
```

### Data
The data can be found in the `data/` folder. Due to the volume of data and the protection of confidentiality of commercial terminals, these data are processed data. Each row represents the layer where the original data is located.

	|- data
		|- explore-710
			|- 1-8-2022
			|- 1-14-2022
			|-...
		|- tiantong-sc310
			|-...
		|- tiantong-T900
			|-...


