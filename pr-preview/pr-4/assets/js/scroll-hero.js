(function(){
  var hero=document.querySelector('.layout--single .page__hero--overlay');
  var mast=document.querySelector('.layout--single .masthead');
  document.addEventListener('DOMContentLoaded',function(){
    document.body.classList.add('content-ready');
    if(mast&&'IntersectionObserver'in window){
      var io=new IntersectionObserver(function(e){if(!e.length)return;e[0].isIntersecting?mast.classList.remove('is-solid'):mast.classList.add('is-solid')},{rootMargin:'-64px 0px 0px 0px',threshold:0});io.observe(hero);
    }
    if(!hero)return;
    var last=-1;var rate=0.25;
    function onScroll(){
      var y=window.scrollY*rate;
      if(Math.abs(y-last)>0.5){hero.style.setProperty('--heroY',(-y)+'px');last=y;}
      requestAnimationFrame(onScroll);
    }
    requestAnimationFrame(onScroll);
  });
})();
