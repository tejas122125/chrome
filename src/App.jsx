import React from 'react'
import { useEffect,useRef } from 'react'
import Chart from 'chart.js/auto';

const App = () => {
  const chart = useRef(null) ;
  const canvasRef = useRef(null);
  useEffect(()=>{
    // ctx = document.getElementById("myChart")
    // console.log(ctx)
    if (canvasRef.current) {
      const ctx = canvasRef.current.getContext('2d');
      if (ctx) {
        if (chart.current) {
          chart.current.destroy();
        }
  chart.current = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}
    }
    
},[])

  return (
    <div className='w-screen h-screen' > 
    <div className='w-1/2 h-1/2'>
    <canvas  ref={canvasRef} id="myChart" className=''>
      <p>fallback call  llm</p>
      </canvas>
    </div>
    
      </div>
  )
}

export default App