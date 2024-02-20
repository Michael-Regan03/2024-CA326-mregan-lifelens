const renderSelectOptions = (dict) => (
    Object.entries(dict).map(([key, value]) => (
        <option key={key} value={key}>{value}</option>
    )));

export default renderSelectOptions