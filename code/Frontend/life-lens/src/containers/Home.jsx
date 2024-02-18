import Header from '../components/Header';
import Navbar from '../components/LoggedInNavbar';
import DaysDropDownMenu from '../components/DaysDropDownMenu';

function Homepage() {
  return(
    <div>
        <Header></Header>
        <DaysDropDownMenu> </DaysDropDownMenu>
    </div>
  );
}

export default Homepage;