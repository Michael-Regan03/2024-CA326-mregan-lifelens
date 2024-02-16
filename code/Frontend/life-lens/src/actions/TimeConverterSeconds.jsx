//covert to seconds for pie chart
function TimeConverter(timeString) {
    const [hours, minutes, seconds] = timeString.split(':').map(Number);
    //covert to return minutes
    return hours * 60 + minutes + seconds / 60;
}

export default TimeConverter