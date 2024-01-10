import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DailyActivityForm from'./components/DailyActivityForm';

function App() {
  return (
    <BrowserRouter>
       <Routes>
         <Route path="/" element={<DailyActivityForm />}/>
       </Routes>
     </BrowserRouter>
   );
}

export default App;
