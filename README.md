# Loadsmart Challenge
_Author: Marcos Monteiro_ 

### Basics

#### Python

The Python version used for this challenge was Python **3.7.4** - available at [python.org](https://www.python.org/downloads/release/python-374/).

#### Creating and setting up a virtual environment

The first and most important thing to do in order to run this code, is to create and set up a new virtual environment. If you don't have **virtualenv** installed, the following command installs it using **pip**:

```bash
pip install virtualenv
```

Creating a new virtual environment:

```bash
virtualenv env
```

Activating the environment:

```bash
source env/bin/activate
```

Installing all dependency packages:

```bash
pip install -r requirements.txt
```

#### Testing

In a new terminal window, it's now possible to run the automated tests for this code. Pytest has already been installed along with the other dependecies and it's ready to use:

```bash
pytest -v
```

All tests should pass.

#### Running

Finally, in order to run the API _per se_, from the project root directory, the following command will initialize **Uvicorn** and start the main application:

```bash
uvicorn app.main:app
```

The server is now running at `http://127.0.0.1:8000` and interactive documentation interfaces can be found at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc), where it's possible to test the API directly from the browser.

The only endpoint for this challenge is the **POST** endpoint `/mapping/`. This endpoint will receive a JSON input with a list of trucks and cargos and will respond with a JSON mapping each cargo to the closest available truck to it. Available meaning that the truck hasn't been used yet.


### Approach

#### The algorithm

To solve this problem, a Kd-Tree approach was used in order to structure the nodes (trucks) spatially and thus be able to find the closest node to a point (cargo) very easily. This Kd-Tree implementation does not supports deletion, so a hashtable was used to map the already busy trucks and ignoring them on the search. The average complexity for building the tree is O(n), where n is the amount of trucks, and the average complexity of a search is O(log(n)), since a Kd-Tree is actually a binary tree. It's important to note that as the number of cargos approaches the number of trucks, the search tends to behave in O(n) time, as more and more trucks become 'busy' and have to be ignored in the search.

#### Framework

