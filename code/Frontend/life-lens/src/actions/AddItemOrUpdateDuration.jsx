import TimeConverter from "./TimeConverterSeconds";

const AddItemOrUpdateDuration = async (item, activities, durations) => {
    //Check if the actvity has already present in the list
    const actionIndex = activities.findIndex(act => act === item.action_label);
    //if the activity was had already taken place
    
    const duration = TimeConverter(item.duration)
    if (actionIndex !== -1) {
        //add durations
        durations[actionIndex] = durations[actionIndex] + duration;
        return {activities, durations}
    } else {
        activities.push(item.action_label)
        durations.push(duration)
        return {activities, durations}
    }
};

export default AddItemOrUpdateDuration