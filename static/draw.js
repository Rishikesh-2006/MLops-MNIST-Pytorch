const canvas = document.getElementById("Drawzone");

let ctx = canvas.getContext("2d");

let drawval = false;

canvas.width = 28;
canvas.height = 28;
let x2 = 0;
let y2 = 0;

const scale = 10;
ctx.lineWidth = 3;

canvas.addEventListener("mouseup",function(){

    drawval = false;
});

canvas.addEventListener("mousemove",function(info){

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

canvas.addEventListener("mousedown",function(){


    drawval = true;

});