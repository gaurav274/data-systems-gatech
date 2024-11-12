# Populate bib entries from dblp profile

## How to use this code

```bash
conda create -n dblp python=3.12 -y
conda activate dblp
pip install -r requirements.txt
# below will produce `prof_to_bib_entries.csv` file
python get_bib_file_from_dblp_profile.py
python gen_yml_entry_from_bib.py
```


## Venues

As of Oct 25, 2024

### List of all venues

```
{'SRDS', 'EEXTT', 'SIGCOMM', 'CLOUD', 'SC', 'JIM', 'ICLR', 'ICIP', 'TON', 'CIDR', 'ICMCS', 'ASUNAM', 'CACM', 'DPD', 'DKE', 'NETAISYS', 'JCSE', 'SODA', 'JSAC', 'AC', 'ACM', 'ACCESS', 'DMSN', 'AEI', 'MIDDLEWARE', 'CLOUD2', 'MEDINFO', 'HIPC', 'ICBO', 'COMPUTER', 'IGI', 'DEXAW', 'IJSEKE', 'SIGMETRICS', 'AMIA', 'JIIS', 'GLOBECOM', 'CIKM', 'ICMLA', 'POMACS', 'IS', 'DASFAA', 'VLDB', 'HASE', 'TCBB', 'DAGLIB', 'ICNP', 'AIS', 'CONEXT', 'DEBU', 'IPPS', 'TCOM', 'SP', 'IJHPCN', 'DB-WORKSHOPS', 'ISIT', 'CSUR', 'JSS', 'ICDCS', 'PACMMOD', 'INFSOF', 'IMW', 'JPDC', 'ACL', 'IAM', 'INFOCOM', 'BMSB', 'ITM', 'KDD', 'ACMSE', 'WECWIS', 'ISMIS', 'HPDC', 'ISCI', 'CN', 'ER', 'IJDMB', 'WEIS', 'PE', 'TCSV', 'IMC', 'CHI', 'HICSS', 'CSB', 'ISSTA', 'ACMICEC', 'USS', 'AISTATS', 'DEEM', 'TISSEC', 'JNSM', 'NETWORKS', 'TNSE', 'DL', 'MMSYS', 'COMPCON', 'JBI', 'COLCOM', 'GIR', 'BIGDATACONF', 'TPDS', 'TVT', 'ICSE', 'PODS', 'COMPSAC', 'ICWS', 'SNAM', 'ICDT', 'IWNAS', 'IVS', 'ICCCN', 'IEEESCC', 'IEEEVAST', 'TC', 'CSYS', 'UAI', 'CODES', 'DAMON', 'TWC', 'ANCS', 'PDIS', 'TSE', 'NPC', 'AID', 'SYNTHESIS', 'WSC', 'MARK2', 'UCC', 'CAD', 'TBC', 'JDM', 'TODS', 'ICML', 'TMC', 'NAR', 'NSF', 'INS', 'TKDE', 'JCDL', 'IDEAS', 'EMNLP', 'TOIT', 'ICDE', 'IWQOS', 'EDBT', 'CAISE', 'QUEUE', 'TNSM', 'VALUETOOLS', 'TKDD', 'IEEECLOUD', 'SIGMOD', 'RIDE', 'WH', 'AAAI', 'IJISCRAM', 'APIN', 'ICDCN', 'SSDBM', 'TVCG', 'NIPS', 'NETWORKING', 'ASPLOS', 'TOMPECS', 'ICDCSW', 'AVI', 'HPSR', 'CCS', 'IJCIS', 'CORR', 'MOBICOM', 'ETT', 'SIGECOM', 'FCSC'}
```

### Venues kept

Filtering was applied to the `gen_yml_entry_from_bib.py` file.

```
['ICLR', 'CIDR', 'CACM', 'ACM', 'CIKM', 'VLDB', 'KDD', 'AISTATS', 'DEEM', 'BIGDATACONF',  'ICML', 'TKDE', 'EMNLP', 'ICDE', 'TKDD', 'SIGMOD', 'AAAI', 'NIPS',]
```