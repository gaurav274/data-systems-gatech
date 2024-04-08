# Populate bib entries from dblp profile

## How to use this code

```bash
conda create -n dblp pytohn=3.12 -y
conda activate dblp
pip install -r requirements.txt
# below will produce `prof_to_bib_entries.csv` file
python get_bib_file_from_dblp_profile.py 
```