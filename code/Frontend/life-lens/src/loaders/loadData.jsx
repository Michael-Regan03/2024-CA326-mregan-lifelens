import AuthFetchComp from "../actions/AuthFetchComp"
import FetchComp from "../actions/FetchComp"

//make a Auth request and if Auth token outdated , get new token and request again
const loadData = async(Url, HTTP_method, Body=null) => {
    const refreshToken = localStorage.getItem('refreshToken');
    try{
      //first request
      const response =  await AuthFetchComp(Url, HTTP_method, Body )
      return response
    } catch (error) {

      try{
        //request new access token
        const refresh = await FetchComp('http://127.0.0.1:8000/auth/jwt/refresh/',{refresh: refreshToken}, 'POST' )
        localStorage.setItem('accessToken', refresh.access);
        //second request with new Auth token
        const response =  await AuthFetchComp(Url, HTTP_method, Body)
        return response
      }catch(error){
        console.error('Refresh error:', error);
    }}}


export default loadData;