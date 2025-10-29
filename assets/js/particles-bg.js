(function(){
  var c=document.getElementById('bgfx');if(!c)return;var d=c.getContext('2d');var w,h,px=[],N=80;
  function rs(){w=window.innerWidth;h=window.innerHeight;c.width=w;c.height=h}
  function rnd(a,b){return Math.random()*(b-a)+a}
  function init(){px=[];for(var i=0;i<N;i++){px.push({x:rnd(0,w),y:rnd(0,h),vx:rnd(-0.15,0.15),vy:rnd(-0.15,0.15)})}}
  function step(){
    d.clearRect(0,0,w,h);
    d.fillStyle='rgba(255,255,255,0.06)';
    for(var i=0;i<N;i++){
      var p=px[i];p.x+=p.vx;p.y+=p.vy;
      if(p.x<0||p.x>w)p.vx*=-1;if(p.y<0||p.y>h)p.vy*=-1;
      d.beginPath();d.arc(p.x,p.y,1.2,0,6.283);d.fill();
    }
    d.strokeStyle='rgba(255,255,255,0.06)';d.lineWidth=1;
    for(var i=0;i<N;i++)for(var j=i+1;j<N;j++){
      var dx=px[i].x-px[j].x,dy=px[i].y-px[j].y,dd=dx*dx+dy*dy;
      if(dd<14000){d.globalAlpha=1-dd/14000;d.beginPath();d.moveTo(px[i].x,px[i].y);d.lineTo(px[j].x,px[j].y);d.stroke()}
    }
    d.globalAlpha=1;
    requestAnimationFrame(step);
  }
  window.addEventListener('resize',function(){rs();init()});
  rs();init();step();
})();
