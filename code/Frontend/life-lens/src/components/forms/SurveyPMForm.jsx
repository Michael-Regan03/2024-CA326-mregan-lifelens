import React, { useEffect, useState } from 'react';
import loadData from '../../loaders/loadData';
import { useNavigate } from 'react-router-dom';


const SurveyPMForm = () => {
    const [days, setDays] = useState([]);
    const nav = useNavigate();
    
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedEmotion, setSelectedEmotion] = useState('');
    const [selectedStress, setSelectedStress] = useState('');
    const [selectedFatigue, setSelectedFatigue] = useState('');
    
    const [selectedCaffeine, setSelectedCaffeine,] = useState('');
    const [selectedCAmount, setSelectedCAmount] = useState(0);
    const [selectedAlcohol, setSelectedAlcohol] = useState('');
    const [selectedAAmount, setselectedAAmount] = useState(0);
    
    // https://www.alcoholrehabguide.org/alcohol/types/
   const alcoholType = {
        1: "Beer",
        2: "Wine",
        3: "Hard Cider",
        4: "Mead",
        5: "Sake",
        6: "Gin",
        7: "Brandy",
        8: "Whiskey",
        9: "Rum",
        10: "Tequilla",
        11: "Vodka",   
   }

    const emotion = {
        1: 'Very unpleasant',
        2: 'Unpleasant', 
        3: 'Moderate', 
        4: 'Pleasant' , 
        5: 'Very pleasant'
    }

    const Stress_Fatigue = {
        1: 'Very much', 
        2: 'Fairly', 
        3: 'As usual', 
        4: 'Not much', 
        5: 'Not at all'
    }    
    

    useEffect( () => {
        const fetchData = async () => {
            try {
                const response = await loadData('http://127.0.0.1:8000/day-without-survey/', 'POST', { meridiemIndicator: "pm" });
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
  
  

  const renderSelectOptions = (dict) => (
    Object.entries(dict).map(([key, value]) => (
        <option key={key} value={key}>{value}</option>
    )));

const handleSubmit = (event) => {
    event.preventDefault(); //prevent page refreash
    
    if ( selectedDate === '' ||  selectedEmotion === '' || selectedStress === '' || selectedFatigue === '') {
        alert('Missing fields');
        return //break out
    }

    const body = {
        date: selectedDate,
        emotion: selectedEmotion,
        stress: selectedStress,
        fatigue: selectedFatigue,
        caffeine: selectedCaffeine,
        cAmount: selectedCAmount,
        alcohol: selectedAlcohol,
        aAmount: selectedAAmount
    }

    const sendData = async () => {
        try {
            const response = await loadData('http://127.0.0.1:8000/survey-pm-upload/', 'POST', body);
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
                <div >
                    <p>Select a date</p>
                    <select value={selectedDate} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedDate(e.target.value)}}}>
                        <option>Select Date</option>
                        {days.map((item) => ( 
                            
                            <option key={item.date} value={item.date}>
                                {item.date}
                            </option>
                        ))}
                    </select>
                </div>
                <div>
                    <p>How do you feel now?</p>
                    <select value={selectedEmotion} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedEmotion(e.target.value)}else{ setSelectedEmotion('')}}}>
                        <option>Select </option>
                        {renderSelectOptions(emotion)}
                    </select>
                </div>
                <div>
                    <p>How stressed are you today?</p>
                    <select value={selectedStress} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedStress(e.target.value)}else{ setSelectedStress('')}}}>
                        <option>Select </option>
                        {renderSelectOptions(Stress_Fatigue)}
                    </select>
                </div>
                <div>
                    <p>How tired are you today? </p>
                    <select value={selectedFatigue} onChange={(e) => { if(e.target.value !== "Select"){ setSelectedFatigue(e.target.value)}else{ setSelectedFatigue('')}}}>
                        <option>Select</option>
                        {renderSelectOptions(Stress_Fatigue)}
                    </select>
                </div>
                <div>
                    <p>Types of beverage cosnsumed today that contains alcohol, if any.. </p>
                    <select value={selectedAlcohol} onChange={(e) => { if(e.target.value !== "No Alcohol"){ setSelectedAlcohol(e.target.value)}else{ setSelectedAlcohol('')}}}>
                        <option>No Alcohol</option>
                        {renderSelectOptions(alcoholType)}
                    </select>
                </div>
                <div>
                    <p>Types of beverages that contains caffeine, if any.</p>
                    <input type="cafinated beverages" onChange={(e) => setSelectedCaffeine(e.target.value)} />
                </div>
                <div>
                    <p>Amount of caffeinated beverages (in ml).</p>
                    <input type="Cafinated beverages in ml" onChange={(e) => setSelectedCAmount(e.target.value)} />
                </div>
       
                <div>
                    <p>Amount of alcoholic beverages (in ml).</p>
                    <input type="alcoholic beverages in ml" onChange={(e) => setselectedAAmount(e.target.value)} />
                </div>
                

                
                <button type="submit">Submit</button>
               
            </form>
        </div>
);
}

export default SurveyPMForm;
