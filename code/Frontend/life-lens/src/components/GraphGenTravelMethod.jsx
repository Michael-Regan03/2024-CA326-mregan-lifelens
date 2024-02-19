import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import BarChart from './BarChart';
import AddItemOrUpdateDuration from '../actions/AddItemOrUpdateDuration';

const GraphGenTravelMethod = ({ date }) => {
    const [method, setMethod] = useState([]);
    const [duration, setDuration] = useState([]);
    

    useEffect(() => {
        
        const fetchData = async () => {
            
            try {
                    const response = await loadData('http://127.0.0.1:8000/daily-activity-view/', 'POST', { date: date, action: 'travel' });
                    if (response && response.length > 0) {
                        let activities = ['walk', 'driving', 'taxi', 'peronal-mobility', 'bus', 'train/subway', 'other'];
                        let durations = [0,0,0,0,0,0,0];
                        for(const item of response) {
                            //methods/durations must be passed to the func as lists instead of setting hooks as the hooks werent async updating
                           ({activities, durations} = await AddItemOrUpdateDuration(item, activities, durations, "travel"));
                         } 
                        setMethod(activities);
                        setDuration(durations); 
                 
                } else {
                    console.log("No data:", date);
                }
            } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
    
    }, [date]);//runs when date has been updated



    return(
        <div>
            
            <BarChart activities={method}
                        durations={duration} >
            </BarChart>
        </div>
    );
};

export default GraphGenTravelMethod;
