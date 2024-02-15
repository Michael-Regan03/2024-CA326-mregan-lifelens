import moment from 'moment-timezone'; //import thrid party library


function KoreanTimeConverter(time, request){
    //convert to korean time as dataset if from korea
    const koreanTime = moment(time).tz('Asia/Seoul');
    switch (request) {
        case 'day':
            return koreanTime.date();
        case 'month':
            // Since month() is 0 indexed
            return koreanTime.month() + 1; 
        case 'year':
            return koreanTime.year();
        case 'yearMonth':
            return koreanTime.format('YYYY-MM');
        case 'yearMonthDay':
                return koreanTime.format('YYYY-MM-DD');
        case 'date':
        default:
            return koreanTime.format('YYYY-MM-DD HH:mm');
}}

export default KoreanTimeConverter;