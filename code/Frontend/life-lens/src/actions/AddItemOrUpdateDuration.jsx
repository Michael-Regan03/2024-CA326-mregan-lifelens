import TimeConverter from "./TimeConverterMinutes";

const AddItemOrUpdateDuration = async (item, activities, durations, clause) => {
    //Check if the actvity has already present in the list
    let actionIndex;
    if(clause === "action"){
        actionIndex = activities.findIndex(act => act === item.action_label);
    }else if(clause === "condition"){
         actionIndex = activities.findIndex(act => act === item.condition);
    }else if(clause === "conditionSub1"){
        actionIndex = activities.findIndex(act => act === item.conditionSub1Option_label);
    }else if(clause === "conditionSub2"){
        actionIndex = activities.findIndex(act => act === item.conditionSub2Option_label);
    }else if(clause === "place"){
        actionIndex = activities.findIndex(act => act === item.place);
    }else if(clause === "activity"){
        actionIndex = activities.findIndex(act => act === item.activity_label);
    }else if(clause === "travel"){
        if(item.actionSubOption === "light" || item.actionSubOption === "moderate" || item.actionSubOption === "heavy"){
            return {activities, durations}
        }else{
            actionIndex = activities.findIndex(act => act === item.actionSubOption);
    
        }
    }

    //if the activity was had already taken place
    
    const duration = TimeConverter(item.duration)
    if (actionIndex !== -1) {
        //add durations
        durations[actionIndex] = durations[actionIndex] + duration;
        return {activities, durations}
    } else {
        if(clause == "action"){
            activities.push(item.action_label)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "travel"){
            activities.push(item.actionSubOption)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "conditionSub1"){
            activities.push(item.conditionSub1Option_label)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "conditionSub2"){
            activities.push(item.conditionSub2Option_label)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "condition"){
            activities.push(item.condition)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "place"){
            activities.push(item.place)
            durations.push(duration)
            return {activities, durations}
        }else if(clause == "activity"){
            activities.push(item.activity_label)
            durations.push(duration)
            return {activities, durations}
        } 
        

    }
};

export default AddItemOrUpdateDuration