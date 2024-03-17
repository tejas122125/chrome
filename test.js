
import axios from 'axios';
const dataToSend = {
    "url":"https://cloud.appwrite.io/v1/storage/buckets/658da6ec42519f39311a/files/65f69dc0a756bb191cc4/view?project=658c3e666ed66b56edb7"
};

axios.post('http://127.0.0.1:8080/getdata', dataToSend)
    .then(response => {
        console.log('Response from Python API:', response.data);
    })
    .catch(error => {
        console.error('Error sending data to Python API:', error);
    });
