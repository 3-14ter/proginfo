const crest = document.getElementsByClassName('crest')[0];

      crest.addEventListener('mousemove', (e) => {
        const rect = crest.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;

        crest.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.15)`;
      });

      crest.addEventListener('mouseleave', () => {
        crest.style.transform = 'rotateX(0) rotateY(0) scale(1)';
      });    