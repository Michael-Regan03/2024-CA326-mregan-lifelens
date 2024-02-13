import React, { useState, useEffect } from 'react';
import loadData from '../loaders/loadData';
import GraphGen from './GraphGen';

function DaysDropDownMenu() {
  const [days, setdays] = useState([]);
  const [day, setDay] = useState([]);

  useEffect( () => {

    const fetchData = async () => {try{
      const responce = await loadData('http://127.0.0.1:8000/day/','GET')
      setdays(responce)
      console.log(responce)
  }catch(error){
    console.error(error)
  }
  
  };
  fetchData();},[])

  const handleChange = (event) => {
    setDay(event.target.value);

  };

return(
  <div>
    <select onChange={handleChange} >
    
    <option>Select Day</option> //current solution to single day issue
    //Can only handle multiple days
    {days.map((day) => (
        <option value={day.date}  >
          {day.date}
        </option>
      ))}
      </select>
      <GraphGen date={day} />
  </div>
);


}

export default DaysDropDownMenu;