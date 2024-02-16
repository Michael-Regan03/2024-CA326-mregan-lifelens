import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import DetermineTimeSpan from '../actions/time_series/DetermineTimeSpan';



const GraphGenEmotionData = ({ date, type }) => {
    const [response, setResponse] = useState({});
    const [Type, setType] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            
            try {
                    const responce = await loadData('http://127.0.0.1:8000/daily-activity-data/', 'POST', { date: date, action: type });
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
        setType(type)
    }, [date]);//runs when date has been updated


    return(
        <div>
            <DetermineTimeSpan timeSeriesData={response} type={Type} />
        </div>
    );
};

export default GraphGenEmotionData;
