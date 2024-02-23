import '../style_components/Homepage.css'

function Homepage() {
  return(
    <div>
        <h2 className="HomepageHeader">About Life Lens</h2>
        <p className="HomepageText">Life Lens is a web application that helps its user's extract meaningful insight from their lifelog data
           through visualisations. It also uses that lifelog data alongside user information to run a chronic illness
          risk assessments of 10 different chronic illnesses ranking the user either 'low-risk', 'mid-risk' or 'high-risk'
          of each illness. In this way Life Lens can be used to help its users prevent chronic illness and maintain good health.</p>
    </div>
  );
}

export default Homepage;