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
      <h1>ETF Price Monitor</h1>
      <h2>By: Nihal Patel</h2>

      <FileUpload onUploadSuccess={handleUploadSuccess} />
      {loading && <p>Loading...</p>}
      {dataFound && !loading && (
        <>
          <ConstituentsTable constituents={constituents} />
          <ETFPrices prices={etfPrices} />
          <TopHoldings topHoldings={topHoldings} />
        </>
      )}
    </div>
  );
}

export default App;
