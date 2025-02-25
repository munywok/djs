// JavaScript for Accordion Functionality
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
      const question = item.querySelector('.faq-question');
      question.addEventListener('click', () => {
        // Close other open answers
        faqItems.forEach(i => {
          if (i !== item) {
            i.querySelector('.faq-answer').style.display = 'none';
            i.querySelector('.faq-toggle').textContent = '+';
          }
        });

        // Toggle the clicked question's answer
        const answer = item.querySelector('.faq-answer');
        const toggle = item.querySelector('.faq-toggle');
        if (answer.style.display === 'block') {
          answer.style.display = 'none';
          toggle.textContent = '+';
        } else {
          answer.style.display = 'block';
          toggle.textContent = '-';
        }
      });
    });

    <script>
  if (window.location.href.endsWith(".html")) {
    window.location.href = window.location.href.replace(".html", "");
  }