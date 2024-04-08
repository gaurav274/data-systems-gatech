import pandas as pd
import re
# read the csv file
df = pd.read_csv('prof_to_bib_entries.csv')

def write_to_file(name, bibentry: dict):
    year = bibentry['year']
    key = bibentry['key'].split("DBLP:")[1]
    pub_type = key.split("-")[0]
    if pub_type == 'journals':
        pub_type = 'Journal'
    elif pub_type == 'conf':
        pub_type = 'Conference'
    elif pub_type == 'phd':
        pub_type = 'Thesis'
    elif pub_type == 'books':
        pub_type = 'Book'
    elif pub_type == 'series':
        pub_type = 'Series'
    
    pdf = bibentry['url']
    title = bibentry['title']
    venue_tag = bibentry['venue_tag']
    venue = venue_tag
    ignore = ["2000-journals-tkde-LiuPT00",
        "2009-journals-kais-ChenL09",
        "2012-conf-colcom-FanLLS12",
        "2012-journals-monet-JoshiBPR12",
        "2013-conf-asunam-TamersoyXLRCN13",
        "2015-conf-sigmod-ArulrajPD15",
        "2017-conf-uic-FerreiraVOP17",
        "2018-journals-tsc-ZhangYPA18",
        "2019-journals-jsjkx-ZhangLW19",
        "2023-journals-toit-SrivastavaLPZ23"]
    # if f"{year}-{key}" in ignore:
    #     return
    
    if "CORR" in venue:
        return
    
    if "Editor's Notes" in title:
        return

    # remove the special characters from the title that are not allowed in yaml strings
    def remove_special_characters(text):
        # Define a regex pattern to match special characters not allowed in YAML strings
        pattern = r'[^\w\s\-.,:;!?%&()\'"<>#@$*+=|\\\/]'
        # Replace matched characters with an empty string
        clean_text = re.sub(pattern, '', text)
        
        # remove extra quotes from the title
        clean_text = clean_text.replace('"', '')
        # remove backslash from the title
        clean_text = clean_text.replace('\\', '')
        
        return clean_text
    
    title = remove_special_characters(title)    
    
    
    f = open(f'ymls_generated/{year}-{key}.html', 'a')
    f.write(f'---\n')
    f.write(f'layout: publication\n')
    # write the year
    f.write(f'year: {year}\n')
    # write the title
    f.write(f'title: "{title}"\n')
    # write the authors
    f.write(f'authors:\n')
    for author in bibentry['author'].split(','):
        f.write(f'  - {author}\n')
    # write the venue_tag
    f.write(f'venue_tags:\n')
    f.write(f'  - {venue_tag}\n')
    f.write(f'venue: {venue}\n')
    # write the type of publication
    f.write(f'type:\n')
    f.write(f'  - {pub_type}\n')
    # write the pdf
    f.write(f'pdf: {pdf}\n')
    f.write(f'---\n')
    f.close()
        
# for each row in the csv file
for _, row in df.iterrows():
    # get the name of the professor
    prof_name = row['Professor']
    bibentries = row['BibEntries']
    # read the bibentries as a list
    bibentries = eval(bibentries)
    
    print(f'Processing {prof_name}...')
    # unique pub_types for each professor
    pub_types = set(bibentry['key'].split("-")[0] for bibentry in bibentries)
    print(f'Unique pub_types for {prof_name}: {pub_types}')
    # for each bibentry in the list
    for bibentry in bibentries:      
        write_to_file(prof_name, bibentry)