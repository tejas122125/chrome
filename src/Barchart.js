const barChartData = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [{
    label: 'Sales', // Label for the dataset
    backgroundColor: 'rgba(255, 99, 132, 0.2)', // Bar color with transparency
    borderColor: 'rgba(255, 99, 132, 1)', // Border color
    borderWidth: 1, // Border width
    hoverBackgroundColor: 'rgba(255, 99, 132, 0.4)', // Hover color with transparency
    hoverBorderColor: 'rgba(255, 99, 132, 1)', // Hover border color
    data: [65, 59, 80, 81, 56, 55, 40] // Data values for each bar
  }]
};

export default barChartData;