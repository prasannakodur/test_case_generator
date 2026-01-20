import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setStatus('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setStatus('Uploading and processing file...');
      const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const result = await response.json();
        setStatus(`File processed successfully. Download: ${result.downloadLink}`);
      } else {
        setStatus('Error processing file.');
      }
    } catch (error) {
      setStatus('An error occurred during upload.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AutoTestGen AI</h1>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Upload and Generate Test Cases</button>
        <p>{status}</p>
      </header>
    </div>
  );
}

export default App;