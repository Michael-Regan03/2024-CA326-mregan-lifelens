//covert to seconds for pie chart
function TimeConverter(timeString) {
    const [hours, minutes, seconds] = timeString.split(':').map(Number);
    return hours * 3600 + minutes * 60 + seconds;
}

export default TimeConverter