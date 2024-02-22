import React from 'react';
import { Pie } from 'react-chartjs-2';
import '../../style_components/Graph.css'




const PieChart = ({ activities, durations, title }) => {
    
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

     const options = {
        maintainAspectRatio: false , //fits page
        plugins: {
            title: {
                display: true,
                text: title, // Set the title
                font: {
                    size: 30 // Styling
                }
            }
    }}

    return(
        <div className="pie-chart" >
            <Pie data={data} options={options}/>
        </div>
        );
}


export default PieChart;
