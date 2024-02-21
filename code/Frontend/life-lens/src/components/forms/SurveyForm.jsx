import React, { useEffect, useState } from 'react';
import SurveyAMForm from './SurveyAMForm';
import SurveyPMForm from './SurveyPMForm';
import '../../style_components/Survey.css'



function SurveyForm() {
    const [meridiemIndicator, setMeridiemIndicator] = useState(null);
    

    const handleChange = (event) => {
        if(event.target.value != "Select"){
            setMeridiemIndicator(event.target.value);
        }
    };

    return (
        <div>
            <h2 className="form-header" >Select a Survey</h2>
            <select onChange={handleChange} >
            <option>Select</option>
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