The chosen framework to attack this problem was [FastAPI](https://fastapi.tiangolo.com/) since it's very sleek, agile and have great support to modeling JSON inputs/outputs with [Pydantic](https://pydantic-docs.helpmanual.io/) and provides an interactive documentation.


### Example

The .csv example files were converted to a JSON in the proper input format so the API can be manually tested from the [interactive documentation](http://127.0.0.1:8000/docs#/default/_map_cargos_to_trucks_mapping__post):

```json
{
   "trucks":[
      {
         "truck":"Hartford Plastics Incartford",
         "city":"Florence",
         "state":"AL",
         "lat":34.79981,
         "lng":-87.677251
      },
      {
         "truck":"Beyond Landscape & Design Llcilsonville",
         "city":"Fremont",
         "state":"CA",
         "lat":37.5482697,
         "lng":-121.9885719
      },
      {
         "truck":"Empire Of Dirt Llcquality",
         "city":"Hampden",
         "state":"ME",
         "lat":44.7445421,
         "lng":-68.8370436
      },
      {
         "truck":"James Haas Al Haas Shelly Haasairfield",
         "city":"North East",
         "state":"MD",
         "lat":39.6001132,
         "lng":-75.94133269999999
      },
      {
         "truck":"Ibrahim Chimandalpharetta",
         "city":"Toledo",
         "state":"OH",
         "lat":41.6639383,
         "lng":-83.55521200000001
      },
      {
         "truck":"John Bianchiake Havasu City",
         "city":"Renton",
         "state":"WA",
         "lat":47.48287759999999,
         "lng":-122.2170661
      },
      {
         "truck":"Macomb Iron Llchesterfield",
         "city":"Cleveland",
         "state":"OH",
         "lat":41.49932,
         "lng":-81.6943605
      },
      {
         "truck":"Robert Robertsonairhope",
         "city":"Green Bay",
         "state":"WI",
         "lat":44.51915899999999,
         "lng":-88.019826
      },
      {
         "truck":"Viking Products Of Austin Incustin",
         "city":"Fort Campbell",
         "state":"TN",
         "lat":36.6634467,
         "lng":-87.47739020000002
      },
      {
         "truck":"Arachus Incashville",
         "city":"Bethlehem",
         "state":"PA",
         "lat":40.6259316,
         "lng":-75.37045789999999
      },
      {
         "truck":"Dawna L Zanderppleton",
         "city":"Burbank",
         "state":"WA",
         "lat":46.1998568,
         "lng":-119.0130618
      },
      {
         "truck":"Michael J Geenenaukauna",
         "city":"Lubbock",
         "state":"TX",
         "lat":33.5778631,
         "lng":-101.8551665
      },
      {
         "truck":"Peet'S Tree Serviceinterport",
         "city":"Schertz",
         "state":"TX",
         "lat":29.5521737,
         "lng":-98.269734
      },
      {
         "truck":"Filippo Lumaroallston",
         "city":"La Porte",
         "state":"TX",
         "lat":29.6657838,
         "lng":-95.0193728
      },
      {
         "truck":"Jorge L Denisollywood",
         "city":"Delta",
         "state":"CO",
         "lat":38.7422062,
         "lng":-108.0689582
      },
      {
         "truck":"Ramiro Castilloucson",
         "city":"Logan",
         "state":"UT",
         "lat":41.7369803,
         "lng":-111.8338359
      },
      {
         "truck":"Paul J Krez Companyorton Grove",
         "city":"Forest City",
         "state":"NC",
         "lat":35.3340108,
         "lng":-81.8651028
      },
      {
         "truck":"Sullivans' Homestead Inclympia",
         "city":"Deerfield Beach",
         "state":"FL",
         "lat":26.3184123,
         "lng":-80.09976569999999
      },
      {
         "truck":"Jeffrey A Shepardypsum",
         "city":"Dalton",
         "state":"GA",
         "lat":34.7698021,
         "lng":-84.9702228
      },
      {
         "truck":"Wayne E Bollinauvoo",
         "city":"North Logan",
         "state":"UT",
         "lat":41.7693747,
         "lng":-111.8046654
      },
      {
         "truck":"Gary Lee Wilcoxpencer",
         "city":"Eagle River",
         "state":"WI",
         "lat":45.9171763,
         "lng":-89.2442988
      },
      {
         "truck":"Jacques N Faucherochester",
         "city":"Mission",
         "state":"KS",
         "lat":39.0277832,
         "lng":-94.6557914
      },
      {
         "truck":"Sidhu Trucking Incarrisburg",
         "city":"Hawkins",
         "state":"TX",
         "lat":32.58847350000001,
         "lng":-95.20411349999999
      },
      {
         "truck":"Edmon'S Unique Furniture & Stone Gallery Inc.Os Angeles",
         "city":"Bolingbrook",
         "state":"IL",
         "lat":41.69864159999999,
         "lng":-88.0683955
      },
      {
         "truck":"Ricardo Juradoacramento",
         "city":"Covesville",
         "state":"VA",
         "lat":37.8901411,
         "lng":-78.70474010000001
      },
      {
         "truck":"Turenne Auto Body Llchorp",
         "city":"Schertz",
         "state":"TX",
         "lat":29.5521737,
         "lng":-98.269734
      },
      {
         "truck":"Allen R Pruittrown City",
         "city":"La Porte",
         "state":"TX",
         "lat":29.6657838,
         "lng":-95.0193728
      },
      {
         "truck":"Kjellberg'S Carpet Oneuffalo",
         "city":"Mount Vernon",
         "state":"OH",
         "lat":40.3933956,
         "lng":-82.4857181
      },
      {
         "truck":"Dupree Testing Services Incutchinson",
         "city":"Houston",
         "state":"TX",
         "lat":29.7604267,
         "lng":-95.3698028
      },
      {
         "truck":"Vincent Rodriguezansas City",
         "city":"Flagstaff",
         "state":"AZ",
         "lat":35.1982836,
         "lng":-111.651302
      },
      {
         "truck":"Loren Martinrand Junction",
         "city":"Forest Grove",
         "state":"OR",
         "lat":45.5198364,
         "lng":-123.1106631
      },
      {
         "truck":"I N H Relocation Services Incoodbridge",
         "city":"San Antonio",
         "state":"TX",
         "lat":29.4241219,
         "lng":-98.49362819999999
      },
      {
         "truck":"Arrow Towing Llcent",
         "city":"Hackettstown",
         "state":"NJ",
         "lat":40.8539879,
         "lng":-74.8290555
      },
      {
         "truck":"Scott Cassidylanchardville",
         "city":"Denver",
         "state":"CO",
         "lat":39.76161889999999,
         "lng":-104.9622498
      },
      {
         "truck":"Como Construction Llcottstown",
         "city":"Wanaque",
         "state":"NJ",
         "lat":41.0381525,
         "lng":-74.2940378
      },
      {
         "truck":"High Pines Farm Llcontello",
         "city":"Chicago",
         "state":"IL",
         "lat":41.8781136,
         "lng":-87.6297982
      },
      {
         "truck":"Jwj Interests Incealy",
         "city":"Glen Burnie",
         "state":"MD",
         "lat":39.1626084,
         "lng":-76.6246886
      },
      {
         "truck":"Efrain Morales Diazorwalk",
         "city":"Marshfield",
         "state":"MO",
         "lat":37.338658,
         "lng":-92.9071209
      },
      {
         "truck":"Rubye Hunterincolnton",
         "city":"Elizabeth",
         "state":"NJ",
         "lat":40.6639916,
         "lng":-74.2107006
      },
      {
         "truck":"Jevin Q Watsonillsboro",
         "city":"McDonough",
         "state":"GA",
         "lat":33.4473361,
         "lng":-84.1468616
      },
      {
         "truck":"Martinez Transport Llcdaho Falls",
         "city":"Chicago",
         "state":"IL",
         "lat":41.8781136,
         "lng":-87.6297982
      },
      {
         "truck":"Jeffery Allan Luiacine",
         "city":"Tuscaloosa",
         "state":"AL",
         "lat":33.2098407,
         "lng":-87.56917349999999
      },
      {
         "truck":"Fish-Bones Towingew York",
         "city":"Monroe",
         "state":"WI",
         "lat":42.60111939999999,
         "lng":-89.6384532
      },
      {
         "truck":"Wisebuys Stores Incouverneur",
         "city":"Washington",
         "state":"WV",
         "lat":39.244853,
         "lng":-81.6637765
      }
   ],
   "cargos":[
      {
         "product":"Light bulbs",
         "origin_city":"Sikeston",
         "origin_state":"MO",
         "origin_lat":36.876719,
         "origin_lng":-89.5878579,
         "destination_city":"Grapevine",
         "destination_state":"TX",
         "destination_lat":32.9342919,
         "destination_lng":-97.0780654
      },
      {
         "product":"Recyclables",
         "origin_city":"Christiansburg",
         "origin_state":"VA",
         "origin_lat":37.1298517,
         "origin_lng":-80.4089389,
         "destination_city":"Apopka",
         "destination_state":"FL",
         "destination_lat":28.6934076,
         "destination_lng":-81.5322149
      },
      {
         "product":"Apples",
         "origin_city":"Columbus",
         "origin_state":"OH",
         "origin_lat":39.9611755,
         "origin_lng":-82.99879419999999,
         "destination_city":"Woodland",
         "destination_state":"CA",
         "destination_lat":38.67851570000001,
         "destination_lng":-121.7732971
      },
      {
         "product":"Wood",
         "origin_city":"Hebron",
         "origin_state":"KY",
         "origin_lat":39.0661472,
         "origin_lng":-84.70318879999999,
         "destination_city":"Jefferson",
         "destination_state":"LA",
         "destination_lat":29.96603709999999,
         "destination_lng":-90.1531298
      },
      {
         "product":"Cell phones",
         "origin_city":"Hickory",
         "origin_state":"NC",
         "origin_lat":35.7344538,
         "origin_lng":-81.3444573,
         "destination_city":"La Pine",
         "destination_state":"OR",
         "destination_lat":43.67039949999999,
         "destination_lng":-121.503636
      },
      {
         "product":"Wood",
         "origin_city":"Northfield",
         "origin_state":"MN",
         "origin_lat":44.4582983,
         "origin_lng":-93.161604,
         "destination_city":"Waukegan",
         "destination_state":"IL",
         "destination_lat":42.3636331,
         "destination_lng":-87.84479379999999
      },
      {
         "product":"Oranges",
         "origin_city":"Fort Madison",
         "origin_state":"IA",
         "origin_lat":40.6297634,
         "origin_lng":-91.31453499999999,
         "destination_city":"Ottawa",
         "destination_state":"IL",
         "destination_lat":41.3455892,
         "destination_lng":-88.8425769
      }
   ]
}
```