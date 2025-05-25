function showTab(tabId) {
  const contents = document.querySelectorAll('.tab-content');
  const buttons = document.querySelectorAll('.tabs button');

  contents.forEach(tab => tab.classList.remove('active'));
  buttons.forEach(btn => btn.classList.remove('active-tab'));

  document.getElementById(tabId).classList.add('active');
  event.target.classList.add('active-tab');
}
