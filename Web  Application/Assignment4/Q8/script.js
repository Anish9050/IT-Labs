// Array of images
let images = [
    "https://picsum.photos/id/1015/400/250",
    "https://picsum.photos/id/1016/400/250",
    "https://picsum.photos/id/1018/400/250",
    "https://picsum.photos/id/1020/400/250"
];

let index = 0;
let slider = document.getElementById("sliderImage");

// Display first image
slider.src = images[index];

// Next button
function nextImage(){
    index++;

    if(index >= images.length)
        index = 0;

    slider.src = images[index];
}

// Previous button
function prevImage(){
    index--;

    if(index < 0)
        index = images.length - 1;

    slider.src = images[index];
}

// Auto slide every 3 seconds
setInterval(nextImage, 3000);