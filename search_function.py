from youtubesearchpython import *
from email_css import email_css
from string import capwords

#NUMBER_OF_RESULTS = 20
def run_a_search(query_term, number_of_results):
    customSearch = CustomSearch(query_term, VideoSortOrder.uploadDate, limit = number_of_results, region = "EU")
    data = customSearch.result()
    email_text = ""

    for i in range(0, number_of_results):
        # Checking the view count, low view count videos are skipped/ignored
        view_count_text = data["result"][i]["viewCount"]["text"]
        view_count = ""
        for n in range(0, len(view_count_text)):
            if view_count_text[n].isnumeric():
                view_count += str(view_count_text[n])
            else:
                pass
        if view_count == "":
            pass
        elif int(view_count) < 2000:
            pass
        elif "Schar" in data["result"][i]["title"]:
            pass
        else:
            email_text += f'{data["result"][i]["title"]}\n'
            email_text += f'{data["result"][i]["link"]}\n'
            email_text += f'{data["result"][i]["publishedTime"]}\n\n'

    return email_text

def run_a_search_html(query_term, number_of_results):
    # Call original creators function with custom parameters
    customSearch = CustomSearch(query_term, VideoSortOrder.uploadDate, limit = number_of_results, region = "EU")
    data = customSearch.result()
    email_text = ""
    email_text = email_css


    for i in range(0, number_of_results):
        # Checking the view count, low view count videos are skipped/ignored
        view_count_text = data["result"][i]["viewCount"]["text"]
        view_count = ""
        for n in range(0, len(view_count_text)):
            if view_count_text[n].isnumeric():
                view_count += str(view_count_text[n])
            else:
                pass
        if view_count == "":
            pass
        elif int(view_count) < 500:
            pass
        elif "Schar" in data["result"][i]["title"]:
            pass
        ##############################################################
        # Adding the image, title, link and view count
        else:
            image_ref = data["result"][i]["thumbnails"][0]["url"]
            title_text = data["result"][i]["title"]
            title_text = capwords(title_text)

            email_text += f'<img src="{image_ref}" alt="{title_text}"><br>'

            email_text += f'{title_text}<br>'
            link_text = f'{data["result"][i]["link"]}'
            email_text += f'<a href="{link_text}">Click to view</a>'
            email_text += f' - {data["result"][i]["publishedTime"]}'
            email_text += f' - Views: {data["result"][i]["viewCount"]["text"]}<br><br>'
        ################################################################
    # End HTML
    email_text += """       </p>
        </body>
    </html>
    """
    return email_text