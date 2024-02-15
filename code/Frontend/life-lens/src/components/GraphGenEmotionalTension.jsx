import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import DetermineTimeSpan from '../actions/time_series/DetermineTimeSpan';



const GraphGenEmotionalTension = ({ date }) => {
    const [response, setResponse] = useState({});
  

    useEffect(() => {
        const fetchData = async () => {
            
            try {
                    const responce = await loadData('http://127.0.0.1:8000/daily-activity-data/', 'POST', { date: date, action: 'emotionTension' });
                    if (responce && responce.length > 0) {
                  
                        setResponse(responce)

                    } else {
                        console.log("No data:", date);
                    }
                }catch (error) {
                console.error('Failed to load data:', error);
            }
        }
        fetchData();
    
    }, [date]);//runs when date has been updated


    return(
        <div>
            <DetermineTimeSpan timeSeriesData={response} />
        </div>
    );
};

export default GraphGenEmotionalTension;
