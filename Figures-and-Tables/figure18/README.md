## Figure 18: SpaceCore’s local state processing costs

<div align=center><img src="./figure18.png" width=""></div>

### Overview
Figure 18 shows SpaceCore's  extra local state processing costs (delay). 
In combination with figure 17, even with the extra local state processing delay introduced by SpaceCore, the overall delay of SpaceCore is still much lower than other solutions. 

### Experimental Methodology

We follow Section 4.4 to implement SpaceCore's Home-Controlled State Updates using attribute-based encryption (ABE). We quantify its local state processing delay using the following setup:

+ Hardware: Raspberry Pi 4B. 
+ OS: Ubuntu 18.04.
+ Software: [OpenABE](https://github.com/zeutro/openabe).


### How to run the code
```
jupyter notebook
open figure18.ipynb file and run notebook
```

### Data
The following data files can be found in the `data/` subfolder:

	|- data
		|- abe-len-100.txt: Encryption and decryption time and encryption length with different number of attrbutes when ciphertext length is 100.


