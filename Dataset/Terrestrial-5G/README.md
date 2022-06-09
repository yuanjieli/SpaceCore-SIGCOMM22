# Dataset

This folder includes the data used for the empirical study and evaluation in [1].
We collect over-the-air signaling messages between operational geostationary satellites and three terrestrial satellite terminals: 

- Inmarsat Explorer 710 satellite terminal (based on 3G UMTS)
- China Telecom’s Tiantong SC310 satellite terminal (based on 2G GMR)
- China Telecom’s Tiantong T900 satellite phone (based on 2G GMR). 

For each device, we enable the diagnostic mode for its satellite baseband, and collect signaling messages of radio resource control (RRC), mobility management (MM), and session management (SM) protocols. 

We also collect over-the-air 5G signaling messages from China Unicom, China Mobile, and China Telecom with Xiaomi 10/11 and OnePlus 9 running [MobileInsight](https://www.mobileinsight.net) with our extensions support these signaling message collections.

Due to excessive data volume, this folder includes a small representative set of examples for these datasets. The complete raw satellite/5G datasets used in [1] are available at [this Dropbox repository](https://www.dropbox.com/sh/3yzhcc5hx9bi8fu/AABJJ2cEn0kZdI-E-TmCzhUGa?dl=0).

## References

[1] Yuanjie Li, Hewu Li, Wei Liu, Lixin Liu, Yimei Chen, Jianping Wu, Qian Wu, Jun Liu, Zeqi Lai. A Case for Stateless Mobile Core Network Functions in Space. To appear at ACM SIGCOMM 2022.

