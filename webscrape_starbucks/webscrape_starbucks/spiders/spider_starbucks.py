import scrapy
from urllib.parse import urlencode

class SpiderStarbucksSpider(scrapy.Spider):
    name = 'spider_starbucks'
    allowed_domains = ['starbucks.com']
    start_urls = ['https://www.starbucks.com/']

    def __init__(self):
        # Initialize a set to store unique store identifiers
        self.seen_stores = set()
    def start_requests(self):
        # List of cities in North Carolina with their latitude and longitude
        cities = [
            {"city": "Charlotte", "lat": 35.2271, "lng": -80.8431},
    {"city": "Raleigh", "lat": 35.7796, "lng": -78.6382},
    {"city": "Greensboro", "lat": 36.0726, "lng": -79.7910},
    {"city": "Durham", "lat": 35.9940, "lng": -78.8986},
    {"city": "Winston-Salem", "lat": 36.0999, "lng": -80.2442},
    {"city": "Fayetteville", "lat": 35.0527, "lng": -78.8784},
    {"city": "Cary", "lat": 35.7915, "lng": -78.7812},
    {"city": "High Point", "lat": 35.9557, "lng": -80.0048},
    {"city": "Greenville", "lat": 35.6120, "lng": -77.3664},
    {"city": "Gastonia", "lat": 35.2620, "lng": -81.1873},
    {"city": "Chapel Hill", "lat": 35.9049, "lng": -79.0450},
    {"city": "Rocky Mount", "lat": 35.9383, "lng": -77.7900},
    {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
    {"city": "Huntersville", "lat": 35.4106, "lng": -80.8423},
    {"city": "Indian Trail", "lat": 35.0982, "lng": -80.6207},
    {"city": "Mooresville", "lat": 35.5849, "lng": -80.8100},
    {"city": "Jacksonville", "lat": 34.7455, "lng": -77.4305},
    {"city": "Apex", "lat": 35.7312, "lng": -78.8503},
    {"city": "Goldsboro", "lat": 35.3855, "lng": -77.9980},
    {"city": "Asheville", "lat": 35.5951, "lng": -82.5515},
    {"city": "Concord", "lat": 35.4087, "lng": -80.5795},
    {"city": "Shelby", "lat": 35.2904, "lng": -81.5347},
    {"city": "Statesville", "lat": 35.7823, "lng": -80.8893},
    {"city": "Wilson", "lat": 35.7213, "lng": -77.9154},
    {"city": "Lumberton", "lat": 34.6251, "lng": -78.9993},
    {"city": "Hickory", "lat": 35.7345, "lng": -81.3412},
    {"city": "New Bern", "lat": 35.1085, "lng": -77.0441},
    {"city": "Pinehurst", "lat": 35.1940, "lng": -79.3920},
    {"city": "Wilmington", "lat": 34.2257, "lng": -77.9447},
    {"city": "Brevard", "lat": 35.2345, "lng": -82.7332},
    {"city": "Lexington", "lat": 35.8259, "lng": -80.2538},
    {"city": "Kinston", "lat": 35.2621, "lng": -77.5861},
    {"city": "Albemarle", "lat": 35.3503, "lng": -80.2006},
    {"city": "Asheboro", "lat": 35.7079, "lng": -79.8136},
    {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
    {"city": "Carrboro", "lat": 35.9101, "lng": -79.0753},
    {"city": "Clayton", "lat": 35.6507, "lng": -78.4564},
    {"city": "Elizabeth City", "lat": 36.2946, "lng": -76.2510},
    {"city": "Garner", "lat": 35.7113, "lng": -78.6142},
    {"city": "Havelock", "lat": 34.8791, "lng": -76.9013},
    {"city": "Henderson", "lat": 36.3296, "lng": -78.3992},
    {"city": "Holly Springs", "lat": 35.6513, "lng": -78.8336},
    {"city": "Hope Mills", "lat": 34.9704, "lng": -78.9453},
    {"city": "Kannapolis", "lat": 35.4874, "lng": -80.6217},
    {"city": "Kernersville", "lat": 36.1199, "lng": -80.0737},
    {"city": "Laurinburg", "lat": 34.7740, "lng": -79.4628},
    {"city": "Lenoir", "lat": 35.9140, "lng": -81.5380},
    {"city": "Lillington", "lat": 35.3993, "lng": -78.8153},
    {"city": "Lincolnton", "lat": 35.4732, "lng": -81.2543},
    {"city": "Lumberton", "lat": 34.6182, "lng": -79.0086},
    {"city": "Matthews", "lat": 35.1168, "lng": -80.7237},
    {"city": "Monroe", "lat": 34.9854, "lng": -80.5495},
    {"city": "Morganton", "lat": 35.7454, "lng": -81.6848},
    {"city": "Mount Airy", "lat": 36.4993, "lng": -80.6073},
    {"city": "Mount Holly", "lat": 35.2987, "lng": -81.0151},
    {"city": "Murraysville", "lat": 34.2991, "lng": -77.8283},
     {"city": "Nashville", "lat": 35.9743, "lng": -77.9653},
    {"city": "Oak Island", "lat": 33.9200, "lng": -78.1500},
    {"city": "Oxford", "lat": 36.3102, "lng": -78.5906},
    {"city": "Reidsville", "lat": 36.3543, "lng": -79.6645},
    {"city": "Roanoke Rapids", "lat": 36.4615, "lng": -77.6544},
    {"city": "Salisbury", "lat": 35.6709, "lng": -80.4742},
    {"city": "Sanford", "lat": 35.4799, "lng": -79.1803},
    {"city": "Selma", "lat": 35.5360, "lng": -78.2831},
    {"city": "Smithfield", "lat": 35.5085, "lng": -78.3397},
    {"city": "Southern Pines", "lat": 35.1740, "lng": -79.3928},
    {"city": "Spring Lake", "lat": 35.1679, "lng": -78.9783},
    {"city": "Tarboro", "lat": 35.8963, "lng": -77.5356},
    {"city": "Thomasville", "lat": 35.8826, "lng": -80.0816},
    {"city": "Wake Forest", "lat": 35.9799, "lng": -78.5097},
    {"city": "Washington", "lat": 35.5463, "lng": -77.0528},
    {"city": "Waynesville", "lat": 35.4887, "lng": -82.9887},
    {"city": "Whiteville", "lat": 34.3302, "lng": -78.7036},
    {"city": "Zebulon", "lat": 35.8249, "lng": -78.3142},
    {"city": "Kings Mountain", "lat": 35.2440, "lng": -81.3412},
    {"city": "Boone", "lat": 36.2168, "lng": -81.6746},
    {"city": "Franklin", "lat": 35.1826, "lng": -83.3812},
    {"city": "Sylva", "lat": 35.3734, "lng": -83.2250},
    {"city": "Bryson City", "lat": 35.4304, "lng": -83.4474},
    {"city": "Marion", "lat": 35.6848, "lng": -82.0093},
    {"city": "Black Mountain", "lat": 35.6179, "lng": -82.3215},
    {"city": "Hendersonville", "lat": 35.3187, "lng": -82.4609},
    {"city": "Blowing Rock", "lat": 36.1359, "lng": -81.6770},
    {"city": "Banner Elk", "lat": 36.1637, "lng": -81.8715},
    {"city": "Elkin", "lat": 36.2449, "lng": -80.8487},
    {"city": "Wilkesboro", "lat": 36.1468, "lng": -81.1598}
        ]

        for city in cities:
            params = {
                'lat': city['lat'],
                'lng': city['lng'],
                'place': city['city'],
                'limit': 100,  # You can adjust the number of results per query
                'offset': 0,   # Start at the first page (offset 0)
            }

            url_with_params = f"https://www.starbucks.com/bff/locations?{urlencode(params)}"

            headers = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://www.starbucks.com/store-locator?map=35.759573,-79.0193,5z&place=North%20Carolina',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-0a132146c0f363f9e964dc29fb206e21-0316eaa77aff5cba-01',
                'tracestate': '1306312@nr=0-1-1307519-24549305-0316eaa77aff5cba----1735153630647',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            cookies = {
                'ux_exp_id': '5cbb2bf6-78d8-485f-bb30-cddee6dc1dfe',
                'tiWQK2tY': 'A7vgNv-TAQAAX01NPkRxpgzPM-flQ6QSyoxfGp3DtccnkHtypbbzmXduh0hwASktxJGucu_LwH8AAEB3AAAAAA|1|0|c016a22a9b7c9cee69a2ae9092e5c04f061f692d',
                'TAsessionID': 'bb7f6f23-813e-4670-b325-20b28897bee1|NEW',
                'notice_behavior': 'implied,us',
                'mtiE3Uno': '',
                '_gcl_au': '1.1.1548366207.1735153608',
                '_gid': 'GA1.2.466560019.1735153609',
                '_dc_gtm_UA-82424379-1': '1',
                'ASLBSA': '00038f952e2a0e4383b269b31ee1c78eb55416d298f826927ef4ff9ef6ab361c81bb',
                'ASLBSACORS': '00038f952e2a0e4383b269b31ee1c78eb55416d298f826927ef4ff9ef6ab361c81bb',
                '_uetsid': '649d6700c2f311ef8d21057c5a2adfcb',
                '_uetvid': '649d75f0c2f311ef91aab1da33813eea',
                '_ga': 'GA1.1.159194907.1735153609',
                'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'qb9kO9vGnqSUhQHAcvpq3tEwwHq1v0CEibnzaJkuO5Y=',
                'notice_preferences': '2:',
                'notice_gdpr_prefs': '0,1,2:',
                'cmapi_gtm_bl': '',
                'cmapi_cookie_privacy': 'permit 1,2,3',
                '_ga_Q8JXK1T67J': 'GS1.1.1735153611.1.1.1735153630.0.0.0',
                '_ga_VMTHZW7WSM': 'GS1.1.1735153609.1.1.1735153630.0.0.0'
            }

            # Make the request for each city
            yield scrapy.Request(url_with_params, headers=headers, cookies=cookies, callback=self.parse)


    def parse(self, response):
        if response.status == 200:
            try:
                data = response.json()  # Parse the JSON response

                # Log the response content for debugging
                self.logger.info(f"Response JSON: {data}")

                if isinstance(data, list):  # Check if the response is a list
                    for location_data in data:
                        store = location_data.get('store', {})  # Get the 'store' key

                        # Extract the desired fields
                        store_name = store.get('name', 'N/A')
                        address = store.get('address', {}).get('singleLine', 'N/A')
                        city = store.get('address', {}).get('city', 'N/A')
                        state = store.get('address', {}).get('countrySubdivisionCode', 'N/A')
                        postal_code = store.get('address', {}).get('postalCode', 'N/A')
                        store_number = store.get('storeNumber', 'N/A')

                        # Extract latitude and longitude
                        coordinates = store.get('coordinates', {})
                        lat = coordinates.get('latitude', 'N/A')
                        long = coordinates.get('longitude', 'N/A')

                        # Extract phone number
                        phone_number = store.get('phoneNumber', 'N/A')

                        # Extract amenities
                        amenities = [amenity.get('name', 'N/A') for amenity in store.get('amenities', [])]

                        # Check if this store has already been processed
                        if store_number not in self.seen_stores:
                            self.seen_stores.add(store_number)  # Mark as seen
                            # Yield the data
                            yield {
                                'store_name': store_name,
                                'address': address,
                                'city': city,
                                'state': state,
                                'postal_code': postal_code,
                                'store_number': store_number,
                                'phone_number': phone_number,
                                'lat': lat,
                                'long': long,
                                'amenities': amenities,
                            }

            except ValueError as e:
                self.logger.error(f"Failed to parse JSON response: {e}")
        else:
            self.logger.error(f"Failed to fetch data. Status code: {response.status}")