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
        if check_whether_is_company(from_wikiid_to_entity_claims(element["id"])):
            companies_list.append({"id": element["id"], "description": element["description"]})
    return companies_list




def from_wikiid_to_entity_claims(wikiid):
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
    entity_claims = entity_data_all["entities"][wikiid]["claims"]
    return(entity_claims)



def check_whether_is_company(entity_data):
    for element in entity_data.get("P31", []):
        if element["mainsnak"]["datavalue"]["value"]["id"] == "Q4830453":
            return True 
    return False


def display_n_choose_company(companies_list):
    for index, element in enumerate(companies_list):
        print(index +1, "-", element["description"])
    chosen = input("Type the number of the companies you want to explore. If more than 1, separate them with a comma (e.g. '1,3'). ")
    chosen = chosen.split(",")
    companies_id_n_decription_list = []
    for element in chosen:
        try:
            number = (int(element.strip()) -1)
            if number >= 0 and number <= len(companies_list) -1:
                companies_id_n_decription_list.append({"id": companies_list[number]["id"], "description": companies_list[number]["description"]})
        except ValueError:
            continue
    if len(companies_id_n_decription_list) > 0:
        return companies_id_n_decription_list
    else:
        print("You haven't picked any of the companies displayed")
        return None


def extract_employees_from_entity_claims(entity_claims):
    if entity_claims.get("P1128") is None:
        return "unknown"
    for element in entity_claims["P1128"]:
        employee_number = element["mainsnak"]["datavalue"]["value"]["amount"]
    return employee_number

def extract_sector_from_entity_claims(entity_claims):
    if entity_claims.get("P452") is None:
        return "unknown"
    sectors_list = []
    for element in entity_claims["P452"]:
        company_sector = element["mainsnak"]["datavalue"]["value"]["id"]
        company_sector = from_wikiid_to_label(company_sector)
        sectors_list.append(company_sector)
    sectors_list = ", ".join(sectors_list)
    return sectors_list

def extract_revenue_from_entity_claims(entity_claims):
    if entity_claims.get("P2139") is None:
        return "unknown"
    for element in entity_claims["P2139"]:
        revenue = element["mainsnak"]["datavalue"]["value"]["amount"]
    return revenue


def from_wikiid_to_label(wikiid):
    url = "https://www.wikidata.org/w/api.php"
    params_id = {
        "action": "wbgetentities",
        "ids": wikiid,
        "format": "json",
        "props": "labels"
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
    label = entity_data_all["entities"][wikiid]["labels"]["en"]["value"]
    return(label)


company_input = input("Hi, I'm DavAIde, your sales agent here to support you. Which company would you like to research today? ").capitalize()
wikidata_id_n_description_list = find_wikidata_id_list(company_input)
companies_list = filter_entities_id(wikidata_id_n_description_list)
chosen_companies = display_n_choose_company(companies_list)
if chosen_companies is not None:
    for id_n_description_list in chosen_companies:
        entity_claims = from_wikiid_to_entity_claims(id_n_description_list["id"])
        employees = extract_employees_from_entity_claims(entity_claims)
        sector = extract_sector_from_entity_claims(entity_claims)
        revenue = extract_revenue_from_entity_claims(entity_claims)
        print(f"The number of employees of {company_input}, {id_n_description_list['description']}, is {employees}, its sector is {sector} and its total revenue is {revenue}")







