from datetime import datetime
import os
import re

import numpy as np
import pandas
import requests

ocrid = "0000-0002-0036-2752"
# lower case for possible names that need to be standardized
possible_names = [
    "henry leung",
    "henry w. leung",
    "henry w leung",
    "w. henry leung",
    "w henry leung",
    "w. h. leung",
    "h. w. leung",
    "h w leung",
]
standardized_names = "Henry W. Leung"
ads_token = os.environ["ADS_TOKEN"]
# match bibtex to your list of publication
extra_data = "./src/pub_data.csv"
save_to_file = "./layouts/shortcodes/pub_list.html"

# list of possible parameters: https://github.com/adsabs/adsabs-dev-api/blob/master/openapi/parameters.yaml
request_cols = [
    "bibcode",
    "citation_count",
    "year",
    "title",
    "author",
    "doctype",
    "doi",
    "pub",
    "volume",
    "page_range",
]
result = requests.get(
    f"https://api.adsabs.harvard.edu/v1/search/query?q=orcid%3A{ocrid}&rows=2000&sort=date%20desc%2C%20bibcode%20desc&fl={','.join(request_cols)}",
    headers={"Authorization": "Bearer " + ads_token},
).json()

if extra_data:
    df = pandas.read_csv(extra_data, index_col=False)

# Get today's date
today = datetime.today()
# Format the date to include the month in English
formatted_date = today.strftime("%B %d, %Y")

html_code = f"""
<p>The list below was generated on {formatted_date}.</p>

<table id="pub-list" class="table table-striped" style="width:100%">
"""

my_places = []  # a list to store the place of my name in the author list

for paper in result["response"]["docs"]:
    authors_str = ""
    detected = False
    etal_done = False
    if len(paper["author"]) < 30:
        for my_place, i in enumerate(paper["author"]):
            i = i.split(",")
            i.reverse()
            try:  # there is white space in first character
                temp_authors_str = i[0].lstrip() + " " + i[1]
            except IndexError:
                temp_authors_str = i[0].lstrip()
            if temp_authors_str.lower() in possible_names:
                authors_str += f"<span style='font-weight: bold;'>{standardized_names}</span>"
                detected = True
                my_places.append(my_place + 1)
                if len(paper["author"]) > 10:
                    authors_str += ", el al.  "
                    etal_done = True
                    break
            else:
                authors_str += temp_authors_str
            authors_str += ", "
        authors_str = authors_str[:-2]
        if not etal_done:
            authors_str = re.sub(r",(?!.*,)", r" &", authors_str)
    else:  # long author list
        i = paper["author"][0]
        i = i.split(",")
        i.reverse()
        try:
            first_author_str = i[0].lstrip() + " " + i[1]
        except IndexError:
            first_author_str = i[0].lstrip()
        if first_author_str.lower() in possible_names:
            authors_str = f" <span style='font-weight: bold;'>{standardized_names}</span>, el al."
        else:
            if len(paper["author"]) > 100:  # safe to assume it is a collaboration paper
                collab_text = "Collaboration paper; "
            else:
                collab_text = ""
            authors_str = (
                f"{first_author_str}, el al. ({collab_text}includes <span style='font-weight: bold;'>{standardized_names}</span>)"
            )
        detected = True
        my_places.append(999)
    if not detected:
        print(
            f"Your author name was not detected in '{paper['title']}'. I suggest you to add an additional possible name"
        )

    # Try to use re.search to find the pattern of arXiv id in the doi field
    try:
        arxiv_possible_matches = [re.search(r"arXiv\.(\d+\.\d+)", i) for i in paper["doi"]]
        # Check if a match was found, those without matches will be None
        for i in arxiv_possible_matches:
            if i:
                arxiv_id = i.group(1)
    except KeyError:
        arxiv_id = None

    buttons_code = """
    <div class="row">
        <div class="col-12 col-lg-3">
            <a target="_blank" href="https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract" class="btn btn-sm btn-primary mt-1">{bibcode}</a>
            <br class="d-none d-lg-block">
            <a target="_blank" href="https://ui.adsabs.harvard.edu/abs/{bibcode}/citations" class="btn btn-sm btn-secondary mt-1">{citation} Citations</a>
    """.format(bibcode=paper["bibcode"], citation=paper["citation_count"])

    if extra_data:
        idx = df["bibcode"] == paper["bibcode"]
        if np.sum(idx) == 1:
            idx = idx.idxmax()
            for column_name in df.columns[1:]:
                buttons_code += """
                
                <br class="d-none d-lg-block">
                <a target="_blank" href="{url}" class="btn btn-sm btn-info mt-1">{column_name}</a>
                """.format(
                    url=df[column_name][idx].lstrip(),
                    column_name=column_name,
                )
        buttons_code += """
        </div>
        """

    html_code += """
    <tr>
        <td width="100%">
            {buttons_code}
            <div class="col-12 col-lg-9 order-first order-lg-0">
                <span class="paper-title">{title}</span><span class="paper-author">{authors}</span>
            </div>
        </td>
    </tr>
    """.format(
        buttons_code=buttons_code, title=paper["title"][0], authors=authors_str
    )

html_code += """
</table>
"""

with open(save_to_file, "w") as f:
    f.write(html_code.encode("ascii", "xmlcharrefreplace").decode())
