import { Client, Storage } from "appwrite";
import { ID } from "appwrite";
const client = new Client()
    .setEndpoint('https://cloud.appwrite.io/v1')
    .setProject('658c3e666ed66b56edb7');

const storage = new Storage(client);
let imageUrl = "";
const addon = "&mode=admin"
const bucketId = "658da6ec42519f39311a"
const uploadFile =async ()=>{
    try {
        
        // const response =await  storage.createFile(
        //     bucketId,
        //     ID.unique(),
        //     document.getElementById('uploader').files[0]
        // );
        const response = "65f69dc0a756bb191cc4"
        if(response){
            imageUrl =  storage.getFileView(bucketId,response)
            console.log(imageUrl.href+addon)
        }
    } catch (error) {
        console.log(error)
    }
}
uploadFile()


