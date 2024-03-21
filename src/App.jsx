import "./index.css"

import { Bar  } from 'react-chartjs-2';
import { Chart } from 'chart.js'; // Import Chart for registration

Chart.register(Chart.defaults.plugins);
import barChartData from './Barchart';
function App() {
  const options = {
    scales: {
      xAxes: [{
        type: 'category', // Use the registered CategoryScale
        scaleLabel: {
          display: true,
          labelString: 'Months' // Optional label for the x-axis
        }
      }]
    }
  };
  


  return (
    <>
      <div className="w-screen h-screen">
      <h1>React Interactive Bar Chart</h1>
      <div className="w-96 h-1/2">
      <Bar data={barChartData} options={options} />
      </div>
     
    </div>
    </>
  )
}

export default App
