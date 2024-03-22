import React from 'react'
import { useEffect, useRef } from 'react'
import Chart from 'chart.js/auto';
import { Client, Storage } from "appwrite";
const App = () => {
  const chart = useRef(null);
  const canvasRef = useRef(null);
  useEffect(() => {
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

  }, [])

  const client = new Client()
  .setEndpoint('https://cloud.appwrite.io/v1')
  .setProject('658c3e666ed66b56edb7');

const storage = new Storage(client);
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  const handleFileUpload = async () => {
    if (file) {
      try {
        const response = await storage.createFile(
          '658da6ec42519f39311a',
          ID.unique(),
          file
      );
        console.log(response.$id)
      } catch (error) {
        console.log("appwrite error",error )
      }
     
      
      console.log('Selected file:', file);
    } else {
      console.log('No file selected');
    }
  };



  return (
    <div className='w-screen h-screen flex flex-row gap-6 justify-center items-center' >
      <div className='w-1/2 h-1/2'>
        <canvas ref={canvasRef} id="myChart" className=''>
          <p>fallback call from llm</p>
        </canvas>
      </div>
      <div className='bg-violet-500 flex flex-row gap-4 justify-center items-center'>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload}>Upload</button>
      </div>

    </div>
  )
}

export default App