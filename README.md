# Living-Place-Recommendation

1.DESCRIPTION

We are building an online platform that provides proper recommendations for apartment seekers with the options to take multiple factors into account. Most of the current search services are single-faceted, so we provide a user-oriented platform with an integrated information system for customers that can interactively obtain and filter information based on multiple choices.

2.INSTALLATION - How to install and setup your code

Install the python on your computer & download our document

3.EXECUTION
  1. Download the Document:
      demo is in CODE/FrontEnd
        1. decompress the zip document
        2. Open up the console
        3. enter `cd + CODE document link`
        4. enter `python3 -m http.server 8888` in the console
        5. Open `http://localhost:8888/FrontEnd/` in your browser

## Data Source
Using Yelp Fusion API:
The Yelp Fusion API uses private key authentication to authenticate all endpoints. Private API Key will be automatically generated after creating  the app. Include API key in headers to send request. 
Request: GET https://api.yelp.com/v3/businesses/search
Parameters we query: location(string), latitude(decimal), longitude(decimal), name(string), city = "New York City", term = "restaurant/food"
Other info: url, transactions: pickup / delivery, categories etc.
More information can be found in url: https://www.yelp.com/developers/documentation/v3/business_search


