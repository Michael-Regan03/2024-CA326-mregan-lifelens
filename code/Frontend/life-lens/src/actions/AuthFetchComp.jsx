const AuthFetchComp =  async (url, HTTP_method, body=null) => {
  const accessToken = localStorage.getItem('accessToken'); 

  const headers = {
    Authorization: `Bearer ${accessToken}`,
  };

  const message = {
      method: HTTP_method,
  };
  

  if(body instanceof FormData){
    //Sending csv data
    message.body = body;
    message.headers = headers;

  }else if(body != null){
    //Sending JSON data
    message.body = JSON.stringify(body);
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    message.headers = headers;
  }else{
    //Requests without body i.e GET requests
    message.headers = headers;
  }


  
  
  try { 
      const response = await fetch( url , message); 
      if (!response.ok) {
          throw new Error('Network response was not ok');
        }
  
        return await response.json();
      } catch (error) {
          console.error('Error in AuthFetchComp:', error);
        
          //throwing error  to be handled by the caller
         throw error;
     }
  };

export default AuthFetchComp;