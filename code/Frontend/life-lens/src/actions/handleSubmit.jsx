
const handleSubmit =  async (url, data) => {
    try { 
    console.log('Sending data:', data);
    const response = await fetch( url , {
      method: 'POST',
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
      // You can choose to handle the error here or throw it to be handled by the caller
      console.error('Error in handleSubmit:', error);
      throw error;
    }
  };

export default handleSubmit;