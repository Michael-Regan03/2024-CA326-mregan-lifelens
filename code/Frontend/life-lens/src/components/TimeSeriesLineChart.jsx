import React from 'react';
import { Line } from 'react-chartjs-2'; // https://www.chartjs.org/docs/latest/charts/line.html
import 'chart.js/auto';
import 'chartjs-adapter-moment'; 


const TimeSeriesLineChart = ({ timeData, timeConfig}) => {
    
    const data = {
        datasets: [
            {
                label: '"Emotional Tension"',
                data: timeData,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1 //Slight curve
            }
        ]
    };

    const options = {
        scales: {
            x: {
                type: 'time',
                time: timeConfig  ,
                title: {
                    display: true,
                    text: 'Time'
                }
            },
            y: {
                beginAtZero: true,  //y axis starts at zero 
            ticks: {
                //The value range
                min: 0, 
                max: 7, 
            },
                title: {
                    display: true,
                    text: 'Emotional Tension'
                }
            }
        },
        maintainAspectRatio: false //fits page
    };

    return (
        <div style={{ height: '400px' }}> {/* Temp styling as graph was to small during testing */}
            <Line data={data} options={options} />
        </div>
    );
};

export default TimeSeriesLineChart;