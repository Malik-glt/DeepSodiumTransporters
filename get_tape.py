import os
import torch
from tape import ProteinBertModel, TAPETokenizer
from tqdm import tqdm
import numpy as np
import glob
import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-in", "--path_input", type=str, help="The path of input fasta file")
parser.add_argument("-out", "--path_output", type=str, help="The path of output esm file")

def main(input_folder, out_folder, miss_txt):
    input_files = glob.glob(input_folder + "/*")
    out_folder = out_folder
    miss_txt = miss_txt
    
    model = ProteinBertModel.from_pretrained('bert-base')
    tokenizer = TAPETokenizer(vocab='iupac')  # 'iupac' for TAPE models, 'unirep' for the UniRep model
    target_length = 1000  # Fixed length for all sequences

    for path in tqdm(input_files, desc="Processing", unit="file"):
        with open(path) as f:
            fasta = f.readlines()
        title = fasta[0][1:].strip()
        sequence = fasta[1].strip()
        out_path = os.path.join(out_folder, title)

        # Skip sequences longer than the target length
        if len(sequence) > target_length:
            continue

        try:
            # Tokenize the sequence
            token_ids = torch.tensor([tokenizer.encode(sequence)])

            # Get the model output
            output = model(token_ids)
            sequence_output = output[0][:, 1:-1, :].cpu().detach().numpy()

            # Pad the sequence output to the target length
            if sequence_output.shape[1] < target_length:
                padding_length = target_length - sequence_output.shape[1]
                sequence_output = np.pad(sequence_output, ((0, 0), (0, padding_length), (0, 0)), mode='constant', constant_values=0)
            
            # Save the output
            np.save(out_path + ".npy", sequence_output)
        
        except Exception as e:
            log_mode = 'a' if os.path.exists(miss_txt) else 'w'
            with open(miss_txt, log_mode) as tape_miss:
                tape_miss.write(title + ".fasta\n")
            print(f"Error processing {title}: {e}")
            continue

if __name__ == "__main__":
    args = parser.parse_args()
    main(args.path_input, args.path_output, "tape_miss")