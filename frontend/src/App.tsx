import React, { useState } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';

function App() {
  const[dataFound, setDataFound] = useState(false);

  const handleUploadSuccess = () => {
    setDataFound(true);
    console.log('Data found');
  }

  return (


    <div className="App">
      <h1>ETF Price Monitor</h1>
      <h2>By: Nihal Patel</h2>

      <FileUpload onUploadSuccess={handleUploadSuccess} />

      {dataFound && <p>Data loaded successfully</p>}


    </div>
  );
}

export default App;
