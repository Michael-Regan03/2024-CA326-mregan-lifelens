import React, { useEffect, useState } from 'react';
import loadData from "../../loaders/loadData";
import PieChart from '../Graphs/PieChart';
import AddItemOrUpdateDuration from '../../actions/AddItemOrUpdateDuration';

const GraphGenPie = ({ date, action , labels}) => {
    const [activity, setActivity] = useState([]);
    const [duration, setDuration] = useState([]);
    

    useEffect(() => {
        
        const fetchData = async () => {
            
            try {
                    const response = await loadData('http://127.0.0.1:8000/daily-activity-view/', 'POST', { date: date, action: action });
                    console.log(response)
                    if (response && response.length > 0) {
                        let activities = [];
                        let durations = [];
                        for(const item of response) {
                            //activity/durations must be passed to the func as lists instead of setting hooks as the hooks werent async updating
                           ({activities, durations} = await AddItemOrUpdateDuration(item, activities, durations, action ));
                         } 
                        setActivity(activities);
                        setDuration(durations); 
                 
                } else {
                    console.log("No data:", date);
                }
            } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
    
    }, [date, action]);//runs when date has been updated



    return(
        <div>
            <PieChart activities={activity}
                        durations={duration}
                         title={labels.title}>
            </PieChart>
        </div>
    );
};

export default GraphGenPie;
