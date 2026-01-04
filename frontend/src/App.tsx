import React, { useState } from "react";
import "./App.css";
import FileUpload from "./components/FileUpload";
import ConstituentsTable from "./components/ConstituentsTable";
import ETFPrices from "./components/ETFPrices";
import TopHoldings from "./components/TopHoldings";
import { getConstituents, getEtfPrices, getTopHoldings } from "./services/api";

function App() {
  const [dataFound, setDataFound] = useState(false);
  const [loading, setLoading] = useState(false);

  // store the data from the api calls
  const [constituents, setConstituents] = useState([]);
  const [etfPrices, setEtfPrices] = useState([]);
  const [topHoldings, setTopHoldings] = useState([]);

  const handleUploadSuccess = async () => {
    setDataFound(true);
    console.log("Data found");
    setLoading(true);

    try {
      // const constituentsRes = await getConstituents();
      // const etfPricesRes= await getEtfPrices();
      // const topHoldingsRes = await getTopHoldings();
      // run all the get call promises at the same time
      const [constituentsRes, pricesRes, holdingsRes] = await Promise.all([
        getConstituents(),
        getEtfPrices(),
        getTopHoldings(),
      ]);

      setConstituents(constituentsRes.data);
      setEtfPrices(pricesRes.data);
      setTopHoldings(holdingsRes.data);

      console.log("Constituents: ", constituentsRes.data);
      console.log("ETF Prices: ", pricesRes.data);
      console.log("Top Holdings: ", holdingsRes.data);
    } catch (error) {
      console.error("Error fetching data: ", error);
      alert("Failed to load data. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // once the csv is uploaded, the dashboard components will be mounted with their perpective data
  // passed as props
  return (
    <div className="App">
      <div className="container-fluid p-4">
        {/* header */}
        <div className="bg-dark rounded-3 p-4 mb-4 shadow">
          <h1 className="text-white fw-bold mb-2">ETF Price Monitor</h1>
          <p className="text-secondary mb-3">By: Nihal Patel</p>
          <FileUpload onUploadSuccess={handleUploadSuccess} />
        </div>
        {/* loading State */}
        {loading && (
          <div className="text-center text-secondary py-5">
            <div className="spinner-border text-primary me-2" role="status">
              <span className="visually-hidden">Loading...</span>
            </div>
            Loading dashboard...
          </div>
        )}
        {/* dashboard */}
        {dataFound && !loading && (
          <div>
            <div className="row g-4 mb-4">
              <div className="col-lg-7  ">
                <div className="bg-light rounded-3 shadow pb-4">
                  <ConstituentsTable constituents={constituents} />
                </div>
              </div>
              <div className="col-lg-5">
                <div className="bg-light rounded-3 p-4 shadow">
                  <TopHoldings topHoldings={topHoldings} />
                </div>
              </div>
            </div>
            <div className="row g-4">
              <div className="col-12">
                <div className="bg-light rounded-3 p-4 shadow">
                  <ETFPrices prices={etfPrices} />
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
