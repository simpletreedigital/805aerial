(function () {
  function inject(html, position) {
    var wrapper = document.createElement('div');
    wrapper.innerHTML = html;
    var node = wrapper.firstElementChild;
    if (position === 'start') {
      document.body.insertBefore(node, document.body.firstChild);
    } else {
      document.body.appendChild(node);
    }
    return node;
  }

  function fetchInclude(path, cb) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', path, true);
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        cb(xhr.responseText);
      }
    };
    xhr.send();
  }

  function wireNav() {
    document.querySelectorAll('.gnav-item > button').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleDrop(btn.closest('.gnav-item').id);
      });
    });
    document.querySelectorAll('.gnav-burger').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelector('.gnav-links').classList.toggle('open');
      });
    });
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    document.querySelectorAll('.gnav-links a').forEach(function (a) {
      var href = a.getAttribute('href').replace(/\/$/, '') || '/';
      if (href === path) a.classList.add('active');
    });
  }

  function boot() {
    fetchInclude('/includes/nav.html', function (html) {
      inject(html, 'start');
      wireNav();
    });
    fetchInclude('/includes/footer.html', function (html) {
      inject(html, 'end');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
