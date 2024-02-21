import React, { useEffect, useState } from 'react';
import loadData from "../../loaders/loadData";
import BarChart from '../Graphs/BarChart';
import AddItemOrUpdateDuration from '../../actions/AddItemOrUpdateDuration';

const GraphGenBarChart = ({ date, action, list, labels }) => {
    const [method, setMethod] = useState([]);
    const [duration, setDuration] = useState([]);
    

    useEffect(() => {
        console.log("TESTING")
        console.log(date)
        const fetchData = async () => {
            
            try {
                    const response = await loadData('http://127.0.0.1:8000/daily-activity-view/', 'POST', { date: date, action: action });
                    console.log(response)
                    if (response && response.length > 0) {
                        let activities = list[0];
                        let durations = list[1];
                        for(const item of response) {
                            //methods/durations must be passed to the func as lists instead of setting hooks as the hooks werent async updating
                           ({activities, durations} = await AddItemOrUpdateDuration(item, activities, durations, action));
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
    
    }, [date, list]);//runs when date has been updated



    return(
        <div>
            <BarChart activities={method}
                        durations={duration}
                        title={labels.title}
                        x_axis={labels.x_axis}
                        y_axis={labels.y_axis} >
            </BarChart>
        </div>
    );
};

export default GraphGenBarChart;
