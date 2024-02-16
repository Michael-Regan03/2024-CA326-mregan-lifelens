import React, { useEffect, useState } from 'react';
import TimeSeriesLineChart from '../../components/TimeSeriesLineChart';
import KoreanTimeConverter from '../KoreanTimeConverter';
import getValue from './getValue';

//Graph time data across a day
const TimeSeriesGraphDay = ({timeSeriesData, type }) => {
    const [timeData, setTimeData] = useState([]);
    const [timeConfig, setTimeConfig] = useState({});
    const [Type, setType] = useState('');
    
    var i = 0;
    let currentValue ;
    let nextValue ;
    let addTime = {};

    useEffect(() => {
      setType(type)
    }, [type])

    useEffect(() => {
        const processData = async() => { 
            try { 
                const data = [];
        
            
                
                console.log(timeSeriesData)
                while(i < timeSeriesData.length){

                    const currentTime = timeSeriesData[i]
                    
                    //Create the first Data point on the graph
                    

                    currentValue = await getValue(currentTime, Type);

                    addTime = {
                        x: KoreanTimeConverter(currentTime.startTime, "date"),
                        y: currentValue,
                    };

                    data.push(addTime);

                    let nextIndex = i + 1;
                    //Iterate through timestamps until one has a diffent value

                    
                    if(nextIndex < timeSeriesData.length){
                      nextValue =  await getValue(timeSeriesData[nextIndex], Type);
                    }
                    while (nextIndex < timeSeriesData.length && nextValue === currentValue) {
                      nextIndex++;
                      if(nextIndex < timeSeriesData.length){
                        nextValue =  await getValue(timeSeriesData[nextIndex], Type);
                      }
                    }

                

                i = nextIndex;
            }

            //For instances where the value is consistant across the timeSpan
            if(data.length == 1){
              nextValue =  await getValue(timeSeriesData[i-1], Type);
              addTime = {
                x: KoreanTimeConverter(timeSeriesData[i-1].endTime, "date"),
                y: nextValue,
              };
              data.push(addTime)
            }

            console.log(data)


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
    
  }, [timeSeriesData, Type]); //When timeSeriesData is refreashed
    
 
    return(
        <div>
            <TimeSeriesLineChart timeData={timeData} timeConfig={timeConfig} />
        </div>
    );
    
    
    };
  
  export default TimeSeriesGraphDay;