import { Bar } from 'react-chartjs-2';
import '../../style_components/Graph.css'



const BarChart = ({ activities, durations, title, x_axis, y_axis }) => {
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
            //axis
            x: {
                title: {
                    display: true,
                    text: x_axis, // X-axis label
                    font: {
                        size: 10  // Styling
                    }
                }
            },
            // Y axis
            y: {
                title: {
                    display: true,
                    text: y_axis , // Y-axis label
                    font: {
                        size: 10 // Styling
                    }
                }
            }
        }
    };

    return(
        <div className="bar-chart" >
            <Bar data={data} options={options}/>
        </div>
        );
}


export default BarChart;
