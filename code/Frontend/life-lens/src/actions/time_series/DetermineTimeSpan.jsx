import React, { useEffect, useState } from 'react';
import KoreanTimeConverter from '../KoreanTimeConverter';
import TimeSeriesGraphDay from './TimeSeriesGraphDay';
import TimeSeriesGraphAverage from './TimeSeriesGraphAverage';



const DetermineTimeSpan = ({ timeSeriesData, type }) => {
    const [timeData, setTimeData] = useState([]);
    const [Type, setType] = useState('');
    

    const [startDay, setStartDay] = useState(null);
    const [endDay, setEndDay] = useState(null);
    const [startMonth, setStartMonth] = useState(null);
    const [endMonth, setEndMonth ] = useState(null);
    const [startYear, setStartYear] = useState(null);
    const [endYear, setEndYear] = useState(null);

    const [timeSpan, setTimeSpan] = useState('');
    const [timeConfig, setTimeConfig] = useState('');


    useEffect(() => {
        setTimeData(timeSeriesData)
    }, [timeSeriesData])

    useEffect(() => {
        setType(type)
    }, [type])

    useEffect(()=>{
        if (timeData.length > 0) {
            //Calulate start date of timeData
            const startTime = timeData[0].startTime;
            //Javascript doesnt have negitive indexing
            //Calulate end date of timeData
            const endTime = timeData[timeData.length - 1].endTime;
            

            //Calculate start day and end day values to detrmine the time range the timestamps lie in
            setStartDay(KoreanTimeConverter(startTime, "yearMonthDay"));
            setEndDay(KoreanTimeConverter(endTime, "yearMonthDay"));
            setStartMonth(KoreanTimeConverter(startTime, "yearMonth"));
            setEndMonth( KoreanTimeConverter(endTime, "yearMonth"));
            setStartYear(KoreanTimeConverter(startTime, "year"));
            setEndYear(KoreanTimeConverter(endTime, "year"));
        }
    },[timeData])//Call when timeData is updated
    
    useEffect(()=>{
    
    var time_Config = {}
    
    //Compare dates to find time span of data points
    if(startDay === endDay){
        setTimeSpan("day")
    }else if(startMonth === endMonth){
        setTimeSpan("month")

        //Configuration for grapghing average values across a month
        time_Config = {
            parser: 'YYYY-MM-DD',
            tooltipFormat: 'DD MMM YYYY',
            unit: 'day',
            displayFormats: {
                day: 'DD MMM YYYY'
            }
        }

        setTimeConfig(time_Config)


    }else if(startYear === endYear){
        setTimeSpan("year")

        //Configuration for grapghing average values across a year
        time_Config = {
            parser: 'YYYY-MM',
            tooltipFormat: 'MMM YYYY',
            unit: 'month',
            displayFormats: {
                month: 'MMM YYYY'
            }
        }

        setTimeConfig(time_Config)


    }
    },[startDay, endDay, startMonth, endMonth, startYear, endYear  ])


    return (
        <div>
            {timeSpan === "day" && (
                <TimeSeriesGraphDay timeSeriesData={timeData} type={type} />
            )}
            {timeSpan === "month"  && (
                <TimeSeriesGraphAverage timeSeriesData={timeData} timeSpan={"yearMonthDay"} time_Config={timeConfig} type={Type} />
            )}
            {timeSpan === "year"  && (
                <TimeSeriesGraphAverage timeSeriesData={timeData} timeSpan={"yearMonth"} time_Config={timeConfig} type={Type} />
            )}
        </div>
    );
}

export default DetermineTimeSpan;
