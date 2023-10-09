console.log("welcome to spotify");

//Initialize the Variables
let songIndex=0;
let audioElement=new Audio('1.mp3');
let masterPlay=document.getElementById('masterPlay');
let myProgressBar=document.getElementById('myProgressBar')
let gif=document.getElementById('gif');

let songs=[
    {songName:"salam-e-ishq",filePath:"songs/1.mp3", coverPath:"covers/1.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/2.mp3", coverPath:"covers/2.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/3.mp3", coverPath:"covers/3.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/4.mp3", coverPath:"covers/4.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/5.mp3", coverPath:"covers/5.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/6.mp3", coverPath:"covers/6.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/7.mp3", coverPath:"covers/7.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/8.mp3", coverPath:"covers/8.jpg"},
    {songName:"salam-e-ishq",filePath:"songs/9.mp3", coverPath:"covers/9.jpg"},
]

//audioElement.play();
//Handle play/pause click
masterPlay.addEventListener('click',()=>{
    if(audioElement.paused || audioElement.currentTime<=0){
        audioElement.play();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        gif.style.opacity=1;
    }
    else{
        audioElement.pause();
        masterPlay.classList.remove('fa-play-circle');
        masterPlay.classList.add('fa-pause-circle');
        gif.style.opacity=0;
    }
})

//List to Events
audioElement.addEventListener('timeupdate',()=>{
  
    //update Seekbar
    progress=parseInt((audioElement.currenttime/audioElement.duration)* 100);
    myProgressBar.value=progress;

})

myProgressBar.addEventListener('change',()=>{
    audioElement.currentTime = myProgressBar.value*audioElement.duration/100;
})

