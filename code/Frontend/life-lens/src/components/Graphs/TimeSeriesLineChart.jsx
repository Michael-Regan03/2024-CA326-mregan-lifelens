import React from 'react';
import { Line } from 'react-chartjs-2'; // https://www.chartjs.org/docs/latest/charts/line.html
import 'chart.js/auto';
//import '../style_components/Graph.css'
import 'chartjs-adapter-moment';

const TimeSeriesLineChart = ({ timeData, timeConfig, title}) => {
    

    const data = {
        datasets: [
            {
                data: timeData,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1 //Slight curve
            }
        ]
    };

    const options = {
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: title, // Set the title
                font: {
                    size: 30 // Styling
                }
            },
            legend: {
                display: false, //Legend doesnt make sence for bar chart
            },
        },
        scales: {
            x: {
                type: 'time',
                time: timeConfig  ,
                title: {
                    display: true,
                    text: timeConfig.unit,
                    font: {
                        size: 10  // Styling
                    }
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
                    text: title ,
                    font: {
                        size: 10  // Styling
                    }
                }
            }
        },
        maintainAspectRatio: false //fits page
    };

  
    return (
        <div className="timeSeriesGraph"> 
            <Line data={data} options={options} />
        </div>
    );
};

export default TimeSeriesLineChart;