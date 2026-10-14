// Gallery previews use smaller images; enlarged viewers retain the original files.
window.setBackdroppedImage = function (img, source, sizes) {
  const media = window.backdroppedMedia?.[source];
  if (media) {
    img.src = media.small;
    img.srcset = media.small + ' ' + media.smallWidth + 'w, ' + media.large + ' ' + media.largeWidth + 'w';
    img.sizes = sizes || '(max-width: 760px) 92vw, (max-width: 1080px) 44vw, 29vw';
    img.width = media.width; img.height = media.height;
    img.addEventListener('error', () => {
      img.removeAttribute('srcset'); img.src = source;
    }, { once: true });
  } else { img.src = source; }
  img.decoding = 'async';
};

// Some mobile browsers defer lazy images inside a closed disclosure indefinitely.
// Brand logos are small, so request them eagerly and keep their native image markup.
document.querySelectorAll('.more-brands').forEach(section => {
  section.addEventListener('toggle', () => {
    if (section.open) section.querySelectorAll('img').forEach(img => { img.loading = 'eager'; });
  });
});

document.querySelectorAll(".brand-logo").forEach(img => { img.addEventListener("error", () => { if (img.getAttribute("src").endsWith(".webp")) img.src = "assets/delivery/backdropped-logo.png"; }, { once: true }); });
