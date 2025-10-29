(function () {
  var hero = document.querySelector('.layout--single .page__hero--overlay');
  var mast = document.querySelector('.layout--single .masthead');
  document.addEventListener('DOMContentLoaded', function () {
    document.body.classList.add('content-ready');
    if (!hero || !mast || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      if (!entries.length) return;
      if (entries[0].isIntersecting) mast.classList.remove('is-solid');
      else mast.classList.add('is-solid');
    }, { rootMargin: '-64px 0px 0px 0px', threshold: 0 });
    io.observe(hero);
  });
})();
