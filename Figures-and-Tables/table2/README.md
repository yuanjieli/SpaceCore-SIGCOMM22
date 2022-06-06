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
