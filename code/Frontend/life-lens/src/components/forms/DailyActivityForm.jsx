import React, { useState } from 'react';
import loadData from '../../loaders/loadData';
import '../../style_components/FileForm.css'
import '../../style_components/Survey.css'
import '../../style_components/FormVerification.css'


function DailyActivityForm() {
    const [file, setFile] = useState(null);
    
    const [loadMessage, setLoadMessage] = useState(false);
    const [message, setMessage] = useState('');
    const [loadError, setLoadError] = useState(false);
    const [error, setError] = useState(null);
    
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = async() => {
        if (!file) {
            alert('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try{
            const response = await loadData('http://127.0.0.1:8000/api/upload-csv/', 'POST', formData)
            console.log(response)
            setLoadError(false)
            setLoadMessage(true)            
            setMessage(response.message)
        }catch(error){
            console.log(error)
            setLoadMessage(false)
            setLoadError(true)
            setError("Failed to send")
        }

    };

    return (
        <div>
            <div className="file-container">
            {/* using label for the file input for styling */}
            <label for="file-upload" className="file-upload">
                Upload a CSV containg the lifelog data spanning across a day
            </label>
            <input  id="file-upload"  className="file-input" type="file" accept=".csv" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload CSV</button>
            </div>

            {loadMessage && <div className="approved-message"> <p>{message}</p> </div>}
            {loadError && <div className="error-message"><p>{error}</p></div>}
        </div>
    );
}

export default DailyActivityForm;
