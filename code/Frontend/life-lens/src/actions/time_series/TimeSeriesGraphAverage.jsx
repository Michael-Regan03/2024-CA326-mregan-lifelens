import React, { useEffect, useState } from 'react';
import TimeSeriesLineChart from '../../components/Graphs/TimeSeriesLineChart';
import KoreanTimeConverter from '../KoreanTimeConverter';
import TimeConverterMinutes from '../TimeConverterMinutes';
import getValue from './getValue';

//Graph an average value across days or months
const TimeSeriesGraphAverage = ({timeSeriesData , timeSpan, time_Config, type}) => {
    const [timeData, setTimeData] = useState([]);
    const [timeConfig, setTimeConfig] = useState({});
    const [Type, setType] = useState('');
    

    useEffect(() => {
      setType(type)
    }, [type])

  
    useEffect(() => {
        const processData = async() => { 
            try { 
                const data = [];
        
                var i = 0;
                
                while(i < timeSeriesData.length){
            
                    const currentTime = timeSeriesData[i]
                    
                    //Accumulation of value per second
                    let acc = 0;
                    //Duration in seconds
                    let divider = 0;

                    let nextIndex = i + 1;

                    var duration = TimeConverterMinutes(currentTime.duration)
                    
                    let value = 0;
                    
                    
                    value = await getValue(currentTime, type)
                    

                    
                    acc = acc + (value * duration)
                  
                    divider = divider + duration
                 
                    //While the timestamps lie in the smae timespan i.e same day or month
                    while (nextIndex < timeSeriesData.length && KoreanTimeConverter(timeSeriesData[nextIndex].startTime, timeSpan) === KoreanTimeConverter(currentTime.startTime, timeSpan)) {
                        //Convert duration into seconds so it can be multiplied  
                        duration = TimeConverterMinutes(timeSeriesData[nextIndex].duration)
                        value = await getValue(timeSeriesData[nextIndex], type)




                        //Multiply the emotional tension by duration to get an accurate time span of the duration of the value
                        acc = acc + (value * duration)

                        
                        divider = divider + duration
                        nextIndex++;
                    }

                    //Calulate average value
                    const average = (acc/divider) 
                    
                    //Add data point to be graphed
                    let addTime = {
                        x: KoreanTimeConverter(currentTime.startTime, timeSpan),
                        y: average,
                    };

                    //Add data point to list
                    data.push(addTime);

                 

                i = nextIndex;
            }


            setTimeData(data);

              

      } catch (error) {
        console.error(error);
      }
    };

    processData();

   
    setTimeConfig(time_Config);

    
  }, [timeSeriesData, timeConfig , type]); // When timeSeriesData and timeConfig is updated
    

    return(
        <div>
            <TimeSeriesLineChart timeData={timeData} timeConfig ={timeConfig} title={type}  />
        </div>
    );
    
    
    };
  
  export default TimeSeriesGraphAverage;