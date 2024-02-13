import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
Chart.register(ArcElement, Tooltip, Legend);


const PieChart = ({ activities, durations }) => {
    const data = {
        labels: activities,
        datasets: [
            {
                data: durations,
                backgroundColor: [
                    '#87CEFA',
                    '#6A5ACD',
                    '#00008B',
                ],
                hoverBackgroundColor: [
                    '#87CEFA',
                    '#6A5ACD',
                    '#00008B',
                ]
            }
        ]
    };

    return(
        <div>
            <Pie data={data}/>
        </div>
        );
}


export default PieChart;
