const FetchComp =  async (url, data, HTTP_method) => {
  try { 
    console.log('Sending data:', data);
    const response = await fetch( url , {
      method: HTTP_method,
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }); 
    
    if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      return await response.json();
    } catch (error) {
        console.error('Error in FetchComp:', error);
      
        //throwing error  to be handled by the caller
        throw error;
    }
  };

export default FetchComp;