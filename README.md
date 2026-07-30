🧬 A lightweight Python tool for rapid screening and visualization of probiotic genomic features (GC content & genome length) based on NCBI assembly data.

## 🎯 Background & Motivation
This project is inspired by the large-scale genomic studies conducted by **Dr. Zou Yuanqiang's group** (e.g., the 3,300 probiotic genome dataset published in 2026). 
It aims to demonstrate a basic but complete bioinformatics pipeline: **Data Retrieval → Sequence Parsing → Feature Extraction → Statistical Visualization**.

## ⚙️ Features
- ✅ Parse multi-sequence FASTA/`.fna` files using `Biopython`.
- ✅ Automatically calculate **Genome Length** and **GC Content** for each strain.
- ✅ Export structured analysis results to `screening_results.csv`.
- ✅ Generate high-quality scatter plots via `Matplotlib` and `Seaborn`.

## 📊 Visualization Results
**Figure 1:** Scatter plot showing the distribution of GC content and genome length across multiple *Bifidobacterium* strains.

## 🛠️ How to Use
1. Clone the repository:
   ```bash
   git clone [这里填您的GitHub链接]

2. Install dependencies:
pip install biopython pandas matplotlib seaborn

3. Prepare your data:
Place your .fna (or .fasta) genome files in the project folder, and edit the fasta_file variable in gene_screener.py to point to your file name.

4. Run the script:
python gene_screener.py

📂 File Structure
gene_screener.py - Main analysis script

demo_seq.fna - Sample genomic data (FASTA format)

screening_results.csv - Output table

candidate_genes_distribution.png - Output visualization
