import React, { useEffect, useState } from 'react';
import TimeSeriesLineChart from '../../components/TimeSeriesLineChart';
import KoreanTimeConverter from '../KoreanTimeConverter';
import TimeConverter from '../TimeConverterSeconds';

//Graph an average value across days or months
const TimeSeriesGraphAverage = ({timeSeriesData , timeSpan, time_Config }) => {
    const [timeData, setTimeData] = useState([]);
    const [timeConfig, setTimeConfig] = useState({});

    useEffect(() => {
        const processData = () => { 
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

                    var duration = TimeConverter(currentTime.duration)
                    var emotionalTension = currentTime.emotionTension

                    acc = acc + (emotionalTension * duration)
                  
                    divider = divider + duration
                 
                    //While the timestamps lie in the smae timespan i.e same day or month
                    while (nextIndex < timeSeriesData.length && KoreanTimeConverter(timeSeriesData[nextIndex].startTime, timeSpan) === KoreanTimeConverter(currentTime.startTime, timeSpan)) {
                        //Convert duration into seconds so it can be multiplied  
                        duration = TimeConverter(timeSeriesData[nextIndex].duration)
                        emotionalTension = timeSeriesData[nextIndex].emotionTension
                        
                        //Multiply the emotional tension by duration to get an accurate time span of the duration of the value
                        acc = acc + (emotionalTension * duration)

                        
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

  }, [timeSeriesData, timeConfig ]); // Whne timeSeriesData and timeConfig is updated
    

    return(
        <div>
            <TimeSeriesLineChart timeData={timeData} timeConfig ={timeConfig}/>
        </div>
    );
    
    
    };
  
  export default TimeSeriesGraphAverage;