import React, { useEffect, useState } from 'react';
import SurveyAMForm from './forms/SurveyAMForm';
import SurveyPMForm from './forms/SurveyPMForm';

function SurveyForm() {
    const [meridiemIndicator, setMeridiemIndicator] = useState(null);
    

    const handleChange = (event) => {
        setMeridiemIndicator(event.target.value);
    };

    return (
        <div>
            <h1>Select a form</h1>
            <select onChange={handleChange} >
            <option>pm</option>
            <option>am</option> 
            </select>
            
            {meridiemIndicator === "am" && (
               <div>
                    <SurveyAMForm ></SurveyAMForm>
               </div>
            )}
            {meridiemIndicator === "pm"  && (
              <div>
                    <SurveyPMForm></SurveyPMForm>
               </div>
            )}



        </div>
    );
}

export default SurveyForm;
