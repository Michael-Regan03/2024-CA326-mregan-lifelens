import TimeConverter from "./TimeConverterMinutes";

const AddItemOrUpdateDuration = async (item, activities, durations, clause) => {
    //Check if the actvity has already present in the list
    let actionIndex;
    if(clause == "activity"){
        actionIndex = activities.findIndex(act => act === item.action_label);
    
    }else if(clause == "travel"){
        if(item.actionSubOption === "light" || item.actionSubOption === "moderate" || item.actionSubOption === "heavy"){
            return {activities, durations}
        }else{
        
        actionIndex = activities.findIndex(act => act === item.actionSubOption);
    } }
    
    //if the activity was had already taken place
    
    const duration = TimeConverter(item.duration)
    if (actionIndex !== -1) {
        //add durations
        durations[actionIndex] = durations[actionIndex] + duration;
        return {activities, durations}
    } else {
        if(clause == "activity"){
            activities.push(item.action_label)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "travel"){
            activities.push(item.actionSubOption)
            durations.push(duration)
            return {activities, durations}
        }  
        

    }
};

export default AddItemOrUpdateDuration