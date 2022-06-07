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
    <td>33,845</td>
    <td>1,178,327</td>
    <td>2,759,859</td>
    <td>3,828,083</td>
    <td>1,475,393</td>
    <td>8,405,587</td>
  </tr>
  <tr>
    <td>RRC<br></td>
    <td>4,484</td>
    <td>9,583</td>
    <td>3,020</td>
    <td>28,841</td>
    <td>14,833</td>
    <td>69,782</td>
  </tr>
  <tr>
    <td>MM</td>
    <td>57,264</td>
    <td>46,139</td>
    <td>13,556</td>
    <td>605</td>
    <td>970</td>
    <td>4,194</td>
  </tr>
  <tr>
    <td>SM</td>
    <td>48,458</td>
    <td>4,586</td>
    <td>1,670</td>
    <td>203</td>
    <td>338</td>
    <td>925</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>946,860</td>
    <td>2,311,663</td>
    <td>4,885,375</td>
    <td>3,857,732</td>
    <td>1,491,534</td>
    <td>8,480,488</td>
  </tr>
</tbody>
</table>

### What is this table about
This table shows our signaling datasets from operational satellites and terrestrial 5G.
### Reproduction steps with our data
1. jupyter notebook
2. Open table2.ipynb file and run notebook

### Data
The data can be found in the `data/` folder. Due to the volume of data and the protection of confidentiality of commercial terminals, these data are processed data. Each row of data represents only the layer or function in which it is located.

	|- data
		|- explore-710
			|- 1-8-2022
				|- 1.txt: 
			|- 1-14-2022
			|-...
		|- tiantong-sc310
			|-...
		|- tiantong-T900
			|-...


### Code annotation
We search for the following strings in the file to determine which layer the line is about.

+ L1/L2: `L1/L2`
+ RRC: `RRC layer` 
+ MM: `Mobility management` 
+ SM: `Session management`
