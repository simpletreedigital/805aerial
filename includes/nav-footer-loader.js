(function () {
  function runScripts(container) {
    var scripts = container.tagName === 'SCRIPT'
      ? [container]
      : Array.prototype.slice.call(container.querySelectorAll('script'));
    scripts.forEach(function (oldScript) {
      var newScript = document.createElement('script');
      for (var i = 0; i < oldScript.attributes.length; i++) {
        var attr = oldScript.attributes[i];
        newScript.setAttribute(attr.name, attr.value);
      }
      newScript.text = oldScript.textContent;
      oldScript.parentNode.replaceChild(newScript, oldScript);
    });
  }

  function inject(html, position) {
    var wrapper = document.createElement('div');
    wrapper.innerHTML = html;
    var nodes = Array.prototype.slice.call(wrapper.children);
    var anchor = position === 'start' ? document.body.firstChild : null;
    nodes.forEach(function (node) {
      if (position === 'start') {
        document.body.insertBefore(node, anchor);
      } else {
        document.body.appendChild(node);
      }
      runScripts(node);
    });
    return nodes[0];
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
