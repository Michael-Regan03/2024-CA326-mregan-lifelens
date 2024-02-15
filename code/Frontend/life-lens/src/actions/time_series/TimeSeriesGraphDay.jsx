import React, { useEffect, useState } from 'react';
import TimeSeriesLineChart from '../../components/TimeSeriesLineChart';
import KoreanTimeConverter from '../KoreanTimeConverter';

//Graph time data across a day
const TimeSeriesGraphDay = ({timeSeriesData}) => {
    const [timeData, setTimeData] = useState([]);
    const [timeConfig, setTimeConfig] = useState({});

    useEffect(() => {
        const processData = () => { 
            try { 
                const data = [];
        
                var i = 0;
                
                while(i < timeSeriesData.length){
            
                    const currentTime = timeSeriesData[i]
                    
                    //Create the first Data point on the graph
                    let addTime = {
                        x: KoreanTimeConverter(currentTime.startTime, "date"),
                        y: currentTime.emotionTension,
                    };
                    data.push(addTime);

                    let nextIndex = i + 1;
                    //Iterate through timestamps until one has a diffent value
                    while (nextIndex < timeSeriesData.length && timeSeriesData[nextIndex].emotionTension === currentTime.emotionTension) {
                      nextIndex++;
                    }

                i = nextIndex;
            }


            setTimeData(data);
      } catch (error) {
        console.error(error);
      }
    };

    processData();

    //Time config for a day of data
    const time_Config = {
        parser: 'YYYY-MM-DD HH:mm',
        tooltipFormat: 'll HH:mm',
        unit: 'hour',
        displayFormats: {
            hour: 'HH:mm'
        }
    }

    setTimeConfig(time_Config);
    
  }, [timeSeriesData]); //When timeSeriesData is refreashed
    
 
    return(
        <div>
            <TimeSeriesLineChart timeData={timeData} timeConfig={timeConfig} />
        </div>
    );
    
    
    };
  
  export default TimeSeriesGraphDay;