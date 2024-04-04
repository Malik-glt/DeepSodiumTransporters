# Unveiling Therapeutic Targets:
This study investigates sodium secondary active transporters' crucial role in disease intervention. Using advanced predictive modeling techniques and pre-trained language models, we identify potential therapeutic targets, accelerating drug discovery and improving treatment strategies for conditions like diabetes and cardiovascular diseases.
## Fig. 1: Our Comprehensive Research Workflow:
![](https://github.com/Malik-glt/Unveiling-Therapeutic-Targets/blob/309a2ff75773d76a869c8aa238f08e49c4f8e5ad/sodium%20Architecture.PNG)
# Mehodology
The dataset is based on two sources. We used the Universal Protein (UniProt) database to retrieve the first set of secondary active transporters, including sodium transporters [1]. In the second part of the study, data were collected from the Transporter Classification Database (TCDB), which is based on Pizzagalli et al. [2]. With Prottrans, a previously trained protein language model, we were able to extract complex features from protein sequences and fine-tune them based on our dataset. This method allowed for more accurate predictive modeling since it captured all encoded information within the sequences. To provide a comprehensive analysis of protein sequences, we use convolutional neural networks (CNNs) along with a variety of window scanning methods. In this strategy, multiple window sizes were considered in order to evaluate sequence patterns in a comprehensive way. Figure 1 shows the complete architecture, while Figure 2 shows the classification model.
## Fig. 2: Multiple-window scanning deep learning networks
![](Model (2).png)
