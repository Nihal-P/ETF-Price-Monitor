## ETF Price Monitor

- Allows traders to view historical prices for a given ETF and its top holdings.
- Once the users uploads a ETF csv file, the application will display the constituents table, the ETF prices chart, and the top holdings chart.

# Tech Stack

- Backend: Python, FastAPI, SQLAlchemy, Pandas, SQLite
- Frontend: React, TypeScript, AG Grid, ECharts, Bootstrap CSS
- Containerization: Docker, Docker Compose
Video Walkthrough:


# Pre-requisites

- Install docker Desktop
  - includes docker and docker compose

# Setup Instructions

1. Clone the repository
2. Navigate to the root directory
   - `cd ETF-Price-Monitor`
3. Run `docker-compose up --build`

4. Application URLs

   - Access the application at http://localhost:3000
   - Access the API at http://localhost:8000/
   - Access the API docs at http://localhost:8000/docs

5. Stop the containers
   - `docker-compose down -v`

Alternative Setup Instructions

1. Start backend:
```
# Navigate to backend directory

`cd backend`

# Create virtual environment

`python -m venv venv`

# Activate virtual environment

# macOS/Linux:

`source venv/bin/activate`

# Windows:

`venv\Scripts\activate`

# Install dependencies

`pip install -r requirements.txt`

# Start backend server

`uvicorn main:app --reload`
```
2. Start Frontend
```
# Navigate to frontend directory

`cd frontend`

# Install dependencies

`npm install`

# Start development server

`npm start`
```

## Project Structure

Used https://project-tree-generator.netlify.app/generate-tree to create the strucutre

```
ETF-Price-Monitor/
├── backend/                                            # Backend directory
│   ├── .dockerignore
│   ├── .gitignore
│   ├── api/                                            # API endpoints
│   │   ├── __init__.py
│   │   ├── get_constituents.py
│   │   ├── get_etf_prices.py
│   │   ├── get_top_holdings.py
│   │   └── upload_etf.py
│   ├── data/.                                         # Price Data CSV file
│   │   └── bankofmontreal-e134q-1arsjzss-prices.csv
│   ├── database/                                      # SQLite database created on startup
│   │   ├── database.py
│   │   └── load_prices.py
│   ├── Dockerfile
│   ├── main.py                                        # Main FastAPI entry point
│   ├── requirements.txt                               # Backend dependencies
│   └── services/                                      # Backend services called by API endpoints
│       ├── calculate_etf_price.py
│       ├── calculate_top_holdings.py
│       ├── retrieve_constituents.py
│       └── upload_etf_to_db.py
├── bankofmontreal-e134q-5osaq2zk-ETF1.csv
├── bankofmontreal-e134q-tf6omf1g-ETF2.csv
├── docker-compose.yml
├── frontend/                                          # Frontend directory
│   ├── .dockerignore
│   ├── .gitignore
│   ├── Dockerfile
│   ├── package-lock.json
│   ├── package.json
│   ├── public/
│   ├── README.md
│   ├── src/
│   │   ├── App.css
│   │   ├── App.tsx                                    # Main React component
│   │   ├── components/.                               # React components
│   │   │   ├── ConstituentsTable.tsx
│   │   │   ├── ETFPrices.tsx
│   │   │   ├── FileUpload.tsx
│   │   │   └── TopHoldings.tsx
│   │   ├── services/.                                 # API services called by React components
│   │   │   └── api.ts
│   └── tsconfig.json
├── LogJournal.md
└── README.md
```

## ASSUMPTIONS MADE:

1. The prices csv file will be the only one that will be used and assume will be compatible with the ETF file provided by a user.
2. All constituents in the uploaded ETF CSV files (ETF1.csv, ETF2.csv) have corresponding price data in the prices CSV.
3. State Management
   - No Redux or global state management library is needed since each component fetches its own data from its dedicated API endpoints.
   - since Data is not shared or manipulated across multiple components, so prop drilling from App.tsx is sufficient.
   - Redux should be used if the data is shared or manipulated across multiple components.
4. Database Design
   - I started of using a global varibale in one service to store the ETF data and use it in the other services.
   - But to demonstarted database usage, i used sqlite and sqlalchemy to store the ETF data in a database. To also show that the data is persistent and not just in memory.
   - I learned about indexing after the interview to demonstarte the feedback and to improve my queries.
5. Backend
   - Python with FastAPI chosen for data processing capabilities so i can also use Pandas for data processing.
6. Frontend
   - AG Grid Community Edition (free) used for interactive table with pagination.
   - I used ECharts for the rest of thecharts due to built-in zoom functionality (AG Grid zoom requires enterprise license)
   - Bootstrap CSS used for styling instead of Tailwind CSS to avoid complex setup.


## ========== Assignment ==========


Full Stack Developer Interview
This is an interview for the full stack data developer role at BMO Capital Markets' Data Cognition Team.

Requirements

Design a single page web application (actually a single page!) that allows traders to view historical prices for a given ETF and its top holdings.

The frontend should be written in a front end framework such as Angular, React, Vue or any other framework that you feel comfortable.

The backend can be anything you want. We primarily use Python but you're free to pick whatever you like.

Partial solutions are acceptable. It is not necessary to submit a complete solution that implements every requirement.

Quick introduction to ETFs

ETFs (Exchange Traded Funds) are traded securities that hold a basket of securities; the securities could be stocks, bonds, or even other ETFs!

In general, the price of the ETF at any time can be computed by doing a weighted sum of the price of each individual constituent and we'll be assuming

that the weights are not changing over time in this challenge.

Data provided

We've provided all the data you need to complete the challenge. You don't need to contact any public external API.

We've provided:

`ETF1.csv` and `ETF2.csv` containing the constituents and their weights in each ETF
`prices.csv` which contains the historical price data for all the constituents. Note that this file contains prices for all constituents

Functionality

Upload a `.csv` file containing weights of a given ETF, `ETF1.csv` or `ETF2.csv`
An interactive table similar to the uploaded `ETF[1-2].csv` file on the webpage that displays three columns
The constituent name, i.e., A
The weight, i.e., 0.02
The most recent close price of the constituent, i.e., $20.05 for A
A zoomable time series plot of the reconstructed price of the ETF. The price of the ETF is calculated as the weighted sum of the individual prices
A bar chart displaying the top 5 biggest holdings in the ETF as of the latest market close. You can compute the holding size of each constituent by multiplying the weight and the price

Challenge Scope

High level description of design and technologies used
Document all assumptions made
Complete solutions aren't required, but what you do submit needs to run

What are we looking for? What does this prove?

Assumptions you make given limited requirements
Technology and design choices
Identify areas of your strengths
This is not a pass or fail test, this will serve as a common ground that we can deep dive together into specific issues

Submission Guidelines:

Follow a clear project structure and include a README file with summary.
Submit within 4 days and prepare for an in-person review.
