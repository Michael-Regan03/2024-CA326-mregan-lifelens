import React, { useEffect, useState } from 'react';
import loadData from "../loaders/loadData";
import BarChart from './BarChart';
import AddItemOrUpdateDuration from '../actions/AddItemOrUpdateDuration';

const RiskView = ({ Illness, risk }) => {
    const [Name, setName] = useState('');
    const [url, setUrl] = useState('');
    const [description, seDescription] = useState('');
    const [risklevel, setRiskLevel] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            
            try {
                const response = await loadData('http://127.0.0.1:8000/illness-description-view/', 'POST', { shortCode: Illness  });
                setName(response.name)
                setUrl(response.url)
                seDescription(response.description)
            } catch (error) {
                console.error('Failed to load data:', error);
            }
        };
        fetchData();
        setRiskLevel(risk)
    }, [Illness, risk]);//runs when date has been updated



    return(
        <div>
            <h2>{Name}: {risklevel}</h2>
            <p>{description}</p>
            <p> find out more <a href={url}>here</a></p>
        </div>
    );
};

export default RiskView;
