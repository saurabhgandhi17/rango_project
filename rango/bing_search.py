import json
import urllib
import http.client
import certifi as cer


def read_bing_key():
    bing_api_key = None

    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline()
    except:
        raise IOError('bing.key file not found')

    return bing_api_key


def run_query(search_terms):

    bing_api_key = read_bing_key()

    if not bing_api_key:
        raise KeyError("Bing Key Not Found")

    host = "api.cognitive.microsoft.com"
    path = "/bing/v7.0/search"

    headers = {'Ocp-Apim-Subscription-Key': bing_api_key}

    conn = http.client.HTTPSConnection(host)

    query = urllib.parse.quote(search_terms)
    print(query)

    conn.request("GET", path + "?q=" + query, headers=headers)

    response = conn.getresponse()

    headers = [k + ": " + v for (k, v) in response.getheaders()
               if k.startswith("BingAPIs-") or k.startswith("X-MSEdge-")]

    result = response.read().decode("utf8")
    results = []

    json_response = json.loads(result)

    for result in json_response['webPages']['value']:
        results.append(
            {'title': result['name'], 'link': result['url'], 'summary': result['snippet']})
    return results


def main():
    search_item = input("Enter your query: ")
    r = run_query(search_item)
    print(r)


if __name__ == '__main__':
    main()


# import json
# import urllib # Py3
# import urllib.request


# def read_bing_key():

# 	bing_api_key = None

# 	try:
# 		with open('bing.key', 'r') as f:
# 			bing_api_key = f.readline()
# 	except:
# 		raise IOError('bing.key file not found')

# 	return bing_api_key

# def run_query(search_terms):

# 	bing_api_key = read_bing_key()

# 	if not bing_api_key:
# 		raise KeyError("Bing Key Not Found")

# 	# Specify the base url and the service (Bing Search API 2.0)
# 	root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search'
# 	service = 'Web'

# 	# Specify how many results we wish to be returned per page.
# 	# Offset specifies where in the results list to start from.
# 	# With results_per_page = 10 and offset = 11, this would start from page 2.
# 	results_per_page = 10
# 	offset = 0

# 	query = "'{0}'".format(search_terms)

# 	query = urllib.parse.quote(query);print(f"this is : {query}")  # Py3

# 	search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
# 				root_url,
# 				service,
# 				results_per_page,
# 				offset,
# 				query);print(f"search : {search_url} ")

# 	username = ''

# 	password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()  # Py3

# 	# The below line will work for both Python versions.
# 	headers = {'Ocp-Apim-Subscription-Key': bing_api_key}
# 	password_mgr.add_password(None, search_url, username,headers)

# 	results = []

# 	try:

# 		handler = urllib.request.HTTPBasicAuthHandler(password_mgr)  # Py3
# 		opener = urllib.request.build_opener(handler)  # Py3
# 		urllib.request.install_opener(opener)  # Py3

# 		# Connect to the server and read the response generated.
# 		response = urllib.request.urlopen(search_url).read()  # Py3
# 		response = response.decode('utf-8')  # Py3

# 		json_response = json.loads(response)

# 		# Loop through each page returned, populating out results list.
# 		for result in json_response['d']['results']:
# 			results.append({'title': result['Title'],
# 				'link': result['Url'],
# 				'summary': result['Description']})
# 	except Exception as e:
# 		print(f"Error when querying the Bing API:{e}")

# 	return results
