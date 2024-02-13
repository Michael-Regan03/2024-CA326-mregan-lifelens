import React, { useState } from 'react';
import loadData from '../loaders/loadData';

function DailyActivityForm() {
    const [file, setFile] = useState(null);
    
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = () => {
        if (!file) {
            alert('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        loadData('http://127.0.0.1:8000/api/upload-csv/', 'POST', formData)


    };

    return (
        <div>
            <input type="file" accept=".csv" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload CSV</button>
        </div>
    );
}

export default DailyActivityForm;
