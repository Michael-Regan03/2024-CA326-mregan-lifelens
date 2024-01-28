import React, { useState, useEffect } from 'react';

const FetchComponent = ({ url, method, headers, body, onResponse }) => {
  useEffect(() => {
    const fetchData = async () => {
      const requestOptions = {
        method: method,
        headers: headers,
        body: JSON.stringify(body)
      };

      try {
        const response = await fetch(url, requestOptions);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const json = await response.json();
        onResponse(json); 
      } catch (error) {
        console.error('Fetch error: ', error);
        onResponse(null, error); 
      }
    };

    if (url && method && headers && body) {
      fetchData();
    }
  }, [url, method, headers, body, onResponse]); // Add onResponse to dependencies

  return null; 
};

export default FetchComponent;