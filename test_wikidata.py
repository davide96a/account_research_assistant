import requests

def find_wikidata_id(company):
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
    lista = []
    for element in data_id["search"]:
        lista.append({"id": element["id"], "description": element["description"]})
    #return lista
    return(data_id["search"][0]["id"])


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




company = input("Hi, I'm DavAIde, your sales agent here to support you. Which company would you like to research today? ")
wikiid = find_wikidata_id(company)
entity_data = from_wikiid_to_entity_data(wikiid)
is_company = check_whether_is_company(entity_data)
print(is_company)







#response_id = requests.get(url, params=params_id, headers=headers, timeout=10)
#data_id = response_id.json()
#print(data_id)


#print(find_wikidata_id("Unicredit"))

