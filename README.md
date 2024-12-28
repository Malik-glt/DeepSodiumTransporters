# NA_mCNN: Classification of Sodium Transporters in Membrane Proteins:
This study focuses on the computational classification of sodium transporters from membrane proteins using a multi-window scanning CNN Model integrated with protein language model embeddings, ProtTRans. Sodium transporters play a critical role in various physiological processes, and their accurate identification is crucial for understanding human health and disease mechanisms, including their involvement in neurological disorders, cardiovascular diseases, and cancer.

## Fig. 1: Our Comprehensive Research Workflow:

![]([Figure_Archtectural_1.png](https://github.com/Malik-glt/DeepSodiumTransporters/blob/main/Figure_Archtectural_1.png))

# Methodology 

We obtained sodium transporter and membrane protein data from Uniprot [1]. Specifically, sodium transporters found in plasma membranes were identified using the query described in the Supplementary Materials. This dataset contains 1,697 sodium transporter sequences and 13,111 membrane protein sequences . With Prottrans, a previously trained protein language model, we were able to extract complex features from protein sequences and fine-tune them based on our dataset. This method allowed for more accurate predictive modeling since it captured all encoded information within the sequences [2]. To provide a comprehensive analysis of protein sequences, we use convolutional neural networks (CNNs) along with a variety of window scanning methods. In this strategy, multiple window sizes were considered in order to evaluate sequence patterns in a comprehensive way. Figure 1 shows the complete architecture of the study.

## Quick Start

### Step 1: Generate Data Features
Navigate to the 'data' folder and use the FASTA file to generate additional data features that are saved in the 'dataset' folder..

**Example usage:**

```bash
python get_ProtTrans.py -in "Your FASTA file folder" -out "The destination folder of your output"
python get_tape.py -in "Your FASTA file folder" -out "The destination folder of your output"
python get_esm.py "Pretrained model of ESM" "Your FASTA file folder" "The destination folder of your output" --repr_layers 33 --include per_tok
```
### Step 2: Generate Dataset Using Data Features
1. **Run `length_change.ipynb`:**
   - Open the `length_change.ipynb` file and specify the following:
     - The proper paths for the training and testing datasets.
     - The feature type: use `'pt'` for ProtTrans, `'esm'` for ESM, and `'tape'` for TAPE.
     - Set the desired sequence length for the study.

2. **Run `Concatenate.ipynb`:**
   - Execute the `Concatenate.ipynb` file to concatenate all protein sequences. This step will produce the following output files:
     - `train_data.npy`: Contains the training data.
     - `train_labels.npy`: Contains the corresponding training labels.
     - `testing_data.npy`: Contains the testing data.
     - `testing_labels.npy`: Contains the corresponding testing labels.
    
### Step 3: Execute Prediction
1. **Navigate to the code folder:**
   - Change your directory to the `code` folder where the prediction model is located.

2. **Run the Model:**
   - Open the `mCNN_Sodium.ipynb` file in Jupyter Notebook.
   - Execute the cells in the notebook to run the model and make predictions based on your dataset.

## References
1.	UniProt: the Universal Protein knowledgebase in 2023. Nucleic Acids Research, 2023. 51(D1): p. D523-D531.
2.	Elnaggar, A., et al., ProtTrans: Toward Understanding the Language of Life Through Self-Supervised Learning. IEEE Trans Pattern Anal Mach Intell, 2022. 44(10): p. 7112-7127.



