import requests

def find_wikidata_id_list(company):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "search": company,
        "language": "en",
        "format": "json",
        "type": "item"
    }
    headers = {
    "User-Agent": "AccountResearchAssistant/1.0 (https://github.com/davide96a/account_research_assistant/tree/main)"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.HTTPError:
        print("HTTP error, the server replied with", response.status_code)
        return None
    except requests.Timeout:
        print("The request exceeded the time limit")
        return None
    except requests.RequestException:
        print("There's been an error during the request execution")
        return None
    data_id = response.json()
    wikidata_id_list = []
    for element in data_id["search"]:
        wikidata_id_list.append({"id": element["id"], "description": element["description"]})
    return wikidata_id_list
    #return(data_id["search"][0]["id"])



def filter_entities_id(wikidata_id_list):
    companies_list = []
    for element in wikidata_id_list:
        if check_whether_is_company(from_wikiid_to_entity_data(element["id"])):
            companies_list.append({"id": element["id"], "description": element["description"]})
    return companies_list




def from_wikiid_to_entity_data(wikiid):
    url = "https://www.wikidata.org/w/api.php"
    params_id = {
        "action": "wbgetentities",
        "ids": wikiid,
        "format": "json",
        "props": "claims"
    }
    headers = {
    "User-Agent": "AccountResearchAssistant/1.0 (https://github.com/davide96a/account_research_assistant/tree/main)"
    }

    try:
        response = requests.get(url, params=params_id, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.HTTPError:
        print("HTTP error, the server replied with", response.status_code)
        return None
    except requests.Timeout:
        print("The request exceeded the time limit")
        return None
    except requests.RequestException:
        print("There's been an error during the request execution")
        return None
    entity_data_all = response.json()
    entity_data = entity_data_all["entities"][wikiid]["claims"]["P31"]
    return(entity_data)



def check_whether_is_company(entity_data):
    for element in entity_data:
        if element["mainsnak"]["datavalue"]["value"]["id"] == "Q4830453":
            return True 
    return False


def display_n_choose_company(companies_list):
    for index, element in enumerate(companies_list):
        print(index +1, "-", element["description"])
    chosen = input("Type the number of the companies you want to explore. If more than 1, separate them with a comma (e.g. '1,3')")
    chosen = chosen.split(",")
    companies_id_list = []
    for element in chosen:
        number = (int(element.strip()) -1)
        companies_id_list.append(companies_list[number]["id"])
    return companies_id_list


company_input = input("Hi, I'm DavAIde, your sales agent here to support you. Which company would you like to research today? ")
wikidata_id_list = find_wikidata_id_list(company_input)
companies_list = filter_entities_id(wikidata_id_list)
chosen_companies = display_n_choose_company(companies_list)
print(chosen_companies)




#response_id = requests.get(url, params=params_id, headers=headers, timeout=10)
#data_id = response_id.json()
#print(data_id)


#print(find_wikidata_id("Unicredit"))

