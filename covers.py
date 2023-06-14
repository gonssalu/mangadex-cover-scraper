import requests, os, sys

# Parse args
if len(sys.argv) == 1:
    print("Usage: python covers.py [manga_id] [locale]")
    exit()

manga = sys.argv[1]
print("Manga ID: " + manga)

locale = None
if len(sys.argv) == 3:
    locale = sys.argv[2].lower()
    print("Locale: " + locale)
else:
    print("No locale specified, downloading covers for all locales")

# Initialize variables
offset = 0
total = 100

# Start
while offset<total:
    # Make the API request
    url = f'https://api.mangadex.org/cover?limit=100&manga[]={manga}&order[volume]=asc&offset={offset}{"&locales[]=" + locale if locale is not None else ""}'
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        exit()

    # Loop through the covers and download the ones that match the criteria
    resJson = response.json()
    offset = resJson['offset']+resJson['limit']
    total = resJson['total']
    covers = resJson['data']
    for cover in covers:
        if cover['type'] != 'cover_art':
            continue
        
        attributes = cover['attributes']
        ext = ' [' + attributes['locale'].upper() + '].' + attributes['fileName'].split('.')[-1]
        
        volume = str(attributes['volume']).zfill(2)
        file_name = f"Volume {volume}{ext}"
        url_file_name = f"https://mangadex.org/covers/{manga}/{attributes['fileName']}"
        
        # Create the manga directory if it doesn't exist
        if not os.path.exists(manga):
            os.makedirs(manga)
        
        # Download the cover
        response = requests.get(url_file_name)
        with open(os.path.join(manga, file_name), 'wb') as f:
            f.write(response.content)
            print(f"Downloaded {file_name}")