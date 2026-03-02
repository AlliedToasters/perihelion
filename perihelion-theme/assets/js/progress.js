// Reading progress bar for chapter pages
(function () {
    var bar = document.getElementById('progress-bar');
    if (!bar) return;

    function updateProgress() {
        var scrollTop = window.scrollY;
        var docHeight = document.documentElement.scrollHeight - window.innerHeight;
        if (docHeight <= 0) {
            bar.style.width = '0%';
            return;
        }
        var percent = Math.min((scrollTop / docHeight) * 100, 100);
        bar.style.width = percent + '%';
    }

    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
})();
