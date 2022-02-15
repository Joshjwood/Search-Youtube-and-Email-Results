from youtubesearchpython import *

NUMBER_OF_RESULTS = 20
def run_a_search(query_term, number_of_results):
    customSearch = CustomSearch(query_term, VideoSortOrder.uploadDate, limit = NUMBER_OF_RESULTS, region = "EU")
    data = customSearch.result()
    email_text = ""

    for i in range(0, NUMBER_OF_RESULTS):
        email_text += f'{data["result"][i]["title"]}\n'
        email_text += f'{data["result"][i]["link"]}\n'
        email_text += f'{data["result"][i]["publishedTime"]}\n\n'

    return email_text