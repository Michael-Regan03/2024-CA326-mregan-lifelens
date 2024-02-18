import React, { useState } from 'react';
import loadData from '../loaders/loadData';
import Header from './Header';
import '../style_components/FileForm.css'
import '../style_components/Survey.css'

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
            <Header></Header>
            <div className="file-container">
            {/* using label for the file input for styling */}
            <label for="file-upload" className="file-upload">
                Upload a CSV containg the lifelog data spanning across a day
            </label>
            <input  id="file-upload"  className="file-input" type="file" accept=".csv" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload CSV</button>
            </div>
        </div>
    );
}

export default DailyActivityForm;
