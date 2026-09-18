const canvas = document.getElementById("Drawzone");

let ctx = canvas.getContext("2d");

const Submit = document.getElementById("pred");
let drawval = false;

canvas.width = 28;
canvas.height = 28;

ctx.fillStyle = "black";
ctx.fillRect(0, 0, canvas.width, canvas.height);

ctx.strokeStyle = "white";

let x2 = 0;
let y2 = 0;

const scale = 10;
ctx.lineWidth = 4
ctx.lineCap = "round";
ctx.lineJoin = "round";


//touch

canvas.addEventListener("pointerup",function(){

    drawval = false;

});

canvas.addEventListener("pointerleave",function(){

    drawval = false;

});

canvas.addEventListener("pointermove",function(info){

    let x = info.offsetX/scale;
    let y = info.offsetY/scale;



    if(drawval === true)
    {
        ctx.beginPath();
        ctx.moveTo(x,y);

        ctx.lineTo(x2,y2);
        ctx.stroke();
        
    }

    x2 = x;
    y2 = y;


});

canvas.addEventListener("pointerdown",function(info){

    
    let x = info.offsetX/scale;
    let y = info.offsetY/scale;

    drawval = true;

});
//save as png
Submit.addEventListener("click",function(){
    canvas.toBlob(function(blob){

        const formdata = new FormData();
        formdata.append("image",blob,"image.png");

        fetch("/predict"
            ,{
            method : "post",
            body : formdata
        })
        .then(response => response.text())
        .then(data => {
            document.open();
            document.write(data);
            document.close();
        });
},"image/png")  
});
