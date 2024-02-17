import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import BarChart from './BarChart';
import AddItemOrUpdateDuration from '../actions/AddItemOrUpdateDuration';
import FetchComp from '../actions/FetchComp';
import RiskView from './RiskView';

function ChronicIllnessRiskAssesment() {
    const [age, setAge] = useState('');
       
    const [formatedData, setFormatedData] = useState('');

    const [riskAssesment, setRiskAssessment] = useState({});

    const [body, setBody] = useState({});

    const [lowRisk, setLowRisk] = useState([]);
    const [midRisk, setMidRisk] = useState([]);
    const [highRisk, setHigRisk] = useState([]);

    useEffect(() => {
        
        const fetchData = async () => {
            
            try {
                    const response = await loadData('http://127.0.0.1:8000/chronic-illness-parameters-view/', 'GET');
                    
                    const bodyConfig =  {"sleepAverage": response.sleepAverage,
                                        "alcoholAverageAprox": response.alcoholAverageAprox, 
                                        "activeTimeAverage" : response.activeTimeAverage, 
                                        "smokingStatus" : response.smokingStatus}
                    
                    console.log(response)
                    setAge(response.age)
                    setBody(bodyConfig)

            } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
    
    }, []);

    useEffect(() => {
        
        const fetchData = async () => {
            
            try {
                    const response = await loadData('http://127.0.0.1:8000/chronic-illness-formated-view/', 'POST', body );
                    console.log(response)
                    setFormatedData(String(response.output))
            } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
    
    }, [body]);

    useEffect(() => {
        console.log("TESTING")
        console.log(formatedData)
        const fetchData = async () => {
            
            try {
                    const response = await FetchComp('http://127.0.0.1:5000/riskassessment', {"behaviours":formatedData}, 'POST');
                    //if(responce.)
                    console.log(typeof response);
                    const low_risk = []
                    const mid_risk = []
                    const high_risk = []
                    console.log(response)
                    for (const [condition, risk] of Object.entries(response)) {
                        //Divide by risk so that they can be rendered from high - low risk on web page
                        console.log(risk)
                        if (risk == "low-risk"){
                            low_risk.push(condition)
                        }else  if (risk == "mid-risk"){
                            mid_risk.push(condition)
                        }else  if (risk == "high-risk"){
                            high_risk.push(condition)
                        }                        
                    }
                    
                    setLowRisk(low_risk)
                    setMidRisk(mid_risk)
                    setHigRisk(high_risk)
                    
                    
                    console.log(response)
                } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
    
    }, [formatedData]);

    return(
        <div>
            <div>
                <p>The models risk assesment is based off of this data about you:</p>
                <p>Your age: {age}</p>
                <p>Your average sleep per day: {body.sleepAverage} hours</p>
                <p>Your average alcohol consumption per day: {body.alcoholAverageAprox} ml</p>
                <p>Your average time being active per day: {body.activeTimeAverage} minutes</p>
                <p>Your smoking status: {body.smokingStatus}</p>
            </div>
            <div>
            {highRisk.map((illness) => (
                <RiskView Illness={illness} risk={"High Risk"}  />
                ))}
            {midRisk.map((illness) => (
                <RiskView Illness={illness} risk={"Mid Risk"}  />
                ))}
            {lowRisk.map((illness) => (
                <RiskView Illness={illness} risk={"Low Risk"}  />
                ))}
                 
            </div>
        </div>
    );
};

export default ChronicIllnessRiskAssesment;
