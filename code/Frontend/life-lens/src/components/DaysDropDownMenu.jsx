import React, { useState, useEffect } from 'react';
import loadData from '../loaders/loadData';

function DaysDropDownMenu() {
  const [days, setdays] = useState([]);
 
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



return(
  <div>
    <select >
    {days.map((day) => (
        <option value={day.days}>
          {day.days}
        </option>
      ))}
      </select>
  </div>
);


}

export default DaysDropDownMenu;