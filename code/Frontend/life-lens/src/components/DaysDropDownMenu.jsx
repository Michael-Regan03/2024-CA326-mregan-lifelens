import React, { useState, useEffect } from 'react';
import loadData from '../loaders/loadData';
import GraphGenActivities from './GraphGenActivities';
import GraphGenEmotionData from './GraphGenEmotionData';
import GraphGenTravelMethod from './GraphGenTravelMethod';


function DaysDropDownMenu() {
  const [date, setDate] = useState([]);

  const [years, setYears] = useState([]);
  const [months, setMonths] = useState([]);
  const [days, setDays] = useState([]);


  const [year, setYear] = useState([]);
  const [month, setMonth] = useState([]);
  const [day, setDay] = useState([]);

  //unique data struct of value, key pairs where key=years and value = another key,value pair where key=month
  // and values=lists of each day in that month
  const [dataStruct, setDataStruct] = useState({})



  const getYearsMonthsDays = async (item, dateStruct) => {
    //seperate year, month, day from date
    const [year, month, day] = item.date.split('-').map(Number);

    if (!dateStruct[year]){
      //log the year if it doesnt exist
      dateStruct[year] = {}
    };
    if (!dateStruct[year][month]) {
      //log the month for that year if it doesnt exist already
      dateStruct[year][month] = []
    };
    //log the day for the that month in that year
    dateStruct[year][month].push(day);
    return {dateStruct}
};
  

  useEffect( () => {

    const fetchData = async () => {
      try{
        const response = await loadData('http://127.0.0.1:8000/day/','GET')
        if (response && response.length > 0) {
          let dateStruct = {};
          for(const item of response) {
              //years, months and days must be passed to the func as lists instead of setting hooks as the hooks werent async updating
              ({dateStruct} = await getYearsMonthsDays(item, dateStruct));
          
          } 
          setDataStruct(dateStruct);
       
      } else {
          console.log("No data:");
      }
  }catch(error){
    console.error(error)
  }
  
  };
  fetchData();},[])

  useEffect( () => {

    const dates = Object.entries(dataStruct);

    const years = []

    dates.forEach(([year, monthData]) => {
      years.push(year)
    });

    setYears(years)

  },[dataStruct])


  //handles year selection
  const handleChange1 = (event) => {
    console.log(event.target.value )
    if(event.target.value === "Select Year"){
      setMonths([])
      setDays([])
    }else{
      setDate(event.target.value);
      setYear(event.target.value)
      const dates = dataStruct[event.target.value] || {};
      const dates_entires = Object.entries(dates);

      const months_selected = []

      dates_entires.forEach(([month, day]) => {
        months_selected.push(month)   
      });

      setMonths(months_selected)
  };}

  //handels month selection
  const handleChange2 = (event) => {
    console.log(event.target.value )
    if(event.target.value === "Select Month"){
      setDays([])
      setDate(String(year))
    }else{}
        setDate(String(year)+"-"+String(event.target.value));
        setMonth(event.target.value)
        
        const dates = dataStruct[year][event.target.value];
  
        setDays(dates)
    };

  //handles day selection
  const handleChange3 = (event) => {
      console.log(event.target.value )
      if(event.target.value !== "Select Day"){
        setDate(String(year)+"-"+String(month)+"-"+String(event.target.value));
        setDay(event.target.value)
      }};


return(
  <div>
    <select onChange={handleChange1} >
    <option>Select Year</option> 

    {years.map((year) => (
        <option value={year}  >
          {year}
        </option>
      ))}
    </select> 
    
    {/*!== underdefined is important for not crashing the app when setMonths([]) is called as
     tryning to get months len after will cause errors */}
    {months !== undefined && months.length > 0 && 
    (<select onChange={handleChange2} >
    <option>Select Month</option> 

    {months.map((month) => (
        <option value={month}  >
          {month}
        </option>
      ))}
    </select>)} 

    {days !== undefined &&  days.length > 0 && 
    <select onChange={handleChange3} >
    <option>Select Day</option> 
  
    {days.map((day) => (
        <option value={day}  >
          {day}
        </option>
      ))}
    </select>} 
     <h2>Visualising data from: {date}</h2>
     <GraphGenActivities date={date}  /> 
     <GraphGenEmotionData date={date} type={"emotionPositive"} />
     <GraphGenEmotionData date={date} type={"emotionTension"} />
     <GraphGenTravelMethod date={date} />
  </div>
);


}

export default DaysDropDownMenu;