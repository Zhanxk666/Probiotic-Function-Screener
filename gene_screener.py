# gene_screener.py
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input file path
fasta_file = "demo_seq.fna" 

data = []
print(f"Reading file: {fasta_file}, please wait...")

try:
    # Read FASTA with UTF-8 encoding
    with open(fasta_file, 'r', encoding='utf-8') as handle:
        records = list(SeqIO.parse(handle, "fasta"))
except UnicodeDecodeError:
    # Fallback to system default encoding
    print("UTF-8 decoding failed, trying system default encoding...")
    with open(fasta_file, 'r') as handle:
        records = list(SeqIO.parse(handle, "fasta"))

print(f"Successfully loaded {len(records)} sequences. Starting analysis...")

for rec in records:
    seq = str(rec.seq)
    length = len(seq)
    gc_count = seq.count('G') + seq.count('C')
    gc_content = (gc_count / length) * 100 if length > 0 else 0
    
    # Extract features
    data.append({
        "ID": rec.id,
        "Length": length,
        "GC_Content": round(gc_content, 2),
        "Description": rec.description
    })

# Export results as CSV
df = pd.DataFrame(data)
csv_path = "screening_results.csv"
df.to_csv(csv_path, index=False)
print(f"Analysis complete. Results saved to {csv_path}.")

# Generate visualization
if len(data) > 0:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Length', y='GC_Content', s=100)
    plt.title("Candidate Functional Genes: Length vs GC Content Distribution")
    plt.xlabel("Sequence Length (bp)")
    plt.ylabel("GC Content (%)")

    plot_path = "candidate_genes_distribution.png"
    plt.savefig(plot_path, dpi=300)
    print(f"Visualization saved to {plot_path}.")
else:
    print("No valid sequences found. Please check your .fna file.")
