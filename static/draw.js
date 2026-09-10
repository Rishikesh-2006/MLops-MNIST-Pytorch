const canvas = document.getElementById("Drawzone");

let ctx = canvas.getContext("2d");

let drawval = false;

canvas.width = 300;
canvas.height = 300;

canvas.addEventListener("mouseup",function(){

    drawval = false;
});

canvas.addEventListener("mousemove",function(info){

    let x = info.offsetX;
    let y = info.offsetY;

    if(drawval === true)
    {
        ctx.beginPath();
        ctx.arc(x,y,20,0,2*Math.PI);
        ctx.stroke();
    }


});



canvas.addEventListener("mousedown",function(){

    drawval = true;

});