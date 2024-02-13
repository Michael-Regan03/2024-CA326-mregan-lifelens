import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import PieChart from './PieChart';


//covert to seconds for pie chart
function timeConverter(timeString) {
    const [hours, minutes, seconds] = timeString.split(':').map(Number);
    return hours * 3600 + minutes * 60 + seconds;
}

const GraphGen = ({ date }) => {
    const [activity, setActivity] = useState([]);
    const [duration, setDuration] = useState([]);
    
    const addItemOrUpdateDuration = async (item, activities, durations) => {
        //Check if the actvity has already present in the list
        const actionIndex = activities.findIndex(act => act === item.action_label);
        //if the activity was had already taken place
        
        const duration = timeConverter(item.duration)
        if (actionIndex !== -1) {
            //add durations
            durations[actionIndex] = durations[actionIndex] + duration;
            return {activities, durations}
        } else {
            activities.push(item.action_label)
            durations.push(duration)
            return {activities, durations}
        }
    };


    useEffect(() => {
        if(date !== "Select Day") {
        const fetchData = async () => {
            try {
                const response = await loadData('http://127.0.0.1:8000/daily-activity-data/', 'POST', { date });
                if (response && response.length > 0) {
                    let activities = [];
                    let durations = [];
                    for(const item of response) {
                        //activity/durations must be passed to the func as lists instead of setting hooks as the hooks werent async updating
                        ({activities, durations} = await addItemOrUpdateDuration(item, activities, durations));
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
    }
    }, [date]);//runs when date has been updated


    useEffect(() => {
        if (date !== "Select Day") {
        }
    }, [activity, duration, date]);
    

    if(date=="Select Day"){
        return(
            <div></div>
        );
    }

    
    return(
        <div>
            {date}
            <PieChart activities={activity}
                        durations={duration} >
            </PieChart>
        </div>
    );
};

export default GraphGen;
