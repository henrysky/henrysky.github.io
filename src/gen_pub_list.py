import os

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

html_code = """
<div class="row">
    <div class="col-md-12">
        <table id="pub-list" class="table table-striped" style="width:100%">
"""

for paper in result["response"]["docs"]:
    authors_str = ""
    detected = False
    if len(paper["author"]) < 30:
        for i in paper["author"]:
            i = i.split(",")
            i.reverse()
            try:  # there is white space in first character
                temp_authors_str = i[0].lstrip() + " " + i[1]
            except IndexError:
                temp_authors_str = i[0].lstrip()
            if temp_authors_str.lower() in possible_names:
                authors_str += f"<b>{standardized_names}</b>"
                detected = True
                if len(paper["author"]) > 10:
                    authors_str += ", el al.  "
                    break
            else:
                authors_str += temp_authors_str
            authors_str += ", "
        authors_str = authors_str[:-2]
    else:  # long author list
        i = paper["author"][0]
        i = i.split(",")
        i.reverse()
        try:
            first_author_str = i[0].lstrip() + " " + i[1]
        except IndexError:
            first_author_str = i[0].lstrip()
        if first_author_str.lower() in possible_names:
            authors_str = f" <b>{standardized_names}</b>, el al."
        else:
            authors_str = (
                f"{first_author_str}, el al. (includes <b>{standardized_names}</b>)"
            )
        detected = True
    if not detected:
        print(
            f"Your author name not detected in '{paper['title']}'. I suggest you to add an additional possible name"
        )

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
    </div>
</div>
"""

with open(save_to_file, "w") as f:
    f.write(html_code.encode("ascii", "xmlcharrefreplace").decode())
