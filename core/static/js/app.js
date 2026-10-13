/* HM Bathroom | app.js
   The pages are plain HTML. This file only adds behaviour:
   1. the product gallery (arrows, thumbnails, counter)
   2. the enlarge modal (lightbox) on the product page
   Nothing here creates content. */

(function () {
  var track = document.querySelector(".gallery-track");
  if (!track) return;

  var slides = track.querySelectorAll(".slide");
  var thumbs = document.querySelectorAll(".thumb");
  var thumbsTrack = document.querySelector(".thumbs-track");
  var prev = document.querySelector(".g-prev");
  var next = document.querySelector(".g-next");
  var cur = document.querySelector(".g-cur");
  var box = document.getElementById("lightbox");
  var lbImg = box.querySelector(".lb-img");
  var n = slides.length;
  var idx = 0;

  function show(i) {
    idx = Math.max(0, Math.min(n - 1, i));
    for (var k = 0; k < thumbs.length; k++) thumbs[k].classList.toggle("is-active", k === idx);
    cur.textContent = idx + 1;
    prev.disabled = idx === 0;
    next.disabled = idx === n - 1;
    var t = thumbs[idx];
    thumbsTrack.scrollTo({ left: t.offsetLeft - (thumbsTrack.clientWidth - t.clientWidth) / 2, behavior: "smooth" });
  }
  function go(i) {
    i = Math.max(0, Math.min(n - 1, i));
    track.scrollTo({ left: i * track.clientWidth, behavior: "smooth" });
    show(i);
  }

  // swiping the main slider updates the counter and thumbnails
  track.addEventListener("scroll", function () {
    var i = Math.round(track.scrollLeft / track.clientWidth);
    if (i !== idx && i >= 0 && i < n) show(i);
  }, { passive: true });

  prev.addEventListener("click", function () { go(idx - 1); });
  next.addEventListener("click", function () { go(idx + 1); });
  for (var k = 0; k < thumbs.length; k++) {
    (function (i) { thumbs[i].addEventListener("click", function () { go(i); }); })(k);
  }
  track.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") { e.preventDefault(); go(idx - 1); }
    if (e.key === "ArrowRight") { e.preventDefault(); go(idx + 1); }
  });
  window.addEventListener("resize", function () { track.scrollLeft = idx * track.clientWidth; });

  // modal
  function openBox() {
    lbImg.src = slides[idx].querySelector("img").getAttribute("src");
    if (!box.open) box.showModal();
  }
  function step(d) {
    go(idx + d);
    lbImg.src = slides[idx].querySelector("img").getAttribute("src");
  }
  document.querySelector(".g-zoom").addEventListener("click", openBox);
  for (var s = 0; s < slides.length; s++) slides[s].addEventListener("dblclick", openBox);
  box.querySelector(".lb-close").addEventListener("click", function () { box.close(); });
  box.querySelector(".lb-prev").addEventListener("click", function () { step(-1); });
  box.querySelector(".lb-next").addEventListener("click", function () { step(1); });
  box.addEventListener("click", function (e) { if (e.target === box) box.close(); });
  box.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") step(-1);
    if (e.key === "ArrowRight") step(1);
  });

  show(0);
})();
