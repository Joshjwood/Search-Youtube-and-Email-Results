from youtubesearchpython import *
from email_css import email_css
from string import capwords

number_of_results = 20
def run_a_search(query_term):
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

def run_a_search_html(query_term):
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
            #begin box
            email_text += '<p style="border:2px; border-style:solid; border-color:#00ffff; padding: 1em;" style="text-align:center">'

            image_ref = data["result"][i]["thumbnails"][0]["url"]
            title_text = data["result"][i]["title"]
            title_text = capwords(title_text)
            link_text = f'{data["result"][i]["link"]}'

            email_text += f'<a href="{link_text}"><img src="{image_ref}" alt="{title_text}"></a><br>'

            email_text += f'{title_text}<br>'

            email_text += f'{data["result"][i]["publishedTime"]}'
            email_text += f' - Views: {data["result"][i]["viewCount"]["text"]}<br><br>'

            #end box
            email_text += '</p><br><br>'
        ################################################################
    # End HTML
    email_text += """       </p>
        </body>
    </html>
    """
    return email_text