import React, { useEffect, useState } from 'react';
import loadData from '../../loaders/loadData';
import { useNavigate } from 'react-router-dom';
import renderSelectOptions from '../../actions/renderSelectOptions';


const SurveyAMForm = () => {
    const [days, setDays] = useState([]);
    const nav = useNavigate();
    
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedSleep, setSelectedSleep] = useState('');
    const [selectedSleepProblem, setSelectedSleepProblem] = useState('');
    const [selectedDream, setSelectedDream] = useState('');
    const [selectedCondition, setSelectedCondition] = useState('');
    const [selectedEmotion, setSelectedEmotion] = useState('');

    const sleep = {
        1: 'Not at all',
        2: 'Not much',
        3: 'Moderately',
        4: 'Fairly',
        5: 'Fully',
    };
    
    const sleepProblem = {
        1: 'It took more than 30 minutes to fall asleep.',
        2: 'I was awake during the night or prior to my scheduled wake time.',
        3: 'I was awake during the night to go to the bathroom.',
        4: 'I snored loudly during the sleep or woke up during the night choking.',
        5: 'I was disturbed by the low temperature during sleep.',
        6: 'I was disturbed by the high temperature during sleep.',
        7: 'I had nightmares.',
        8: 'I was disturbed by the pain.',
        9: 'I was disturbed by other reasons not listed above.',
        0: 'I did not have any problems.',
    }
    

    const dream = {
        1: 'Nightmare',
        2: 'Neutral dream',
        3: 'Nice dream',
        4: 'None'
    }
    

    const condition = {
        1: 'Not at all' , 
        2: 'Not much', 
        3: 'Moderately',
        4: 'Fairly',
        5: 'Fully'
    }
    

    const emotion = {
        1: 'Very unpleasant',
        2: 'Unpleasant', 
        3: 'Moderate', 
        4: 'Pleasant' , 
        5: 'Very pleasant'
    }
    

    useEffect( () => {
        const fetchData = async () => {
            try {
                const response = await loadData('http://127.0.0.1:8000/day-without-survey/', 'POST', { meridiemIndicator: "am" });
                if (response && response.length > 0) {
                    setDays(response);
            } else {
                console.log("No data:",);
            }
        } catch (error) {
            console.error('Failed to load data:', error);
        }
    };
    fetchData();

    },[]) 
  
  



const handleSubmit = (event) => {
    event.preventDefault(); //prevent page refreash
    
    if ( selectedDate === '' ||  selectedSleep === '' || selectedSleepProblem === '' || selectedDream === '' || selectedCondition === ''|| selectedEmotion === '') {
        alert('Missing fields');
        return //break out
    }

    const body = {
        date: selectedDate,
        sleep: selectedSleep,
        sleepProblem: selectedSleepProblem,
        dream: selectedDream,
        condition: selectedCondition,
        emotion: selectedEmotion
    }

    const sendData = async () => {
        try {
            const response = await loadData('http://127.0.0.1:8000/survey-am-upload/', 'POST', body);
            //redirect to homepage
            //ensures that the same day isnt submitted twice
            nav('/');
        }catch (error) {
        console.error('Failed to post data:', error);
    }};

    sendData();

};

return (
        <div>
            <form onSubmit={handleSubmit}>
                <label >
                    <p>Select a date</p>
                    <select value={selectedDate} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedDate(e.target.value)}}}>
                        <option>Select Date</option>
                        {days.map((item) => ( 
                            
                            <option key={item.date} value={item.date}>
                                {item.date}
                            </option>
                        ))}
                    </select>
                </label>
                <label>
                    <p>Are you satisfied with your sleep?</p>
                    <select value={selectedSleep} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedSleep(e.target.value)}else{ setSelectedSleep('')}}}>
                        <option>Select </option>
                        {renderSelectOptions(sleep)}
                    </select>
                </label>
                <label>
                    <p>Did you have problems during sleep?</p>
                    <select value={selectedSleepProblem} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedSleepProblem(e.target.value)}else{ setSelectedSleepProblem('')}}}>
                        <option>Select</option>
                        {renderSelectOptions(sleepProblem)}
                    </select>
                </label>
                <label>
                    <p>Did you have a dream?</p>
                    <select value={selectedDream} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedDream(e.target.value)}else{ setSelectedDream('')}}}>
                        <option>Select</option>
                        {renderSelectOptions(dream)}
                    </select>
                </label>
                <label>
                    <p>Do you feel refreshed after awakening?</p>
                    <select value={selectedCondition} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedCondition(e.target.value)}else{ setSelectedCondition('')}}}>
                        <option>Select</option>
                        {renderSelectOptions(condition)}
                    </select>
                </label>
                <label>
                    <p>How do you feel after awakening?</p>
                    <select value={selectedEmotion} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedEmotion(e.target.value)}else{ setSelectedEmotion('')}}}>
                        <option>Select</option>
                        {renderSelectOptions(emotion)}
                    </select>
                </label>
                <button type="submit">Submit</button>
               
            </form>
        </div>
);
}

export default SurveyAMForm;


