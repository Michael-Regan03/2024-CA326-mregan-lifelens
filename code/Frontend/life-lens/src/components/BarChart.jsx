import { Bar } from 'react-chartjs-2';


const BarChart = ({ activities, durations }) => {
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
        <div style={{ height: '400px' }} >
            <Bar data={data}/>
        </div>
        );
}


export default BarChart;
