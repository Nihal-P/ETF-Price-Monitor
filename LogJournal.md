# LogJournal.md

## 2026-01-02

### 

The purpouse of this log journal is to document my progress and thoughts as I work on this project.
This may also help the reviewers understand the reason behind my choices and decisions.

### 

1. First thoughts and Goals:
- The requirements mentioned about stock related words such as weights and constituents, so need to reasearch about that.
    - weights add up to 1 to make it a valid ETF.
    - constituents are the stocks that make up the ETF.
    - etf price calculation will be calculated as (weight * price of constituent) for each constituent and summing them up.
- Have a look at the csv files provided and understand the structure of the data.
- Figure out what frontend and backend frameworks to use.
    - Going with React for frontend with typescript since i do have experience with it.
    - For backend, was thinking to go with node.js but after some online digging it looks Python might be a better choice as i can use Pandas or numpy for data processing. and seems to be used by DCT as well.

2. Basic simplifed Architecture and Design choices:
- I am thinking to plan the base design for what i think a mvp should be.
- Lets simiplify it so there is a button to upload the csv file. which will parse the file and show it in chart.
- Frontend: 
    - React with typescript.
        - file upload component.
        - chart component.
        - later other charts
        - Also considering Redux but not sure there seems to be a use case since we are only going to be displaying the data and there is no manipulation required. but might come back to this.
    - Libraries:
        - ~~Chart.js for charts. Was thinking of using AG grid for the table view but requires enterprise for that.~~ Actually there is AG grid community version which is free. and Echarts for other charts since we require a zoomable time series chart.
        - Axios for API calls.
- Backend: Python with FastAPI.
    - used for HTTP/REST API calls.
    - current thinking for calls:
        - POST /upload-etf
        - GET /constituents (to get table data?)
        - GET /etf-price (to get etf price?) 
        - GET /top-holdings (to get top holdings?) "?" since might change as we go along.

    - Data Processing:
        - CSV parsing using pandas but might change to numpy if needed later on.
        - for some of the get calls, we will need to do some calculations.
        - ASSUMPTION: the prices csv file will be the only one that will be used and assume will be compatible with the ETF file provided by a user.

    - Data layer:
        - we can keep the prices csv loaded as a static data
        - also temporarly keep the ETF file as static data
        - later i might come back so i can try to do some caching if that helps?


3. Starting with backend:
    - found some useful libraries to add in the requirements.txt like python-multipart for file upload.
    - started with the main.py file and added the basic FastAPI setup.
    - added CORS middleware to allow requests from the frontend.
    - added a health check endpoint.
    - got the server running using `uvicorn main:app --reload`

4. Understand frontend UI to create the structure of the api endpoints.
    - now to create the structure of the api endpoints i need understand what needs to be shown in the frontend.
    - a. File upload component.
        - we can create a button or dropzone to upload the file.
        - this will trigger a POST method to /upload-etf endpoint.
        - this will return a success message or error message.
    - b. interactive table
        - a table that wiill basically show each constituent and its weight.
        - this will trigger a GET method to /constituents endpoint.
        - assuming a response like:
            Response: [
               {"name": "A", "weight": 0.087, "price": 27.03},
               {"name": "F", "weight": 0.146, "price": 49.10}, 
            ]
    - c. Time series chart
        - similar get method as the table
        - Response: [
           {"date": "2017-01-01", "price": 65.32},...]
    - d. bar chart
        - similar get method as the table
        - Response: [
           {"name": "A", "value": 11.23, "weight": 0.087, "price": 27.03},...]

5. Implemented the first upload endpoint
    - created a upload_etf POST route which takes a file as passes it in the etf_service.upload_etf method.
    - that service currently just returns a success message or error message with basic stats so we can
    verify the file was uploaded correctly.
    - I tested the method by uploading the etf in insomnia(similar to postman) as form-data on the 
    url http://localhost:8000/api/upload-etf as POST method.
    - Created a init inside the api folder to package all the routers and export them to be used in main.py

6. Implemented the constituents endpoint 
    - created a constituents GET route which takes a file as passes it in the etf_service.upload_etf method.
    - this service returns a list of constituents with name, weight and price. IT is list of dict because i will be using AG grid library for the table view and it requires data in that format.


## 2026-01-03

1. Implemented the etf prices endpoint
    - created a etf_prices GET route which takes a file as passes it in the etf_service.upload_etf method.
    - this service returns list of dict with date and price so its compatible with the time series chart, when i will be using Echarts.
    - tested the method in insomnia(similar to postman) as GET method on the 
    url http://localhost:8000/api/etf-prices.

# Thinking to change the architecture
- I am thinking to create a local db to store the etf data and prices data so i can show the data is persistent and not just in memory.
- I can use  sqlite for the local db from sqlalchemy. So when the user parses the etf file, i can store it in the db and use it for the constituents and etf prices endpoints this way i can use queries to get the data.

1. Update the backend structure to include a new database file that creates the models of the etf and prices data.
- Update the etf_service to use the database instead of static data.

the serivce can now be divided into smaller files now that they don't have to relay on the static data
stored in the global var. If i create a db then i can move those static data in to the db.

The main reason for this change is to show my understanding the database in the full stack app even though there may not be high usage in the project. Also help me answer the indexing interview question i was asked in the tech interview. 
For example i indexed the date so it essentiall create a b-tree to make the query faster. For example we have 2 endpoints that requires calculations on the last price of the ETF, since we have it indexed the query will just need to get the max date and return the price. otherwise it would have to traverse the whole table to find the max date.

2. Implemented the final endpoint for the bar chart
    - created a final get method that returns the top holdings of the ETF
    - also tested this method in insomnia(similar to postman) as GET method on the url http://localhost:8000/api/top-holdings













