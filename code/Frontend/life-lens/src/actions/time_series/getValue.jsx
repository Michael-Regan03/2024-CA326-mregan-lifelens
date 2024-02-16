const getValue =  async (time ,type) => {
    let output
      if(type == "emotionTension"){
        output = time.emotionTension
        return output
      }else if(type == "emotionPositive"){
        output = time.emotionPositive
        return output
      }
}



export default getValue;