

import re

def find_drug_pages(pattern,file_content):
    starts = [m.start() for m in re.finditer(pattern, file_content)]
    ends = [m.end() for m in re.finditer(pattern, file_content)]
    # retrieve [[*]]
    hyper_links = [file_content[start+2:end-2] for start,end in zip(starts,ends)]
    
    # |
    
    drug_items = []
    for item in hyper_links:
        inner_items = item.split("|")
        drug_items = drug_items + inner_items
    
    # space
    
    
    return drug_items
    

#read file
f = open("Wikipedia-20171013010045.xml")
list_of_drugs_pages = f.read()
#drug list
drug_pages_list = find_drug_pages("\[\[.*?\]\]",list_of_drugs_pages)

#print items
f_write = open("drug_page_titles",'w')

page_titles = ""

for page_title in drug_pages_list:
    page_titles = page_titles + page_title + "\n"
    
f_write.write(page_titles)

#export wikipedia pages
