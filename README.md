# NA_mCNN: Classification of Sodium Transporters in Membrane Proteins:
This study focuses on the computational classification of sodium transporters from membrane proteins using a multi-window scanning CNN Model integrated with protein language model embeddings, ProtTRans. Sodium transporters play a critical role in various physiological processes, and their accurate identification is crucial for understanding human health and disease mechanisms, including their involvement in neurological disorders, cardiovascular diseases, and cancer.

## Fig. 1: Our Comprehensive Research Workflow:

![](https://github.com/Malik-glt/Unveiling-Therapeutic-Targets/blob/main/Model%20Work%20Flow.png?raw=true)

# Methodology 

We obtained sodium transporter and membrane protein data from Uniprot [1]. Specifically, sodium transporters found in plasma membranes were identified using the query described in the Supplementary Materials. This dataset contains 1,697 sodium transporter sequences and 13,111 membrane protein sequences . With Prottrans, a previously trained protein language model, we were able to extract complex features from protein sequences and fine-tune them based on our dataset. This method allowed for more accurate predictive modeling since it captured all encoded information within the sequences [2]. To provide a comprehensive analysis of protein sequences, we use convolutional neural networks (CNNs) along with a variety of window scanning methods. In this strategy, multiple window sizes were considered in order to evaluate sequence patterns in a comprehensive way. Figure 1 shows the complete architecture, while Figure 2 shows the classification model.

## Fig. 2: Multiple-window scanning deep learning networks

![](https://github.com/Malik-glt/Unveiling-Therapeutic-Targets/blob/main/Figure_MCNN.png?raw=true)

## References
1.	UniProt: the Universal Protein knowledgebase in 2023. Nucleic Acids Research, 2023. 51(D1): p. D523-D531.
2.	Elnaggar, A., et al., ProtTrans: Toward Understanding the Language of Life Through Self-Supervised Learning. IEEE Trans Pattern Anal Mach Intell, 2022. 44(10): p. 7112-7127.

cff-version: 1.2.0
message: "Please cite the following paper if you use this code:"
authors:
  - family-names: "Malik"
    given-names: "Muhammad Shahid"
  - family-names: "Ou"
    given-names: "Yu-Yen"
title: "Integrating Pre-Trained protein language model and multiple window scanning deep learning networks for accurate identification of secondary active transporters in membrane proteins"
journal: "Methods"
volume: "220"
pages: "11-20"
year: 2023
doi: "https://doi.org/10.1016/j.ymeth.2023.10.008"
url: "https://github.com/yourusername/your-repo"
