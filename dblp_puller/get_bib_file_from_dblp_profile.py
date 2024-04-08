import requests,re
import pandas as pd
import bibtexparser

def get_bib_file_from_dblp_profile(dblp_profile_url):
    # get the html content of the dblp profile
    response = requests.get(dblp_profile_url)
    bib_data = response.text
    # remove newline and extra spaces
    bib_data = re.sub(r'\n\s*', ' ', bib_data)
    return bib_data
    

# read csv with header
df = pd.read_csv("gt_professors_dblp.csv",sep="|")

# print professors with no dblp bib file i.e. NaN
print("Professors with no dblp bib file")
print(df[df["DBLP_BibTeX_URL"].isnull()])
# remove professors with no dblp bib file
df = df.dropna(subset=["DBLP_BibTeX_URL"])

prof_to_bib_entries = {}

def filter_bib_entries(bib_entries):
    # check if entries have following keys if not raise an error
    mandatory_keys = ["author", "title", "year", "url"]
    filtered_entries = []
    filtered_entry = {}
    # for each entry in bib_entries check if it has all the keys
    for entry in bib_entries:
        mandatory_key_not_found = False
        for mandatory_key in mandatory_keys:
            entry_keys = set(key for key,_ in entry.items())
            if mandatory_key not in entry_keys:
                mandatory_key_not_found = True
                # if even a single key is not found then skip the entry
                continue
        if mandatory_key_not_found:
            continue
        # add a key called venue_tag
        filtered_entry["venue_tag"] = entry.key.split("/")[1].upper()
        # replace '/' in entry.key with '-'
        filtered_entry["key"] = entry.key.replace("/", "-")
        # replace "and" in author with ','
        filtered_entry["author"] = entry["author"].replace(" and ", ",")
        filtered_entry["title"] = entry["title"]
        filtered_entry["year"] = entry["year"]
        filtered_entry["url"] = entry["url"]
        # add the entry to the filtered_entries
        filtered_entries.append(filtered_entry.copy())
    return filtered_entries


# loop through the professors and get the bib file
for index, row in df.iterrows():
    try:
        dblp_profile_url = row["DBLP_BibTeX_URL"]
        bib_data = get_bib_file_from_dblp_profile(dblp_profile_url)
        bib_entries = bibtexparser.parse_string(bib_data).entries
        bib_entries = filter_bib_entries(bib_entries)
        print(f"Processed bib entries for {row['Professor']} successfully")
        prof_to_bib_entries[row["Professor"]] = bib_entries
    except Exception as e:
        print(f"Error processing bib entries for {row['Professor']}")
        print(e)
# convert prof_to_bib_entries to a pandas dataframe
prof_to_bib_entries_df = pd.DataFrame(prof_to_bib_entries.items(), columns=["Professor", "BibEntries"])

# save prof_to_bib_entries_df to a csv file
prof_to_bib_entries_df.to_csv("prof_to_bib_entries.csv", index=False)